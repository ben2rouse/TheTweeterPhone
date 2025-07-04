# Spy Phone Twitter Bot

A Flask-based phone bot that allows users to post tweets via phone calls using Twilio and Twitter API integration. This project is designed to be hosted on PythonAnywhere with static file hosting for audio assets.

## Features

- **Phone Authentication**: Secure 6-digit code verification
- **Voice-to-Tweet**: Convert speech to Twitter posts
- **Audio Feedback**: Plays sound effects for user feedback
- **Web Testing**: Browser-based tweet testing endpoint
- **PythonAnywhere Integration**: Optimized for PythonAnywhere hosting with static file support

## Prerequisites

- Python 3.7 or higher
- Twitter Developer Account with API credentials
- Twilio Account for phone integration
- PythonAnywhere account (recommended for hosting)
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
   
   The project uses audio files hosted on PythonAnywhere's static file system. Upload your audio files to your PythonAnywhere static files directory:
   - `applause.mp3` - Played after successful code verification and as a "tone" before recording
   - `keys.mp3` - Background sound effects (if needed)
   
   **PythonAnywhere Static Files Setup:**
   1. Log into your PythonAnywhere account
   2. Go to the "Files" tab
   3. Navigate to `/home/yourusername/mysite/static/mysite/`
   4. Upload your MP3 files to this directory
   5. The files will be accessible at: `https://yourusername.pythonanywhere.com/static/mysite/filename.mp3`

3. **Audio File URLs**
   
   The current configuration uses PythonAnywhere static file URLs:
   ```
   https://ben2rouse.pythonanywhere.com/static/mysite/applause.mp3
   ```
   
   Update these URLs in the code to match your PythonAnywhere username and file locations.

## Usage

### Running the Application

#### Local Development
1. **Start the Flask server locally**
   ```bash
   python TweeterPhone.py
   ```

2. **For local production testing**
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```

#### PythonAnywhere Deployment

1. **Upload your files to PythonAnywhere**
   - Upload `TweeterPhone.py` to `/home/yourusername/mysite/`
   - Upload `.env` file to `/home/yourusername/mysite/`
   - Upload audio files to `/home/yourusername/mysite/static/mysite/`

2. **Configure your Web App**
   - Go to the "Web" tab in PythonAnywhere
   - Set your source code directory to `/home/yourusername/mysite/`
   - Set your WSGI configuration file to point to your Flask app
   - Reload your web app

3. **Update Audio File URLs**
   - Replace `ben2rouse` in the audio URLs with your PythonAnywhere username
   - Example: `https://yourusername.pythonanywhere.com/static/mysite/applause.mp3`

4. **Configure Twilio Webhooks**
   - Set your Twilio webhook URL to: `https://yourusername.pythonanywhere.com/voice`

### API Endpoints

- **`/voice`** (POST) - Main phone entry point, prompts for 6-digit code
- **`/verify`** (POST) - Verifies the entered code and prompts for speech
- **`/tweet`** (POST) - Processes speech and posts to Twitter
- **`/testtweet`** (GET) - Test endpoint for posting tweets via browser

### Testing

**Browser Testing:**
```
# Local testing
http://localhost:5000/testtweet?text=Your test tweet here

# PythonAnywhere testing
https://yourusername.pythonanywhere.com/testtweet?text=Your test tweet here
```

**Phone Testing:**
1. Configure Twilio webhook to point to your PythonAnywhere URL
2. Call your Twilio phone number
3. Enter your 6-digit code when prompted
4. Speak your tweet after the tone
5. The tweet will be posted to your Twitter account

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
├── requirements.txt    # Python dependencies
├── applause.mp3        # Success sound effect (upload to PythonAnywhere static)
├── keys.mp3            # Background sound effect (upload to PythonAnywhere static)
├── background.png      # Project background image
└── image.png           # Project image
```

## PythonAnywhere Hosting

This project is optimized for PythonAnywhere hosting:

1. **Static File Hosting**: Audio files are served through PythonAnywhere's static file system
2. **Easy Deployment**: Simple file upload and configuration
3. **HTTPS Support**: Secure connections for Twilio webhooks
4. **Persistent Storage**: Environment variables and logs are preserved

### PythonAnywhere Setup Steps:

1. **Create a new Web App** on PythonAnywhere
2. **Upload your project files** to `/home/yourusername/mysite/`
3. **Configure static files** in the Web tab:
   - URL: `/static/`
   - Directory: `/home/yourusername/mysite/static/`
4. **Update audio URLs** in your code to match your username
5. **Set up Twilio webhooks** to point to your PythonAnywhere domain

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
3. **Audio File Issues**: 
   - Verify file paths and hosting for audio files
   - Ensure MP3 files are uploaded to PythonAnywhere static directory
   - Check that audio URLs match your PythonAnywhere username
4. **Phone Integration**: Ensure Twilio webhooks are properly configured to your PythonAnywhere domain
5. **PythonAnywhere Issues**:
   - Check the error logs in the Web tab
   - Verify static file configuration
   - Ensure your web app is reloaded after changes

## Development

To modify the project:

1. **Add new endpoints** in `TweeterPhone.py`
2. **Update audio files** by replacing the MP3 files
3. **Modify speech processing** in the `/tweet` endpoint
4. **Add new authentication methods** in the `/verify` endpoint

## License

This project is for educational and personal use. Ensure compliance with Twitter's API terms of service and Twilio's usage policies.
