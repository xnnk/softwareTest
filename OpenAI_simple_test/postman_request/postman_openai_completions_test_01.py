import unittest

import requests
import json


class TestCompletions(unittest.TestCase):


  def test_completions(self):
    url = "https://api.openai.com/v1/chat/completions"


    payload = json.dumps({
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "user",
          "content": "Hello! This is software test!"
        }
      ]
    })
    headers = {
      'Authorization': 'Bearer sk-your-key',
      'Content-Type': 'application/json',
      'Cookie': ''
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
