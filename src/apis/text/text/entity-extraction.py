from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "input_string",
        "default": "Text to extract entities from",
        "placeholder": "Text to extract entities from",
        "tooltip": "Insert the text to extract entities from",
    }
]

output = {
        "name": "extracted_entities",
        "type": "list",
        "example": "extracted_entities"
    }


TaskRouter(router=router, input=inputs, output=output, default_model="dbmdz-bert-large-cased-finetuned-conll03-english")
