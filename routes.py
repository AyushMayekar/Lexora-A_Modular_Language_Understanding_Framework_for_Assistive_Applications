# backend/lexora_api.py
from fastapi import FastAPI
from pydantic import BaseModel
from functions import perform_ner, perform_sentiment, perform_summary, perform_keywords

app = FastAPI(title="Lexora API", description="Language Intelligence Engine API", version="1.0")

class TextRequest(BaseModel):
    text: str

@app.post("/ner")
def ner_api(req: TextRequest):
    return {"entities": perform_ner(req.text)}

@app.post("/sentiment")
def sentiment_api(req: TextRequest):
    return {"sentiment": perform_sentiment(req.text)}

@app.post("/summary")
def summary_api(req: TextRequest):
    return {"summary": perform_summary(req.text)}

@app.post("/keywords")
def keywords_api(req: TextRequest):
    return {"keywords": perform_keywords(req.text)}
