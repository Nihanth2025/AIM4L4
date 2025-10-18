import requests

h_api= "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"
def a(text):
  url = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
  headers={"Authorization":f"Bearer {h_api}"}
  payload={"inputs":text}
  response=requests.post(url,headers=headers,json=payload)
  return response.json()
Sam_text="i am netural today "
result=a(Sam_text)
print(result)