from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "text",
        "default": "i would like to find a flight from charlotte to las vegas that makes a stop in st. louis",
        "placeholder": "i would like to find a flight from charlotte to las vegas that makes a stop in st. louis",
        "tooltip": "Insert the text to extract intent and slot from",
    }
]

output = {
        "name": "analyzed_text",
        "type": "list",
        "example": "analyzed_text"
    }


#TaskRouter(router=router, input=inputs, output=output, default_model="jointBERT-bert-atis")
