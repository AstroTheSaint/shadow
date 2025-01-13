// AI Shadow Dashboard Frontend

class Dashboard {
    constructor() {
        this.ws = null;
        this.charts = {};
        this.opportunities = [];
        this.activities = [];
        
        this.initializeWebSocket();
        this.setupEventListeners();
        this.initializeCharts();
    }
    
    initializeWebSocket() {
        this.ws = new WebSocket(`ws://${window.location.host}/ws`);
        
        this.ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.handleUpdate(data);
        };
        
        this.ws.onclose = () => {
            console.log('WebSocket connection closed');
            // Attempt to reconnect after 5 seconds
            setTimeout(() => this.initializeWebSocket(), 5000);
        };
    }
    
    setupEventListeners() {
        // Setup refresh buttons
        document.querySelectorAll('.refresh-btn').forEach(btn => {
            btn.addEventListener('click', () => this.refreshData());
        });
        
        // Setup timeframe selectors
        document.querySelectorAll('.timeframe-select').forEach(select => {
            select.addEventListener('change', (e) => {
                this.updateTimeframe(e.target.value);
            });
        });
    }
    
    initializeCharts() {
        // Initialize growth charts
        const growthCtx = document.getElementById('growth-charts');
        this.charts.growth = new Chart(growthCtx, {
            type: 'line',
            data: {
                labels: [],
                datasets: []
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 1
                    }
                }
            }
        });
    }
    
    handleUpdate(data) {
        switch (data.type) {
            case 'opportunities':
                this.updateOpportunities(data.data);
                break;
            case 'growth':
                this.updateGrowthMetrics(data.data);
                break;
            case 'activity':
                this.updateActivityFeed(data.data);
                break;
        }
    }
    
    updateOpportunities(opportunities) {
        const container = document.getElementById('opportunities-list');
        container.innerHTML = '';
        
        opportunities.forEach(opp => {
            const card = this.createOpportunityCard(opp);
            container.appendChild(card);
        });
    }
    
    createOpportunityCard(opportunity) {
        const card = document.createElement('div');
        card.className = 'opportunity-card';
        
        card.innerHTML = `
            <div class="card-header">
                <span class="platform">${opportunity.platform}</span>
                <span class="engagement">Engagement: ${opportunity.engagement_ratio.toFixed(2)}x</span>
            </div>
            <div class="card-content">
                <p>${opportunity.content}</p>
            </div>
            <div class="card-footer">
                <span class="category">${opportunity.category}</span>
                <a href="${opportunity.url}" target="_blank" class="view-btn">View</a>
            </div>
        `;
        
        return card;
    }
    
    updateGrowthMetrics(growth) {
        // Update charts
        this.updateGrowthCharts(growth);
        
        // Update summary metrics
        this.updateGrowthSummary(growth.summary);
        
        // Update recommendations
        this.updateRecommendations(growth.recommendations);
    }
    
    updateGrowthCharts(growth) {
        const dimensions = Object.keys(growth.dimension_analysis);
        const datasets = dimensions.map(dim => ({
            label: dim,
            data: growth.dimension_analysis[dim].history.map(h => h.score),
            fill: false,
            tension: 0.4
        }));
        
        this.charts.growth.data.datasets = datasets;
        this.charts.growth.update();
    }
    
    updateGrowthSummary(summary) {
        const container = document.querySelector('.growth-summary');
        if (!container) return;
        
        container.innerHTML = `
            <div class="summary-card">
                <h3>Overall Progress</h3>
                <div class="progress-indicators">
                    ${Object.entries(summary).map(([key, value]) => `
                        <div class="indicator">
                            <label>${key}</label>
                            <div class="value">${value}</div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }
    
    updateRecommendations(recommendations) {
        const container = document.querySelector('.recommendations');
        if (!container) return;
        
        container.innerHTML = `
            <h3>Growth Recommendations</h3>
            <ul>
                ${recommendations.map(rec => `
                    <li class="recommendation">
                        <span class="rec-text">${rec}</span>
                    </li>
                `).join('')}
            </ul>
        `;
    }
    
    updateActivityFeed(activities) {
        const container = document.getElementById('activity-list');
        
        // Prepend new activities
        activities.forEach(activity => {
            if (!this.activities.find(a => a.id === activity.id)) {
                const element = this.createActivityElement(activity);
                container.insertBefore(element, container.firstChild);
                this.activities.unshift(activity);
            }
        });
        
        // Limit to latest 50 activities
        while (this.activities.length > 50) {
            this.activities.pop();
            if (container.lastChild) {
                container.removeChild(container.lastChild);
            }
        }
    }
    
    createActivityElement(activity) {
        const element = document.createElement('div');
        element.className = 'activity-item';
        
        element.innerHTML = `
            <div class="activity-time">${this.formatTime(activity.timestamp)}</div>
            <div class="activity-content">
                <span class="activity-type">${activity.type}</span>
                <span class="activity-description">${activity.description}</span>
            </div>
        `;
        
        return element;
    }
    
    formatTime(timestamp) {
        const date = new Date(timestamp);
        return date.toLocaleTimeString();
    }
    
    refreshData() {
        // Manually trigger data refresh
        fetch('/api/opportunities')
            .then(response => response.json())
            .then(data => this.updateOpportunities(data));
            
        fetch('/api/growth/current')
            .then(response => response.json())
            .then(data => this.updateGrowthMetrics(data));
            
        fetch('/api/activity/recent')
            .then(response => response.json())
            .then(data => this.updateActivityFeed(data));
    }
    
    updateTimeframe(timeframe) {
        fetch(`/api/growth/trends?timeframe=${timeframe}`)
            .then(response => response.json())
            .then(data => this.updateGrowthMetrics(data));
    }
}

// Initialize dashboard when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.dashboard = new Dashboard();
}); 