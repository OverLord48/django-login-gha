import requests
import json

def logout_token(token):
    try:
        response = requests.post(f"http://127.0.0.1:8000/logout", data={"token":token})
        return response.text
    except Exception as e:
        return {"error":e}
