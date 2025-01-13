class Dashboard {
    constructor() {
        this.ws = null;
        this.charts = {};
        this.filters = {
            timeframe: 'day',
            platform: 'all',
            category: 'all'
        };
        this.parallaxElements = [];
        this.lastScrollY = window.scrollY;
        
        this.initializeWebSocket();
        this.setupEventListeners();
        this.initializeCharts();
        this.initializeParallax();
        this.initializeIntersectionObserver();
    }

    initializeWebSocket() {
        this.ws = new WebSocket(`ws://${window.location.host}/ws`);
        
        this.ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.handleUpdate(data);
        };

        this.ws.onclose = () => {
            console.log('WebSocket connection closed. Reconnecting...');
            setTimeout(() => this.initializeWebSocket(), 1000);
        };
    }

    initializeParallax() {
        this.parallaxElements = [
            ...document.querySelectorAll('.metric-card'),
            ...document.querySelectorAll('.opportunity-card'),
            ...document.querySelectorAll('.activity-item')
        ];

        window.addEventListener('scroll', () => {
            requestAnimationFrame(() => this.handleParallax());
        });

        window.addEventListener('mousemove', (e) => {
            requestAnimationFrame(() => this.handleMouseParallax(e));
        });
    }

    handleParallax() {
        const scrolled = window.scrollY;
        const delta = scrolled - this.lastScrollY;
        
        this.parallaxElements.forEach((el) => {
            const speed = 0.1;
            const yPos = (scrolled * speed) * (this.parallaxElements.indexOf(el) % 3 + 1);
            el.style.transform = `translateY(${yPos}px) scale(${1 - Math.abs(delta) * 0.001})`;
        });
        
        this.lastScrollY = scrolled;
    }

    handleMouseParallax(e) {
        const { clientX, clientY } = e;
        const centerX = window.innerWidth / 2;
        const centerY = window.innerHeight / 2;
        
        this.parallaxElements.forEach((el) => {
            const rect = el.getBoundingClientRect();
            const elCenterX = rect.left + rect.width / 2;
            const elCenterY = rect.top + rect.height / 2;
            
            const deltaX = (clientX - centerX) * 0.01;
            const deltaY = (clientY - centerY) * 0.01;
            
            el.style.transform = `translate(${deltaX}px, ${deltaY}px)`;
        });
    }

    initializeIntersectionObserver() {
        const options = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    if (entry.target.classList.contains('metric-card')) {
                        this.animateNumber(entry.target);
                    }
                }
            });
        }, options);

        document.querySelectorAll('.metric-card, .opportunity-card, .activity-item').forEach(el => {
            observer.observe(el);
        });
    }

    animateNumber(element) {
        const numberElement = element.querySelector('.score');
        if (!numberElement) return;

        const finalNumber = parseFloat(numberElement.textContent);
        if (isNaN(finalNumber)) return;

        let currentNumber = 0;
        const duration = 1000;
        const steps = 60;
        const increment = finalNumber / steps;

        const updateNumber = () => {
            currentNumber += increment;
            if (currentNumber > finalNumber) currentNumber = finalNumber;
            numberElement.textContent = currentNumber.toFixed(2);
            
            if (currentNumber < finalNumber) {
                requestAnimationFrame(updateNumber);
            }
        };

        requestAnimationFrame(updateNumber);
    }

    setupEventListeners() {
        document.querySelector('.timeframe-select').addEventListener('change', (e) => {
            this.filters.timeframe = e.target.value;
            this.refreshData();
            this.animateRefreshButton();
        });

        document.querySelector('.platform-filter').addEventListener('change', (e) => {
            this.filters.platform = e.target.value;
            this.refreshOpportunities();
            this.animateRefreshButton();
        });

        document.querySelector('.category-filter').addEventListener('change', (e) => {
            this.filters.category = e.target.value;
            this.refreshOpportunities();
            this.animateRefreshButton();
        });

        document.querySelector('.refresh-btn').addEventListener('click', () => {
            this.refreshData();
            this.animateRefreshButton();
        });

        // Add hover effects
        document.querySelectorAll('.metric-card, .opportunity-card').forEach(card => {
            card.addEventListener('mouseenter', () => {
                this.createParticles(card);
            });
        });
    }

    createParticles(element) {
        const particles = document.createElement('div');
        particles.className = 'particles';
        
        for (let i = 0; i < 10; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.setProperty('--x', `${Math.random() * 100}%`);
            particle.style.setProperty('--y', `${Math.random() * 100}%`);
            particles.appendChild(particle);
        }
        
        element.appendChild(particles);
        setTimeout(() => particles.remove(), 1000);
    }

    initializeCharts() {
        const ctx = document.getElementById('growth-charts').getContext('2d');
        
        const gradientFill = ctx.createLinearGradient(0, 0, 0, 400);
        gradientFill.addColorStop(0, 'rgba(110, 86, 207, 0.4)');
        gradientFill.addColorStop(1, 'rgba(110, 86, 207, 0)');
        
        this.charts.growth = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Overall Growth',
                    data: [],
                    borderColor: '#6E56CF',
                    backgroundColor: gradientFill,
                    fill: true,
                    tension: 0.4,
                    pointBackgroundColor: '#6E56CF',
                    pointBorderColor: '#fff',
                    pointHoverRadius: 8,
                    pointHoverBackgroundColor: '#6E56CF',
                    pointHoverBorderColor: '#fff',
                    pointHoverBorderWidth: 4
                }, {
                    label: 'Spiritual Evolution',
                    data: [],
                    borderColor: '#3ECF8E',
                    backgroundColor: 'rgba(62, 207, 142, 0.1)',
                    fill: true,
                    tension: 0.4,
                    pointBackgroundColor: '#3ECF8E',
                    pointBorderColor: '#fff',
                    pointHoverRadius: 8,
                    pointHoverBackgroundColor: '#3ECF8E',
                    pointHoverBorderColor: '#fff',
                    pointHoverBorderWidth: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 2000,
                    easing: 'easeInOutQuart'
                },
                interaction: {
                    mode: 'nearest',
                    axis: 'x',
                    intersect: false
                },
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            color: 'rgba(255, 255, 255, 0.9)',
                            font: {
                                family: 'Inter',
                                weight: '500'
                            },
                            padding: 20,
                            usePointStyle: true,
                            pointStyle: 'circle'
                        }
                    },
                    tooltip: {
                        backgroundColor: 'rgba(0, 0, 0, 0.8)',
                        titleFont: {
                            family: 'Inter',
                            size: 14,
                            weight: '600'
                        },
                        bodyFont: {
                            family: 'Inter',
                            size: 13
                        },
                        padding: 12,
                        cornerRadius: 8,
                        caretSize: 6
                    }
                },
                scales: {
                    x: {
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)',
                            drawBorder: false
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.6)',
                            font: {
                                family: 'Inter'
                            }
                        }
                    },
                    y: {
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)',
                            drawBorder: false
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.6)',
                            font: {
                                family: 'Inter'
                            }
                        }
                    }
                }
            }
        });
    }

    handleUpdate(data) {
        switch(data.type) {
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
        const grid = document.getElementById('opportunities-grid');
        grid.innerHTML = '';
        
        opportunities.forEach((opp, index) => {
            if (this.matchesFilters(opp)) {
                const card = this.createOpportunityCard(opp);
                card.style.animationDelay = `${index * 0.1}s`;
                grid.appendChild(card);
            }
        });
    }

    createOpportunityCard(opp) {
        const card = document.createElement('div');
        card.className = 'opportunity-card';
        card.innerHTML = `
            <div class="platform-badge ${opp.platform}">${opp.platform}</div>
            <h3>${opp.content}</h3>
            <div class="engagement-ratio">
                <span class="label">Engagement Ratio</span>
                <span class="value">${opp.engagement_ratio.toFixed(2)}x</span>
            </div>
            <div class="category-tag">${opp.category}</div>
        `;

        // Add hover effect
        card.addEventListener('mouseenter', () => {
            this.createParticles(card);
        });

        return card;
    }

    updateGrowthMetrics(data) {
        // Update summary cards with animation
        document.querySelectorAll('.metric-card').forEach(card => {
            const metric = card.querySelector('h3').textContent.toLowerCase();
            if (data.dimension_analysis[metric]) {
                const score = data.dimension_analysis[metric].score;
                this.animateNumber(card, score);
                card.querySelector('.trend').textContent = data.dimension_analysis[metric].trend;
            }
        });

        // Update chart with animation
        this.charts.growth.data.labels = data.dimension_analysis.spiritual.history.map(h => h.date);
        this.charts.growth.data.datasets[0].data = data.dimension_analysis.spiritual.history.map(h => h.score);
        this.charts.growth.update('show');

        // Update recommendations with fade effect
        const recList = document.getElementById('growth-recommendations');
        recList.style.opacity = '0';
        setTimeout(() => {
            recList.innerHTML = data.recommendations.map(rec => `<li>${rec}</li>`).join('');
            recList.style.opacity = '1';
        }, 300);
    }

    updateActivityFeed(activities) {
        const feed = document.getElementById('activity-list');
        activities.forEach((activity, index) => {
            const item = document.createElement('div');
            item.className = 'activity-item';
            item.style.animationDelay = `${index * 0.1}s`;
            item.innerHTML = `
                <div class="timestamp">${this.formatTimestamp(activity.timestamp)}</div>
                <div class="description">${activity.description}</div>
                <div class="type-badge ${activity.type}">${activity.type}</div>
            `;
            feed.insertBefore(item, feed.firstChild);
        });
    }

    matchesFilters(opp) {
        return (this.filters.platform === 'all' || opp.platform === this.filters.platform) &&
               (this.filters.category === 'all' || opp.category === this.filters.category);
    }

    formatTimestamp(timestamp) {
        const date = new Date(timestamp);
        return date.toLocaleString();
    }

    animateRefreshButton() {
        const btn = document.querySelector('.refresh-btn');
        btn.classList.add('spinning');
        setTimeout(() => btn.classList.remove('spinning'), 1000);
    }

    refreshData() {
        this.ws.send(JSON.stringify({
            action: 'refresh',
            filters: this.filters
        }));
    }

    refreshOpportunities() {
        this.ws.send(JSON.stringify({
            action: 'refresh_opportunities',
            filters: this.filters
        }));
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.dashboard = new Dashboard();
}); 