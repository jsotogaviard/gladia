import json

from happytransformer import HappyQuestionAnswering


def predict(context: str, question: str) -> str:
    """
    Using the given `context`, answer the provided `question`.

    :param context: context to use to answer the question
    :param question: question to answer
    :return: JSON formatted str containing both the answer and the confidence score.
    """

    happy_qa = HappyQuestionAnswering("DISTILBERT", "distilbert-base-cased-distilled-squad")
    result = happy_qa.answer_question(context, question)

    return json.dumps({'answer': result[0].answer, 'score': result[0].score})
