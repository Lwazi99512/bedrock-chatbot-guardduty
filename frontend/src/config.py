import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# AWS Configuration
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# Alerting (Slack, Email, etc.)
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
