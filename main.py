from dotenv import load_dotenv
from datetime import datetime
import tweepy
import os
import emoji
import schedule
import random

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_KEY = os.getenv('ACCESS_KEY')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

try:
	api.verify_credentials()
	print("Authentication OK")
except:
	print("Error during authentication")

EMOJIS = [
	':thumbs_up:', ':waving_hand:', ':raised_hand:', ':grinning_face:', ':grinning_face_with_big_eyes:',
	':smiling_face_with_sunglasses:',
	':grinning_face_with_smiling_eyes:', ':beaming_face_with_smiling_eyes:', ':grinning_squinting_face:',
	':slightly_smiling_face:', ':upside-down_face:',
	':winking_face:', ':smiling_face_with_smiling_eyes:', ':face_with_tongue:', ':winking_face_with_tongue:',
	':zany_face:', ':squinting_face_with_tongue:',
	':smiling_face_with_open_hands:', ':face_with_medical_mask:', ':cowboy_hat_face:', ':nerd_face:', ':robot:',
	':waving_hand:', ':raised_back_of_hand:',
	':hand_with_fingers_splayed:', ':raised_hand:', ':vulcan_salute:', ':victory_hand:', ':love-you_gesture:',
	':sign_of_the_horns:', ':call_me_hand:',
	':raised_fist:', ':handshake:', ':desktop_computer:'
]

LANGUAGE = ['#HTML', '#css', '#JavaScript', '#C++', '#C', '#Python', '#PHP', '#Java', '#Dart', '#Kotlin']


def make_random_tweet() -> None:
	tweet = emoji.emojize(
		"Hello World! " +
		datetime.now().strftime("%H:%M:%S %d/%m/%Y") +
		" " + random.choice(EMOJIS) +
		" " + random.choice(LANGUAGE)
	)

	api.update_status(status=tweet)


def main():
	schedule.every().hour.at(":00").do(make_random_tweet)

	while True:
		schedule.run_pending()


if __name__ == '__main__':
	main()
