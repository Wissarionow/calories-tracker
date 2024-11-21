
from openai import OpenAI
import base64
import instructor
from pydantic import BaseModel
from dotenv import dotenv_values


class Meal(BaseModel):
    name: str
    calories: int
    protein: int
    carbs: int
    fats: int
    fiber: int

def openAI_response(image):
    
    env = dotenv_values(".env")
    openai_client = OpenAI(api_key=env["OPENAI_API_KEY"])
    instructor_openai_client = instructor.from_openai(openai_client)
    
    meal = instructor_openai_client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=Meal,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Wypełnij makroskładniki i kalorie posiłku oraz podaj jego nazwę.", 
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": prepare_image_for_open_ai(image),
                            "detail": "high"
                        },
                    },
                ],
            },
        ],
    )
    return meal

def prepare_image_for_open_ai(image_path):
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    return f"data:image/png;base64,{image_data}"

#
#To do: 
#-Identify user weight goals in db
#-Pass 2nd argument 
def fill_meal(image):
    list = []
    for i in range(4):
        list[i]=openAI_response(image)
    print(list)
     

