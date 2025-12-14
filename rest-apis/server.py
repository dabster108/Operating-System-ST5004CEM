from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    result: str

@app.post('/api/uppercase', response_model=TextResponse)
def uppercase(request: TextRequest):
    result = request.text.upper()
    return TextResponse(result=result)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5002)