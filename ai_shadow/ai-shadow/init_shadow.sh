#!/bin/bash

# AI Shadow System Initialization Script

echo "Initializing AI Shadow System..."

# Create directory structure
echo "Creating directory structure..."
mkdir -p ai-shadow/{learning/{journal_insights,growth_patterns,relationship_models,value_system},memory/{experiences,reflections,decisions,emotions},integration/{content_feeds,response_templates,interaction_logs,feedback_loop},consciousness/{current_state,value_alignment,personality_core,growth_direction}}

# Set up Python virtual environment
echo "Setting up Python environment..."
python3 -m venv .venv
source .venv/bin/activate

# Install required packages
echo "Installing dependencies..."
pip install -r requirements.txt

# Initialize database
echo "Setting up databases..."
python setup_databases.py

# Configure file watchers
echo "Configuring repository monitors..."
python setup_monitors.py

# Initial data processing
echo "Processing existing repository data..."
python initial_processing.py

# Start services
echo "Starting core services..."
docker-compose up -d

echo "AI Shadow initialization complete!"
echo "Run 'python setup_learning.py' to configure learning parameters" 