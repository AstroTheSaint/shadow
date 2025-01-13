"""
Growth Tracking System
Quantifies and monitors personal development across multiple dimensions
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json
import numpy as np
from collections import defaultdict

class GrowthTracker:
    def __init__(self):
        self.dimensions = {
            'spiritual': {
                'meditation_depth': {
                    'metric': 'minutes',
                    'weight': 0.3
                },
                'presence_quality': {
                    'metric': 'scale_1_10',
                    'weight': 0.4
                },
                'insight_frequency': {
                    'metric': 'count_per_day',
                    'weight': 0.3
                }
            },
            'intellectual': {
                'learning_depth': {
                    'metric': 'scale_1_10',
                    'weight': 0.4
                },
                'knowledge_integration': {
                    'metric': 'scale_1_10',
                    'weight': 0.3
                },
                'creative_output': {
                    'metric': 'count_per_day',
                    'weight': 0.3
                }
            },
            'emotional': {
                'awareness_level': {
                    'metric': 'scale_1_10',
                    'weight': 0.4
                },
                'regulation_quality': {
                    'metric': 'scale_1_10',
                    'weight': 0.3
                },
                'relationship_depth': {
                    'metric': 'scale_1_10',
                    'weight': 0.3
                }
            },
            'physical': {
                'energy_level': {
                    'metric': 'scale_1_10',
                    'weight': 0.3
                },
                'exercise_intensity': {
                    'metric': 'minutes',
                    'weight': 0.4
                },
                'sleep_quality': {
                    'metric': 'scale_1_10',
                    'weight': 0.3
                }
            },
            'social': {
                'connection_quality': {
                    'metric': 'scale_1_10',
                    'weight': 0.4
                },
                'impact_reach': {
                    'metric': 'count',
                    'weight': 0.3
                },
                'community_engagement': {
                    'metric': 'scale_1_10',
                    'weight': 0.3
                }
            }
        }
        
        self.history = defaultdict(list)
        self.insights = defaultdict(list)
        
    async def track_daily_metrics(self, date: datetime, metrics: Dict) -> Dict:
        """Track daily growth metrics across all dimensions"""
        
        processed_metrics = {}
        
        for dimension, aspects in self.dimensions.items():
            if dimension in metrics:
                dimension_score = self._calculate_dimension_score(
                    aspects,
                    metrics[dimension]
                )
                
                processed_metrics[dimension] = {
                    'score': dimension_score,
                    'details': metrics[dimension],
                    'insights': self._generate_insights(dimension, metrics[dimension])
                }
                
                self.history[dimension].append({
                    'date': date,
                    'score': dimension_score,
                    'metrics': metrics[dimension]
                })
                
        return processed_metrics
        
    async def analyze_growth_trends(self, timeframe: str = '30d') -> Dict:
        """Analyze growth trends across all dimensions"""
        
        end_date = datetime.now()
        start_date = self._get_start_date(end_date, timeframe)
        
        trends = {}
        for dimension in self.dimensions:
            dimension_data = [
                entry for entry in self.history[dimension]
                if start_date <= entry['date'] <= end_date
            ]
            
            if dimension_data:
                trends[dimension] = {
                    'overall_trend': self._calculate_trend(dimension_data),
                    'peak_performance': self._find_peak_performance(dimension_data),
                    'growth_rate': self._calculate_growth_rate(dimension_data),
                    'consistency': self._calculate_consistency(dimension_data),
                    'insights': self._analyze_dimension_patterns(dimension_data)
                }
                
        return trends
        
    async def generate_growth_report(self, timeframe: str = '30d') -> Dict:
        """Generate comprehensive growth report"""
        
        trends = await self.analyze_growth_trends(timeframe)
        
        return {
            'summary': self._generate_summary(trends),
            'dimension_analysis': trends,
            'recommendations': self._generate_recommendations(trends),
            'milestones': self._identify_milestones(trends),
            'areas_for_improvement': self._identify_growth_opportunities(trends)
        }
        
    async def track_milestone(self, milestone: Dict):
        """Track significant growth milestones"""
        
        dimension = milestone['dimension']
        self.insights[dimension].append({
            'date': datetime.now(),
            'type': 'milestone',
            'description': milestone['description'],
            'impact_score': milestone.get('impact_score', 0)
        })
        
    def _calculate_dimension_score(self, aspects: Dict, metrics: Dict) -> float:
        """Calculate weighted score for a dimension"""
        
        total_score = 0
        total_weight = 0
        
        for aspect, config in aspects.items():
            if aspect in metrics:
                normalized_value = self._normalize_metric(
                    metrics[aspect],
                    config['metric']
                )
                total_score += normalized_value * config['weight']
                total_weight += config['weight']
                
        return total_score / total_weight if total_weight > 0 else 0
        
    def _normalize_metric(self, value: float, metric_type: str) -> float:
        """Normalize metric to 0-1 scale"""
        
        if metric_type == 'scale_1_10':
            return value / 10
        elif metric_type == 'minutes':
            return min(value / 120, 1)  # Cap at 2 hours
        elif metric_type == 'count_per_day':
            return min(value / 10, 1)  # Cap at 10 instances
        elif metric_type == 'count':
            return min(value / 100, 1)  # Cap at 100
        
        return value
        
    def _calculate_trend(self, data: List[Dict]) -> Dict:
        """Calculate trend line for dimension data"""
        
        dates = [(entry['date'] - data[0]['date']).days for entry in data]
        scores = [entry['score'] for entry in data]
        
        if len(dates) > 1:
            slope, intercept = np.polyfit(dates, scores, 1)
            return {
                'direction': 'increasing' if slope > 0 else 'decreasing',
                'strength': abs(slope),
                'consistency': np.corrcoef(dates, scores)[0, 1]
            }
        
        return {'direction': 'neutral', 'strength': 0, 'consistency': 0}
        
    def _generate_insights(self, dimension: str, metrics: Dict) -> List[str]:
        """Generate insights based on metrics"""
        insights = []
        
        # Analyze patterns and generate insights
        return insights
        
    def _get_start_date(self, end_date: datetime, timeframe: str) -> datetime:
        """Calculate start date based on timeframe"""
        
        units = {
            'd': 'days',
            'w': 'weeks',
            'm': 'months',
            'y': 'years'
        }
        
        value = int(timeframe[:-1])
        unit = timeframe[-1]
        
        if unit in units:
            return end_date - timedelta(**{units[unit]: value})
            
        raise ValueError(f"Invalid timeframe format: {timeframe}")
        
    def _find_peak_performance(self, data: List[Dict]) -> Dict:
        """Find peak performance period"""
        if not data:
            return {}
            
        peak_entry = max(data, key=lambda x: x['score'])
        return {
            'date': peak_entry['date'],
            'score': peak_entry['score'],
            'metrics': peak_entry['metrics']
        }
        
    def _calculate_growth_rate(self, data: List[Dict]) -> float:
        """Calculate growth rate"""
        if len(data) < 2:
            return 0
            
        first_score = data[0]['score']
        last_score = data[-1]['score']
        days = (data[-1]['date'] - data[0]['date']).days
        
        return (last_score - first_score) / days if days > 0 else 0
        
    def _calculate_consistency(self, data: List[Dict]) -> float:
        """Calculate consistency of growth"""
        if len(data) < 2:
            return 1
            
        scores = [entry['score'] for entry in data]
        return 1 - np.std(scores) / np.mean(scores) if np.mean(scores) > 0 else 0
        
    def _analyze_dimension_patterns(self, data: List[Dict]) -> List[str]:
        """Analyze patterns within dimension data"""
        return []  # Placeholder
        
    def _generate_summary(self, trends: Dict) -> Dict:
        """Generate overall growth summary"""
        return {}  # Placeholder
        
    def _generate_recommendations(self, trends: Dict) -> List[str]:
        """Generate growth recommendations"""
        return []  # Placeholder
        
    def _identify_milestones(self, trends: Dict) -> List[Dict]:
        """Identify significant milestones"""
        return []  # Placeholder
        
    def _identify_growth_opportunities(self, trends: Dict) -> List[Dict]:
        """Identify areas for improvement"""
        return []  # Placeholder 