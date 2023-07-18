import os
from dotenv import load_dotenv


load_dotenv()


def parser(key):
    return os.getenv(key)

