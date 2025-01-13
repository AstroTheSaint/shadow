"""
Social Media Integration Configuration
Combines personal growth insights with strategic social engagement
"""

# Platform Configurations
PLATFORMS = {
    'twitter': {
        'engagement_threshold': 1000,  # Minimum engagement for interaction
        'trending_window': '24h',      # Time window for trending content
        'response_delay': '30s',       # Delay between finding and responding
        'daily_interaction_limit': 20,  # Maximum daily interactions
        'content_categories': [
            'technology',
            'spirituality',
            'personal_growth',
            'entrepreneurship',
            'ai_innovation'
        ]
    },
    'linkedin': {
        'engagement_threshold': 500,
        'content_focus': [
            'business_innovation',
            'technology_trends',
            'education_innovation',
            'ai_development'
        ],
        'post_types': ['articles', 'thought_leadership', 'industry_insights']
    },
    'reddit': {
        'subreddits': [
            'technology',
            'spirituality',
            'meditation',
            'entrepreneurship',
            'artificialintelligence'
        ],
        'minimum_upvotes': 1000,
        'sort_by': 'rising'  # Catch posts early in their growth
    },
    'instagram': {
        'hashtag_categories': [
            'tech_innovation',
            'spiritual_growth',
            'digital_nomad',
            'entrepreneurlife',
            'mindfulness'
        ],
        'engagement_minimum': 5000,
        'content_types': ['posts', 'reels', 'stories']
    }
}

# Personal Growth Integration
GROWTH_INTEGRATION = {
    'journal_weight': 0.4,        # Weight of recent journal entries
    'growth_weight': 0.3,         # Weight of growth patterns
    'relationship_weight': 0.2,    # Weight of relationship insights
    'current_state_weight': 0.1,  # Weight of current state/location
    
    'recency_decay': {
        'hours_1': 1.0,
        'hours_24': 0.8,
        'days_7': 0.6,
        'days_30': 0.4
    }
}

# Content Alignment Scoring
ALIGNMENT_METRICS = {
    'personal_relevance': {
        'current_journey': 0.4,    # Alignment with current personal journey
        'growth_goals': 0.3,       # Alignment with growth objectives
        'value_system': 0.2,       # Alignment with core values
        'location_context': 0.1    # Relevance to current location/situation
    },
    
    'engagement_potential': {
        'trending_factor': 0.4,    # How trending the topic is
        'timing_factor': 0.3,      # Time of day/week optimization
        'audience_match': 0.2,     # Alignment with target audience
        'platform_fit': 0.1        # Suitability for specific platform
    }
}

# Response Generation
RESPONSE_GUIDELINES = {
    'style_elements': {
        'authenticity': 0.4,       # Maintain authentic voice
        'value_add': 0.3,          # Provide meaningful contribution
        'relatability': 0.2,       # Connect with others' experiences
        'uniqueness': 0.1          # Stand out from typical responses
    },
    
    'content_mix': {
        'personal_experience': 0.4, # Share relevant personal insights
        'spiritual_wisdom': 0.3,    # Incorporate spiritual perspective
        'technical_insight': 0.2,   # Add technical value when relevant
        'question_prompt': 0.1      # Encourage further discussion
    }
}

# Content Discovery
DISCOVERY_SETTINGS = {
    'monitoring_frequency': {
        'trending_topics': '15m',   # Check trending topics every 15 minutes
        'engagement_scan': '5m',    # Scan for high-engagement posts every 5 minutes
        'relevance_check': '1m'     # Check content relevance every minute
    },
    
    'feed_curation': {
        'personal_growth': {
            'sources': ['medium', 'substack', 'twitter', 'reddit'],
            'update_frequency': '1h',
            'relevance_threshold': 0.7
        },
        'tech_innovation': {
            'sources': ['github', 'twitter', 'linkedin', 'techcrunch'],
            'update_frequency': '2h',
            'relevance_threshold': 0.6
        },
        'spiritual_content': {
            'sources': ['instagram', 'youtube', 'reddit'],
            'update_frequency': '3h',
            'relevance_threshold': 0.8
        }
    }
}

# Safety and Ethics
SAFETY_SETTINGS = {
    'rate_limits': {
        'posts_per_hour': 5,
        'comments_per_hour': 10,
        'likes_per_hour': 20
    },
    
    'content_filters': {
        'sentiment_threshold': 0.7,     # Minimum positivity score
        'controversy_threshold': 0.3,    # Maximum controversy score
        'alignment_minimum': 0.8         # Minimum personal alignment score
    },
    
    'privacy_guards': {
        'personal_info_check': True,     # Check for personal info exposure
        'relationship_privacy': True,     # Protect relationship details
        'location_privacy': True         # Smart location sharing
    }
}

# Monitoring and Analytics
ANALYTICS_CONFIG = {
    'track_metrics': {
        'engagement_rate': True,
        'response_quality': True,
        'alignment_accuracy': True,
        'growth_integration': True
    },
    
    'reporting': {
        'daily_summary': True,
        'weekly_analysis': True,
        'monthly_insights': True,
        'growth_correlation': True
    }
} 