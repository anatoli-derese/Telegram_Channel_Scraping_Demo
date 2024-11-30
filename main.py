import json
import os
from dotenv import load_dotenv
from telethon import TelegramClient, errors

load_dotenv()

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
channel_username = os.getenv('CHANNEL_USERNAME')
client = TelegramClient('session_name', api_id, api_hash)


async def fetch_messages():
    try:
        print(f"Resolving entity for: {channel_username}")
        channel = await client.get_entity(channel_username)
        messages_data = []

        print("Fetching messages...")
        async for message in client.iter_messages(channel, limit=100):
            messages_data.append({
                "message_id": message.id,
                "date": message.date.isoformat() if message.date else None,
                "text": message.text if message.text else "",
                "sender_id": message.sender_id,
                "reply_to_msg_id": message.reply_to_msg_id,
                "views": message.views,
                "forwards": message.forwards,
            })

        json_file_name = 'telegram_messages.json'
        with open(json_file_name, 'w', encoding='utf-8') as json_file:
            json.dump(messages_data, json_file, indent=4, ensure_ascii=False)
        print(f"Messages saved to '{json_file_name}'.")
    
    except errors.FloodWaitError as e:
        print(f"FloodWaitError: Need to wait {e.seconds} seconds before retrying.")
    except errors.ChannelPrivateError:
        print(f"Error: The channel '{channel_username}' is private. Access is restricted.")
    except errors.UsernameNotOccupiedError:
        print(f"Error: The username '{channel_username}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

async def main():
    await fetch_messages()

with client:
    client.loop.run_until_complete(main())
