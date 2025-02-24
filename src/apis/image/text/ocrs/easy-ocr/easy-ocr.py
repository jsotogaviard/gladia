import easyocr


def predict(image: bytes, source_language: str) -> [str]:
    """
    Call the EasyOcr package and return the text detected in the image by the ocr

    :param image: image to provide to the ocr
    :param source_language: language of the text to be searched
    :return: characters found in the image
    """

    reader = easyocr.Reader([source_language], gpu=True)
    text = reader.readtext(image, detail=False)

    return text
