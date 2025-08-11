import requests
from os import environ as env
from dotenv import load_dotenv

class PluggyApi:
    def __init__(self) -> str:
        
        load_dotenv()
        self.client_id = env.get("PLUGGY_CLIENT_ID")
        self.client_secret = env.get("PLUGGY_CLIENT_SECRET")

   
    def __str__(self) -> None:
        return f"Client ID: {self.client_id}. Client Secret: {self.client_secret}"
        

    def _get_api_key(self) -> list[str]:
        url = "https://api.pluggy.ai/auth"

        payload = {"clientId": self.client_id, "clientSecret": self.client_secret}
        header = {"accept": "application/json", "content-type": "application/json"}
        
        response = requests.post(url, json=payload, headers=header)
        return response.json()
        

    def get_connect_token(self) -> list[str]:
        url = "https://api.pluggy.ai/auth"
        api_key = self._get_api_key()

        header = {"accept": "application/json", "content-type": "application/json", "X-API-KEY": api_key['apiKey']}

        try:
            response = requests.post(url, headers=header)
            return response.json()

        except Exception as e:
            return f"Error retriving Connect Token: {e}"

if __name__ == '__main__':
    context = PluggyApi()
    print(context.get_connect_token())
    