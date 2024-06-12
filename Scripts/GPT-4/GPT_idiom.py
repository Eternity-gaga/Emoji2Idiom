# from openai import OpenAI
import base64
import requests

api_key="API-KEY"


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')


image_path = "file_path"
example_image_path_1 = "example_file_path"


base64_image = encode_image(image_path)

base64_example_image_1 = encode_image(example_image_path_1)



headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }

payload_1 = {
      "model": "gpt-4o",  # or GPT-4-turbo
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What is the Chinese idiom represented by the emojis in this image? Output format: 'The idiom is...'."
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
              }
            },
             {
              "type": "text",
              "text": "Here are some examples about the emoji images and the corresponding idioms. Emojis come first, and follows the corresponding idiom."
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_example_image_1}"
              }
            },
             {
              "type": "text",
              "text": "The idiom is <ground truth>."
            }
          ]
        }
      ],
      "max_tokens": 300
    }

response_1 = requests.post("openai_api", headers=headers, json=payload_1)

print(response_1.json())

