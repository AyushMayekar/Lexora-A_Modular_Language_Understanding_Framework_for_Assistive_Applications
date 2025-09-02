from transformers import pipeline

# Load pipelines once (not every call)
ner_pipeline = pipeline("ner", grouped_entities=True)
sentiment_pipeline = pipeline("sentiment-analysis")
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
keyword_pipeline = pipeline("feature-extraction")

def _sanitize(result):
    """Convert NumPy types to native Python types for JSON serialization."""
    if isinstance(result, list):
        return [_sanitize(r) for r in result]
    if isinstance(result, dict):
        return {k: _sanitize(v) for k, v in result.items()}
    if hasattr(result, "item"):  
        return result.item()
    return result

def perform_ner(text: str):
    return _sanitize(ner_pipeline(text))

def perform_sentiment(text: str):
    return _sanitize(sentiment_pipeline(text)[0])

def perform_summary(text: str):
    return summarizer_pipeline(text, max_length=60, min_length=20, do_sample=False)[0]['summary_text']

def perform_keywords(text: str):
    words = list(set(text.split()))
    return words[:10] 
