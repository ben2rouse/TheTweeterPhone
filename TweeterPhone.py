from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather
import os
import tweepy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Twitter API credentials (loaded from environment variables)
TWITTER_BEARER_TOKEN = os.environ.get('TWITTER_BEARER_TOKEN')
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

# Set your 6-digit code here
SECRET_CODE = os.environ.get('TWITTER_SECRET_CODE', '123456')

def get_twitter_client():
    return tweepy.Client(
        bearer_token=TWITTER_BEARER_TOKEN,
        consumer_key=TWITTER_CONSUMER_KEY,
        consumer_secret=TWITTER_CONSUMER_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    )

@app.route('/voice', methods=['POST'])
def voice():
    resp = VoiceResponse()
    gather = Gather(num_digits=6, action='/verify', method='POST', timeout=10)
    gather.say('Please enter your 6 digit code.')
    resp.append(gather)
    resp.say('We did not receive any input. Goodbye!')
    return Response(str(resp), mimetype='text/xml')

@app.route('/verify', methods=['POST'])
def verify():
    digits = request.form.get('Digits')
    resp = VoiceResponse()
    
    if digits == SECRET_CODE:
        resp.say('Code accepted.')
        resp.play('https://ben2rouse.pythonanywhere.com/static/mysite/applause.mp3')
        resp.say('Please say your tweet after the tone.')
        resp.play('https://ben2rouse.pythonanywhere.com/static/mysite/applause.mp3')
        
        gather = Gather(input='speech', action='/tweet', method='POST', timeout=5)
        resp.append(gather)  # No children inside <Gather>; Twilio starts listening here
        resp.say('We did not receive any speech. Goodbye!')
    else:
        resp.say('Invalid code. Goodbye!')

    return Response(str(resp), mimetype='text/xml')

@app.route('/tweet', methods=['POST'])
def tweet():
    speech = request.form.get('SpeechResult')
    resp = VoiceResponse()
    if speech:
        try:
            client = get_twitter_client()
            client.create_tweet(text=speech)
            resp.say('Your tweet has been posted. Goodbye!')
        except Exception as e:
            error_message = f'There was an error posting your tweet: {str(e)}. Goodbye!'
            resp.say(error_message)
            # Also log the error for debugging
            import traceback
            with open('/tmp/tweet_error.log', 'a') as f:
                f.write(traceback.format_exc())

    else:
        resp.say('No speech detected. Goodbye!')
    return Response(str(resp), mimetype='text/xml')

@app.route('/testtweet', methods=['GET'])
def test_tweet():
    text = request.args.get('text', 'This is a test tweet from the browser!')
    try:
        client = get_twitter_client()
        client.create_tweet(text=text)
        return f"Tweet posted: {text}"
    except Exception as e:
        import traceback
        with open('/tmp/tweet_error.log', 'a') as f:
            f.write(traceback.format_exc())
        return f"Error posting tweet: {str(e)}"
