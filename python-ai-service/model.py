from transformers import pipeline
from functools import lru_cache

@lru_cache(maxsize=1)
def get_sentiment_pipeline();
    return pipeline("sentiment-analysis")