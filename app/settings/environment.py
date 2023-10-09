import os

from dotenv import load_dotenv

load_dotenv()

settings = {
    "app": {
        "CONTAINER_APP_NAME": os.getenv("CONTAINER_APP_NAME"),
        "APP_PORT": os.getenv("APP_PORT"),
    },
}
