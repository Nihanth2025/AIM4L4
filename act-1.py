import requests
from config import HF_API_KEY

def classify_text(text):
    API_URI="https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
    headers={"Authorization":f"Bearer{HF_API_KEY}"}
    payload={"inputs":text}

    response=requests.post(API_URI, headers=headers, json=payload)
    return response.json()

if __name__=="__main__":
    sample_text="I love using Hugging Face APIs!"
    result=classify_text(sample_text)
    print(result)