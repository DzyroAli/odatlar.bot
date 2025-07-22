from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from calendar_utils import generate_calendar

app = FastAPI()

class DateInput(BaseModel):
    dates: List[str]  # формат: "14-03-2025"

@app.post("/calendar")
async def create_calendar(input_data: DateInput):
    try:
        response = generate_calendar(input_data.dates)
        return {"message": response}
    except Exception as e:
        return {"error": str(e)}
