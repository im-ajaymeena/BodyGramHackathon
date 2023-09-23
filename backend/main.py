from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
from typing import Annotated, Optional
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter, Request
# from sqlalchemy.orm import Session

app = FastAPI()

class UserData(BaseModel):

    name: str
    height: int
    weight: int
    age: int
    gender: str


@app.post('/post_user_data')
async def upload(user: UserData = Depends(), 
                 front_image: UploadFile = File(...),
                 right_image: UploadFile = File(...),
                 ):
  
  print(f"user name is: {user.name}")
  print(f"user age is: {user.age}")
  print(f"user gender is: {user.gender}")
  print(f"user height is: {user.height}")


  return {"message": "Upload"}
