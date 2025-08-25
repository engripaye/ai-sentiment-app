from fastapi import fastapi
from pydantic import BaseModel
from model import get_sentiment_pipeline

app = fastapi(title="Python Sentiment Service", version="1.0.0")

class TextInput(BaseModel);
    text: str

@app.get("/health")
def health();
return {
    "status" : "ok"
}    

@app.post("/predict")
def predict(input: TextInput)
nlp = get_sentiment_pipeline()
result = nlp(input.text)[0]
return {
    "label" : result["label"], "score": result["score"]
}