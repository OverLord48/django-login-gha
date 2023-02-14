import requests
import json
from os import getenv
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

micro_signout_host = getenv("MICRO_OUT_HOST")
micro_signout_port = getenv("MICRO_OUT_PORT")
def logout_token(token):
    try:
        response = requests.post(f"http://{micro_signout_host}:{micro_signout_port}/logout", data={"token":token})
        return response.text
    except Exception as e:
        return {"error":e}
