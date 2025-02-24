from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "word",
        "default": "cat",
        "placeholder": "cat",
        "tooltip": "Insert the word to pluralize here",
    },
    {
        "type": "int",
        "name": "count",
        "default": 2,
        "placeholder": 2,
        "tooltip": "Insert the number associated to the word to pluralize",
    },
]

output = {
        "name": "pluralized_text",
        "type": "str",
        "example": "cats"
    }

TaskRouter(router=router, input=inputs, output=output, default_model="inflect")
