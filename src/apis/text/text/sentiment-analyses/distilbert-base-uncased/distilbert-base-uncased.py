import json

from happytransformer import HappyTextClassification


def predict(text: str) -> str:
    """
    For a given text, predict if it's POSITIVE or NEGATIVE

    :param text: text to analyze.
    :return: JSON formatted str containing the label (POSITIVE/NEGATIVE) with it score
    """

    happy_tc = HappyTextClassification("DISTILBERT", "distilbert-base-uncased", num_labels=2)
    result = happy_tc.classify_text(text)

    return json.dumps({
        "label": "POSITIVE" if result.label == "LABEL_0" else "NEGATIVE",
        "score": result.score,
    })
