from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from router import route_request

app = FastAPI(title="LangChain Router Microservice")

class UserRequest(BaseModel):
    user_id: str
    message: str

class RouterResponse(BaseModel):
    model_name: str
    response: str

@app.post("/route", response_model=RouterResponse)
async def route_message(request: UserRequest):
    try:
        model_name, response = await route_request(request.user_id, request.message)
        return RouterResponse(model_name=model_name, response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
