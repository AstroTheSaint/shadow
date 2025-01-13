"""
AI Shadow Dashboard
Monitors system activities, engagement opportunities, and growth insights
"""

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import asyncio
from typing import Dict, List
import json
from datetime import datetime, timedelta

from ..social_integration.content_monitor import ContentMonitor
from ..personality.numerology_analyzer import NumerologyAnalyzer
from ..growth.tracker import GrowthTracker

app = FastAPI(title="AI Shadow Dashboard")

# Initialize components
content_monitor = ContentMonitor()
numerology = NumerologyAnalyzer()
growth_tracker = GrowthTracker()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve dashboard HTML"""
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>AI Shadow Dashboard</title>
            <link rel="stylesheet" href="/static/styles.css">
            <script src="/static/dashboard.js"></script>
        </head>
        <body>
            <div class="dashboard">
                <div class="header">
                    <h1>AI Shadow Dashboard</h1>
                    <div class="current-state"></div>
                </div>
                
                <div class="main-content">
                    <div class="engagement-opportunities">
                        <h2>Viral Opportunities</h2>
                        <div id="opportunities-list"></div>
                    </div>
                    
                    <div class="growth-metrics">
                        <h2>Growth Tracking</h2>
                        <div id="growth-charts"></div>
                    </div>
                    
                    <div class="personality-insights">
                        <h2>Personality Analysis</h2>
                        <div id="numerology-insights"></div>
                    </div>
                </div>
                
                <div class="activity-feed">
                    <h2>Recent Activities</h2>
                    <div id="activity-list"></div>
                </div>
            </div>
        </body>
    </html>
    """

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket connection for real-time updates"""
    await websocket.accept()
    
    try:
        while True:
            # Send real-time updates
            await asyncio.gather(
                send_engagement_opportunities(websocket),
                send_growth_updates(websocket),
                send_activity_updates(websocket)
            )
            await asyncio.sleep(5)  # Update every 5 seconds
    except:
        await websocket.close()

@app.get("/api/opportunities")
async def get_opportunities() -> List[Dict]:
    """Get current viral engagement opportunities"""
    opportunities = await content_monitor.get_viral_opportunities()
    
    return [{
        'platform': 'twitter',
        'content': opp['tweet']['text'],
        'engagement_ratio': opp['engagement_ratio'],
        'category': opp['category'],
        'url': f"https://twitter.com/i/web/status/{opp['tweet']['id']}"
    } for opp in opportunities]

@app.get("/api/growth/current")
async def get_current_growth() -> Dict:
    """Get current growth metrics"""
    return await growth_tracker.generate_growth_report('7d')

@app.get("/api/growth/trends")
async def get_growth_trends(timeframe: str = '30d') -> Dict:
    """Get growth trends"""
    return await growth_tracker.analyze_growth_trends(timeframe)

@app.get("/api/personality/numerology")
async def get_numerology() -> Dict:
    """Get numerological insights"""
    return numerology.analyze_full_profile(
        name="Johnathan Michael Rapp",
        birth_date=datetime(1997, 8, 15, 23, 47)
    )

@app.get("/api/activity/recent")
async def get_recent_activity() -> List[Dict]:
    """Get recent system activity"""
    # Implement activity tracking
    return []

async def send_engagement_opportunities(websocket: WebSocket):
    """Send real-time engagement opportunities"""
    opportunities = await get_opportunities()
    await websocket.send_json({
        'type': 'opportunities',
        'data': opportunities
    })

async def send_growth_updates(websocket: WebSocket):
    """Send real-time growth updates"""
    growth_data = await get_current_growth()
    await websocket.send_json({
        'type': 'growth',
        'data': growth_data
    })

async def send_activity_updates(websocket: WebSocket):
    """Send real-time activity updates"""
    activities = await get_recent_activity()
    await websocket.send_json({
        'type': 'activity',
        'data': activities
    })

# Additional API endpoints for specific functionality
@app.get("/api/search/viral")
async def search_viral_content(
    min_ratio: float = 2.0,
    category: str = None
) -> List[Dict]:
    """Search for viral content with specific criteria"""
    opportunities = await content_monitor.get_viral_opportunities(min_ratio)
    
    if category:
        opportunities = [
            opp for opp in opportunities
            if opp['category'] == category
        ]
    
    return opportunities

@app.get("/api/growth/dimension/{dimension}")
async def get_dimension_details(dimension: str) -> Dict:
    """Get detailed analysis of a specific growth dimension"""
    trends = await growth_tracker.analyze_growth_trends('30d')
    return trends.get(dimension, {})

@app.get("/api/personality/current-state")
async def get_current_state() -> Dict:
    """Get current personality state and insights"""
    # Implement current state analysis
    return {} 