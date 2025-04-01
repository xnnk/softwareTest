import unittest
import requests
import json

class TestModels(unittest.TestCase):


  def test_show_models(self):
    url = "https://api.openai.com/v1/models"

    payload = {}
    headers = {
      'Authorization': 'Bearer sk-your-key',
      'Content-Type': 'application/json',
      'Cookie': ''
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)