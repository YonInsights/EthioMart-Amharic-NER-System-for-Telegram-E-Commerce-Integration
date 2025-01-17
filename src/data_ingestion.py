from telethon import TelegramClient
import json
import os

# My Telegram API credentials
API_ID = 29267451
API_HASH = '439870004d79b44bcaa1fa775ed82b6f'
SESSION_NAME = 'mydata_session'

# Directory to save raw data
OUTPUT_DIR = 'data/raw/'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Channel usernames
CHANNELS = ['@ZemenExpress', '@nevacomputer', '@meneshayeofficial', '@ethio_brand_collection', '@Leyueqa']

def fetch_messages():
    # Initialize Telegram client
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    
    # Start the client
    with client:
        for channel in CHANNELS:
            print(f"Fetching messages from {channel}...")
            messages = []
            
            async for message in client.iter_messages(channel, limit=100):  # Adjust limit as needed
                messages.append({
                    "id": message.id,
                    "text": message.text,
                    "date": str(message.date),
                    "sender": message.sender_id,
                    "media": str(message.media) if message.media else None
                })
            
            # Save messages to a JSON file
            output_file = os.path.join(OUTPUT_DIR, f"{channel.strip('@')}_messages.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(messages, f, ensure_ascii=False, indent=4)
            
            print(f"Saved messages from {channel} to {output_file}")

if __name__ == "__main__":
    fetch_messages()
