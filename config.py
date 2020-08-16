from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')

load_dotenv(dotenv_path)

FIREBASE_URL= str(getenv("FIREBASE_URL"))
SECERET_KEY = str(getenv("SECERET_KEY "))
FIREBASE_EMAIL = str(getenv("EMAIL"))
FIREBASE_PASSWORD = str(getenv("PASSWORD"))
TIME_ZONE = "Asia/Bangkok"