import torch
from transformers import AutoFeatureExtractor, AutoModelForAudioClassification


MODEL_NAME = "MIT/ast-finetuned-audioset-10-10-0.4593"


def load_model():
    """
    Load the pretrained Hugging Face audio classification model.
    """

    feature_extractor = AutoFeatureExtractor.from_pretrained(
        MODEL_NAME
    )

    model = AutoModelForAudioClassification.from_pretrained(
        MODEL_NAME
    )

    model.eval()

    return feature_extractor, model