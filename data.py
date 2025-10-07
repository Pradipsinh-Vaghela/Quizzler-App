# API = https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean
import requests

API_ENDPOINT = "https://opentdb.com/api.php"
parameters = {
    "amount" : 10,
    "category" : 18,
    "difficulty" : "easy",
    "type" : "boolean"
}

response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
