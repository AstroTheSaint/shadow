"""
Response Generator
Creates authentic, personality-aligned responses for social media engagement
"""

import logging
from typing import Dict, Optional
from datetime import datetime

from .config import RESPONSE_GUIDELINES, SAFETY_SETTINGS
from .personality_model import PersonalityModel
from .growth_analyzer import GrowthAnalyzer
from .content_analyzer import ContentAnalyzer

class ResponseGenerator:
    def __init__(self):
        self.personality = PersonalityModel()
        self.growth_analyzer = GrowthAnalyzer()
        self.content_analyzer = ContentAnalyzer()
        
    async def generate_response(
        self,
        content: Dict,
        platform: str,
        max_retries: int = 3
    ) -> Optional[str]:
        """Generate a personality-aligned response to content"""
        
        # Get current personal context
        current_state = await self.growth_analyzer.get_current_state()
        recent_insights = await self.growth_analyzer.get_recent_insights()
        
        # Analyze content
        content_analysis = await self.content_analyzer.analyze(content)
        
        # Generate response attempts
        for _ in range(max_retries):
            response = await self._create_response(
                content_analysis,
                platform,
                current_state,
                recent_insights
            )
            
            if await self._validate_response(response, content, platform):
                return response
                
        logging.warning("Failed to generate valid response after max retries")
        return None
        
    async def _create_response(
        self,
        content_analysis: Dict,
        platform: str,
        current_state: Dict,
        recent_insights: Dict
    ) -> str:
        """Create a response based on content and personal context"""
        
        # Get response components
        personal_angle = await self._get_personal_angle(
            content_analysis,
            current_state,
            recent_insights
        )
        
        value_add = await self._get_value_addition(
            content_analysis,
            platform
        )
        
        engagement_hook = await self._create_engagement_hook(
            content_analysis,
            platform
        )
        
        # Combine components based on platform and content type
        response = await self._format_response(
            personal_angle,
            value_add,
            engagement_hook,
            platform
        )
        
        return response
        
    async def _get_personal_angle(
        self,
        content_analysis: Dict,
        current_state: Dict,
        recent_insights: Dict
    ) -> str:
        """Generate a personal perspective on the content"""
        
        # Find relevant personal experiences
        relevant_experiences = await self.personality.find_relevant_experiences(
            content_analysis['topics'],
            current_state,
            recent_insights
        )
        
        # Select most appropriate experience
        if relevant_experiences:
            chosen_experience = await self.personality.select_best_experience(
                relevant_experiences,
                content_analysis
            )
            
            # Create personal narrative
            return await self.personality.create_personal_narrative(
                chosen_experience,
                content_analysis['tone']
            )
            
        # If no direct experience, generate perspective
        return await self.personality.generate_perspective(
            content_analysis,
            current_state
        )
        
    async def _get_value_addition(self, content_analysis: Dict, platform: str) -> str:
        """Generate valuable insights or information to add"""
        
        # Determine appropriate value type
        if content_analysis['type'] == 'technical':
            return await self._generate_technical_insight(content_analysis)
        elif content_analysis['type'] == 'spiritual':
            return await self._generate_spiritual_insight(content_analysis)
        else:
            return await self._generate_general_insight(content_analysis, platform)
            
    async def _create_engagement_hook(
        self,
        content_analysis: Dict,
        platform: str
    ) -> str:
        """Create a hook to encourage further engagement"""
        
        # Generate appropriate hook based on platform and content
        if platform == 'twitter':
            return await self._create_twitter_hook(content_analysis)
        elif platform == 'linkedin':
            return await self._create_linkedin_hook(content_analysis)
        else:
            return await self._create_general_hook(content_analysis)
            
    async def _format_response(
        self,
        personal_angle: str,
        value_add: str,
        engagement_hook: str,
        platform: str
    ) -> str:
        """Format the response appropriately for the platform"""
        
        # Get platform-specific formatting
        format_template = await self._get_platform_template(platform)
        
        # Apply personality style
        style = await self.personality.get_communication_style(platform)
        
        # Combine components
        response = format_template.format(
            personal=personal_angle,
            value=value_add,
            hook=engagement_hook
        )
        
        # Apply style modifications
        response = await self.personality.apply_style(response, style)
        
        return response
        
    async def _validate_response(
        self,
        response: str,
        original_content: Dict,
        platform: str
    ) -> bool:
        """Validate the response meets all requirements"""
        
        # Check safety requirements
        if not await self._check_safety(response):
            return False
            
        # Verify personality alignment
        if not await self.personality.verify_alignment(response):
            return False
            
        # Check platform appropriateness
        if not await self._check_platform_fit(response, platform):
            return False
            
        # Verify value addition
        if not await self._verify_value_add(response, original_content):
            return False
            
        return True
        
    async def _check_safety(self, response: str) -> bool:
        """Check if response meets safety requirements"""
        
        # Check sentiment
        sentiment_score = await self.content_analyzer.analyze_sentiment(response)
        if sentiment_score < SAFETY_SETTINGS['content_filters']['sentiment_threshold']:
            return False
            
        # Check controversy
        controversy_score = await self.content_analyzer.analyze_controversy(response)
        if controversy_score > SAFETY_SETTINGS['content_filters']['controversy_threshold']:
            return False
            
        # Check privacy
        if await self._contains_sensitive_info(response):
            return False
            
        return True
        
    async def _contains_sensitive_info(self, text: str) -> bool:
        """Check if text contains sensitive information"""
        sensitive_patterns = [
            # Add patterns for sensitive information
        ]
        
        return any(pattern in text.lower() for pattern in sensitive_patterns)
        
    async def _get_platform_template(self, platform: str) -> str:
        """Get response template for specific platform"""
        templates = {
            'twitter': "{personal} {value} {hook}",
            'linkedin': "Based on my experience: {personal}\n\nKey insight: {value}\n\n{hook}",
            'reddit': "{personal}\n\n{value}\n\n{hook}",
            'instagram': "✨ {personal}\n\n💡 {value}\n\n🤝 {hook}"
        }
        
        return templates.get(platform, "{personal} {value} {hook}")
        
    async def _verify_value_add(self, response: str, original_content: Dict) -> bool:
        """Verify response adds meaningful value"""
        # Implement value addition verification
        return True  # Placeholder 