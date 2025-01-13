"""
Twitter (X) API Integration
Focuses on finding viral content and managing engagement
"""

import tweepy
import asyncio
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import logging
import json

from ..config import PLATFORMS

class TwitterAPI:
    def __init__(self):
        self.config = PLATFORMS['twitter']
        self.client = self._setup_client()
        self.engagement_cache = {}
        self.rate_limit_cache = {}
        
    def _setup_client(self) -> tweepy.Client:
        """Initialize Twitter API client"""
        return tweepy.Client(
            bearer_token="YOUR_BEARER_TOKEN",
            consumer_key="YOUR_API_KEY",
            consumer_secret="YOUR_API_SECRET",
            access_token="YOUR_ACCESS_TOKEN",
            access_token_secret="YOUR_ACCESS_SECRET"
        )
        
    async def get_viral_opportunities(self, min_ratio: float = 2.0) -> List[Dict]:
        """Find tweets with abnormally high engagement relative to follower count"""
        opportunities = []
        
        # Search for tweets in relevant categories
        for category in self.config['content_categories']:
            tweets = await self._search_category(category)
            
            for tweet in tweets:
                engagement_ratio = self._calculate_engagement_ratio(tweet)
                if engagement_ratio > min_ratio:
                    opportunities.append({
                        'tweet': tweet,
                        'engagement_ratio': engagement_ratio,
                        'category': category
                    })
        
        return sorted(opportunities, key=lambda x: x['engagement_ratio'], reverse=True)
        
    async def _search_category(self, category: str) -> List[Dict]:
        """Search for tweets in a specific category"""
        search_queries = self._get_category_queries(category)
        results = []
        
        for query in search_queries:
            try:
                tweets = await self._search_with_metadata(query)
                results.extend(tweets)
            except Exception as e:
                logging.error(f"Error searching category {category}: {str(e)}")
                
        return results
        
    def _get_category_queries(self, category: str) -> List[str]:
        """Get optimized search queries for each category"""
        queries = {
            'technology': [
                'AI filter:links min_faves:1000',
                'artificial intelligence filter:links min_faves:1000',
                'tech innovation filter:links min_faves:500',
                'future of tech filter:links min_faves:500'
            ],
            'spirituality': [
                'meditation mindfulness min_faves:500',
                'spiritual growth min_faves:500',
                'consciousness awakening min_faves:500',
                'divine wisdom min_faves:500'
            ],
            'personal_growth': [
                'self development min_faves:500',
                'personal growth min_faves:500',
                'life lessons learned min_faves:500',
                'growth mindset min_faves:500'
            ],
            'entrepreneurship': [
                'startup success min_faves:1000',
                'entrepreneur tips min_faves:1000',
                'business growth min_faves:500',
                'founder advice min_faves:500'
            ],
            'ai_innovation': [
                'GPT-4 filter:links min_faves:1000',
                'AI agents filter:links min_faves:1000',
                'machine learning breakthrough min_faves:500',
                'AI development min_faves:500'
            ]
        }
        
        return queries.get(category, [f"{category} min_faves:500"])
        
    async def _search_with_metadata(self, query: str) -> List[Dict]:
        """Search tweets with engagement metadata"""
        try:
            tweets = self.client.search_recent_tweets(
                query=query,
                tweet_fields=['public_metrics', 'created_at', 'author_id'],
                user_fields=['public_metrics'],
                expansions=['author_id'],
                max_results=100
            )
            
            return self._process_tweets(tweets)
        except Exception as e:
            logging.error(f"Error in search: {str(e)}")
            return []
            
    def _process_tweets(self, response) -> List[Dict]:
        """Process tweet data and add engagement metrics"""
        if not response.data:
            return []
            
        processed_tweets = []
        users = {user.id: user for user in response.includes['users']}
        
        for tweet in response.data:
            user = users.get(tweet.author_id)
            if user:
                processed_tweets.append({
                    'id': tweet.id,
                    'text': tweet.text,
                    'created_at': tweet.created_at,
                    'metrics': tweet.public_metrics,
                    'author': {
                        'id': user.id,
                        'followers_count': user.public_metrics['followers_count'],
                        'following_count': user.public_metrics['following_count']
                    }
                })
                
        return processed_tweets
        
    def _calculate_engagement_ratio(self, tweet: Dict) -> float:
        """Calculate engagement ratio relative to follower count"""
        metrics = tweet['metrics']
        followers = tweet['author']['followers_count']
        
        if followers == 0:
            return 0
            
        engagement = (
            metrics['like_count'] +
            metrics['retweet_count'] * 2 +
            metrics['reply_count'] * 3 +
            metrics.get('quote_count', 0) * 2
        )
        
        return engagement / followers
        
    async def check_rate_limits(self) -> bool:
        """Check if we're within rate limits"""
        current_time = datetime.now()
        
        # Clean old entries
        self.rate_limit_cache = {
            k: v for k, v in self.rate_limit_cache.items()
            if v['timestamp'] > current_time - timedelta(hours=1)
        }
        
        # Count recent actions
        recent_actions = len(self.rate_limit_cache)
        
        return recent_actions < self.config['daily_interaction_limit']
        
    async def post_response(self, tweet: Dict, response: str):
        """Post a response to a tweet"""
        try:
            result = self.client.create_tweet(
                text=response,
                in_reply_to_tweet_id=tweet['id']
            )
            
            # Update rate limit cache
            self.rate_limit_cache[result.data['id']] = {
                'timestamp': datetime.now(),
                'type': 'reply'
            }
            
            return result.data['id']
        except Exception as e:
            logging.error(f"Error posting response: {str(e)}")
            return None
            
    async def get_trending_topics(self) -> List[Dict]:
        """Get trending topics with their categories"""
        try:
            trends = self.client.get_trends(id=1)  # 1 is the woeid for worldwide
            categorized_trends = await self._categorize_trends(trends)
            return categorized_trends
        except Exception as e:
            logging.error(f"Error getting trends: {str(e)}")
            return []
            
    async def _categorize_trends(self, trends) -> List[Dict]:
        """Categorize trending topics"""
        categorized = []
        for trend in trends:
            categories = await self._detect_trend_categories(trend)
            if categories:
                categorized.append({
                    'trend': trend,
                    'categories': categories
                })
        return categorized
        
    async def _detect_trend_categories(self, trend: Dict) -> List[str]:
        """Detect categories for a trending topic"""
        # Implement category detection logic
        return []  # Placeholder 