from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

inputs = [
    {
        "type": "image",
        "name": "image",
        "default": "Image to colorize",
        "placeholder": "Image to colorize",
        "tooltip": "Image to colorize"
    }
]

output = {
        "name": "colorized_image",
        "type": "image",
        "example": "image"
    }

router = APIRouter()

TaskRouter(
    router=router, input=inputs, output=output, default_model="deoldify-stable"
)
