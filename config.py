import os

from dotenv import load_dotenv


load_dotenv()


TOKEN_TG = os.getenv("TOKEN_TG")
TOKEN_OWM = os.getenv("TOKEN_OWM")