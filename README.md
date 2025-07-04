# Spy Phone Twitter Bot

A Flask-based phone bot that allows users to post tweets via phone calls using Twilio and Twitter API integration.

## Features

- **Phone Authentication**: Secure 6-digit code verification
- **Voice-to-Tweet**: Convert speech to Twitter posts
- **Audio Feedback**: Plays sound effects for user feedback
- **Web Testing**: Browser-based tweet testing endpoint

## Prerequisites

- Python 3.7 or higher
- Twitter Developer Account with API credentials
- Twilio Account for phone integration
- Internet connection for API calls

## Installation

1. **Clone or download the project files**
   ```bash
   cd "/Users/benjaminrouse/Desktop/Spy Phone/Test Tweet"
   ```

2. **Install required Python packages**
   ```bash
   pip install flask twilio tweepy python-dotenv
   ```

   Or install from requirements file:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Environment Variables**
   
   The project uses a `.env` file to store sensitive credentials. Make sure your `.env` file contains:
   ```
   TWITTER_CONSUMER_KEY="your_consumer_key"
   TWITTER_CONSUMER_SECRET="your_consumer_secret"
   TWITTER_BEARER_TOKEN="your_bearer_token"
   TWITTER_ACCESS_TOKEN="your_access_token"
   TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
   TWITTER_SECRET_CODE="123456"
   ```

2. **Audio Files**
   
   Ensure the following audio files are accessible:
   - `applause.mp3` - Played after successful code verification
   - `keys.mp3` - Background sound effects

## Usage

### Running the Application

1. **Start the Flask server**
   ```bash
   python TweeterPhone.py
   ```

2. **For production deployment**
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```

### API Endpoints

- **`/voice`** (POST) - Main phone entry point, prompts for 6-digit code
- **`/verify`** (POST) - Verifies the entered code and prompts for speech
- **`/tweet`** (POST) - Processes speech and posts to Twitter
- **`/testtweet`** (GET) - Test endpoint for posting tweets via browser

### Testing

**Browser Testing:**
```
http://localhost:5000/testtweet?text=Your test tweet here
```

**Phone Testing:**
1. Call your Twilio phone number
2. Enter your 6-digit code when prompted
3. Speak your tweet after the tone
4. The tweet will be posted to your Twitter account

## Dependencies

```bash
pip install flask           # Web framework
pip install twilio          # Phone integration
pip install tweepy          # Twitter API client
pip install python-dotenv   # Environment variable loading
```

## Project Structure

```
Test Tweet/
├── TweeterPhone.py     # Main Flask application
├── .env                # Environment variables (keep secret!)
├── README.md           # This file
├── applause.mp3        # Success sound effect
├── keys.mp3            # Background sound effect
├── background.png      # Project background image
└── image.png           # Project image
```

## Security Notes

- **Never commit your `.env` file** to version control
- Keep your Twitter API credentials secure
- Use a strong 6-digit code for phone authentication
- Consider implementing rate limiting for production use

## Error Handling

The application includes comprehensive error handling:
- Invalid codes result in "Invalid code. Goodbye!"
- Twitter API errors are logged to `/tmp/tweet_error.log`
- Speech recognition failures are handled gracefully

## Troubleshooting

1. **Import Errors**: Ensure all required packages are installed
2. **Twitter API Errors**: Check your credentials in the `.env` file
3. **Audio File Issues**: Verify file paths and hosting for audio files
4. **Phone Integration**: Ensure Twilio webhooks are properly configured

## Development

To modify the project:

1. **Add new endpoints** in `TweeterPhone.py`
2. **Update audio files** by replacing the MP3 files
3. **Modify speech processing** in the `/tweet` endpoint
4. **Add new authentication methods** in the `/verify` endpoint

## License

This project is for educational and personal use. Ensure compliance with Twitter's API terms of service and Twilio's usage policies.
