

# **Telegram Public Channel Scraper**

This project demonstrates how to fetch and save the last 100 messages from a Telegram channel, including metadata, into a JSON file. It is designed as a starting point for private channel scraping.

---

## **Features**
- Fetches the latest 100 messages from a Telegram channel.
- Saves messages, metadata (message ID, sender, date, etc.), and user interactions into a JSON file.
- Handles public channels by default but can be extended to private channels (requires access).
- Built using the Telethon library.

---

## **Requirements**
- Python 3.8 or later
- A Telegram account with access to the target channel
- Virtual environment support (recommended)

---

## **Setup**

### 1. **Clone the Repository**
```bash
git clone https://github.com/anatoli-derese/telegram-channel-scraper.git
cd telegram-channel-scraper
```

### 2. **Set Up a Virtual Environment**
Create and activate a virtual environment for the project:
```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
```

### 3. **Install Dependencies**
Install required Python libraries:
```bash
pip install -r requirements.txt
```

### 4. **Configure API Keys**
Create a `.env` file in the root directory and add the following:
```env
API_ID=your_api_id
API_HASH=your_api_hash
CHANNEL_USERNAME=target_channel_username
```

- Replace `your_api_id` and `your_api_hash` with your Telegram API credentials.
- Replace `target_channel_username` with the username of the Telegram channel (e.g., `@example_channel`).

### 5. **Run the Script**
Execute the script to fetch the last 100 messages:
```bash
python3 main.py
```

---

## **Output**
- The messages and metadata are saved in a file named `telegram_messages.json` in the project directory.
- Sample JSON format:
  ```json
  [
      {
          "message_id": 12345,
          "date": "2024-12-01T12:34:56",
          "text": "Hello, world!",
          "sender_id": 67890,
          "reply_to_msg_id": null,
          "views": 100,
          "forwards": 5
      }
  ]
  ```

---


## **Error Handling**
- **FloodWaitError**: The script will notify you if rate limits are reached and suggest waiting.
- **ChannelPrivateError**: Ensure you have access to the private channel.
- **UsernameNotOccupiedError**: Verify the channel username in `.env`.

---

## **Next Steps**
This script is a proof of concept. It can be expanded to:
- Support scraping private channels at scale.
- Implement advanced filtering for specific content types (e.g., media, links).
- Add logging and error recovery for long-running tasks.



## **Contact**
For questions or customization requests, feel free to contact me (Anatoli).
derese.anatoli@gmail.com