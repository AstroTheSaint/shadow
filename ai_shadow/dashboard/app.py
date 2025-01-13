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

app = FastAPI(title="AI Shadow Dashboard")

# Initialize components
content_monitor = ContentMonitor()

# Mount static files
app.mount("/static", StaticFiles(directory="ai_shadow/dashboard/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve dashboard HTML"""
    with open("ai_shadow/dashboard/templates/dashboard.html", "r") as f:
        return f.read()

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
        'content': 'Example viral content',
        'engagement_ratio': 2.5,
        'category': 'technology',
        'url': 'https://twitter.com/example'
    }]  # Placeholder data

@app.get("/api/growth/current")
async def get_current_growth() -> Dict:
    """Get current growth metrics"""
    return {
        'summary': {
            'overall_growth': 0.75,
            'top_dimension': 'spiritual',
            'recent_milestone': 'Completed meditation streak'
        },
        'dimension_analysis': {
            'spiritual': {
                'score': 0.8,
                'trend': 'increasing',
                'history': [{'date': '2024-01-14', 'score': 0.8}]
            },
            'intellectual': {
                'score': 0.7,
                'trend': 'stable',
                'history': [{'date': '2024-01-14', 'score': 0.7}]
            }
        },
        'recommendations': [
            'Increase meditation duration',
            'Document more insights',
            'Engage with spiritual content'
        ]
    }

@app.get("/api/growth/trends")
async def get_growth_trends(timeframe: str = '30d') -> Dict:
    """Get growth trends"""
    return await get_current_growth()  # Placeholder

@app.get("/api/activity/recent")
async def get_recent_activity() -> List[Dict]:
    """Get recent system activity"""
    return [{
        'id': 1,
        'timestamp': datetime.now().isoformat(),
        'type': 'meditation',
        'description': 'Completed 20-minute session'
    }]  # Placeholder data

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