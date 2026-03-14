import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
MAILERLITE_API_KEY = os.getenv('MAILERLITE_API_KEY')
API_URL = 'https://connect.mailerlite.com/api/campaigns'
HEADERS = {
    'Authorization': f'Bearer {MAILERLITE_API_KEY}',
    'Content-Type': 'application/json'
}

def list_sent_campaigns():
    response = requests.get(API_URL, headers=HEADERS)
    response.raise_for_status()
    campaigns = response.json().get('data', [])
    sent_campaigns = [c for c in campaigns if c.get('status') == 'sent']
    if not sent_campaigns:
        print('No sent campaigns found.')
        return
    for c in sent_campaigns:
        print(f"ID: {c['id']}")
        print(f"Name: {c['name']}")
        print(f"Created at: {c['created_at']}")
        print(f"Subject: {c['emails'][0]['subject'] if c.get('emails') else 'N/A'}")
        print('-' * 40)

if __name__ == '__main__':
    list_sent_campaigns()
