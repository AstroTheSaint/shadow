"""
Content Monitoring System
Tracks trending content and determines optimal engagement opportunities
"""

import asyncio
from typing import Dict, List, Optional
import logging
from datetime import datetime

from .config import (
    PLATFORMS,
    GROWTH_INTEGRATION,
    ALIGNMENT_METRICS,
    DISCOVERY_SETTINGS
)
from .platform_apis import TwitterAPI, LinkedInAPI, RedditAPI, InstagramAPI
from .growth_analyzer import GrowthAnalyzer
from .content_scorer import ContentScorer
from .response_generator import ResponseGenerator

class ContentMonitor:
    def __init__(self):
        self.growth_analyzer = GrowthAnalyzer()
        self.content_scorer = ContentScorer()
        self.response_generator = ResponseGenerator()
        
        # Initialize platform APIs
        self.platforms = {
            'twitter': TwitterAPI(),
            'linkedin': LinkedInAPI(),
            'reddit': RedditAPI(),
            'instagram': InstagramAPI()
        }
        
        self.trending_cache = {}
        self.engagement_opportunities = []
        
    async def start_monitoring(self):
        """Start all monitoring tasks"""
        tasks = [
            self.monitor_trending_topics(),
            self.scan_engagement_opportunities(),
            self.check_content_relevance(),
            self.process_engagement_queue()
        ]
        await asyncio.gather(*tasks)
        
    async def monitor_trending_topics(self):
        """Monitor trending topics across platforms"""
        while True:
            for platform, api in self.platforms.items():
                trends = await api.get_trending_topics()
                relevant_trends = self.filter_relevant_trends(trends, platform)
                self.trending_cache[platform] = relevant_trends
            
            await asyncio.sleep(
                self.parse_time(DISCOVERY_SETTINGS['monitoring_frequency']['trending_topics'])
            )
            
    async def scan_engagement_opportunities(self):
        """Scan for high-engagement content"""
        while True:
            for platform, api in self.platforms.items():
                config = PLATFORMS[platform]
                
                # Get high-engagement content
                content = await api.get_trending_content(
                    min_engagement=config['engagement_threshold']
                )
                
                # Score content for personal relevance
                scored_content = [
                    {
                        'content': item,
                        'score': await self.score_content_relevance(item, platform)
                    }
                    for item in content
                ]
                
                # Filter and add to opportunities
                for item in scored_content:
                    if item['score'] >= ALIGNMENT_METRICS['personal_relevance']['current_journey']:
                        self.engagement_opportunities.append({
                            'platform': platform,
                            'content': item['content'],
                            'score': item['score'],
                            'timestamp': datetime.now()
                        })
            
            await asyncio.sleep(
                self.parse_time(DISCOVERY_SETTINGS['monitoring_frequency']['engagement_scan'])
            )
            
    async def check_content_relevance(self):
        """Continuously check content relevance against personal growth"""
        while True:
            current_state = await self.growth_analyzer.get_current_state()
            
            # Update content scoring based on current state
            self.content_scorer.update_relevance_model(current_state)
            
            # Re-score existing opportunities
            self.engagement_opportunities = [
                opp for opp in self.engagement_opportunities
                if await self.validate_opportunity(opp)
            ]
            
            await asyncio.sleep(
                self.parse_time(DISCOVERY_SETTINGS['monitoring_frequency']['relevance_check'])
            )
            
    async def process_engagement_queue(self):
        """Process and act on engagement opportunities"""
        while True:
            if self.engagement_opportunities:
                opportunity = self.engagement_opportunities[0]
                
                if await self.should_engage(opportunity):
                    response = await self.response_generator.generate_response(
                        opportunity['content'],
                        opportunity['platform']
                    )
                    
                    if response:
                        await self.engage(opportunity, response)
                        
                self.engagement_opportunities.pop(0)
            
            await asyncio.sleep(1)  # Check queue every second
            
    async def score_content_relevance(self, content: Dict, platform: str) -> float:
        """Score content relevance based on personal growth and engagement potential"""
        personal_score = await self.content_scorer.score_personal_relevance(content)
        engagement_score = await self.content_scorer.score_engagement_potential(
            content, platform
        )
        
        return (
            personal_score * ALIGNMENT_METRICS['personal_relevance']['current_journey'] +
            engagement_score * ALIGNMENT_METRICS['engagement_potential']['trending_factor']
        )
        
    async def validate_opportunity(self, opportunity: Dict) -> bool:
        """Validate if an engagement opportunity is still relevant"""
        # Check if content is still trending
        still_trending = await self.platforms[opportunity['platform']].check_content_status(
            opportunity['content']
        )
        
        if not still_trending:
            return False
            
        # Re-score based on current state
        new_score = await self.score_content_relevance(
            opportunity['content'],
            opportunity['platform']
        )
        
        # Update score
        opportunity['score'] = new_score
        
        return new_score >= ALIGNMENT_METRICS['personal_relevance']['current_journey']
        
    async def should_engage(self, opportunity: Dict) -> bool:
        """Determine if we should engage with this opportunity"""
        platform = opportunity['platform']
        
        # Check rate limits
        if not await self.platforms[platform].check_rate_limits():
            return False
            
        # Verify alignment hasn't changed
        if not await self.validate_opportunity(opportunity):
            return False
            
        return True
        
    async def engage(self, opportunity: Dict, response: str):
        """Engage with content on the platform"""
        platform = opportunity['platform']
        content = opportunity['content']
        
        try:
            await self.platforms[platform].post_response(content, response)
            logging.info(f"Engaged with content on {platform}: {response[:100]}...")
        except Exception as e:
            logging.error(f"Failed to engage on {platform}: {str(e)}")
            
    @staticmethod
    def parse_time(time_str: str) -> int:
        """Parse time string to seconds"""
        unit = time_str[-1]
        value = int(time_str[:-1])
        
        if unit == 's':
            return value
        elif unit == 'm':
            return value * 60
        elif unit == 'h':
            return value * 3600
        
        raise ValueError(f"Invalid time format: {time_str}")
        
    def filter_relevant_trends(self, trends: List[Dict], platform: str) -> List[Dict]:
        """Filter trends based on platform-specific criteria"""
        config = PLATFORMS[platform]
        
        return [
            trend for trend in trends
            if any(category in trend['categories'] for category in config['content_categories'])
        ] 