from fastapi import FastAPI, File, Form, UploadFile
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter, Request
from pydantic import BaseModel
from typing import Annotated, Optional
import requests
import uuid
import base64
import json
import math

from utils import somatotype_data_list, SomatotypeData
from fastapi.middleware.cors import CORSMiddleware

# from sqlalchemy.orm import Session
import os
app = FastAPI()

origins = [
    "http://localhost:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ORGANIZATION_KEY = os.environ.get('ORGANIZATION_KEY')
API_KEY = os.environ.get('API_KEY') # USE IN HEADER "Authorization: "
BODYGRAM_POST_SCAN_API = f"https://platform.bodygram.com/api/orgs/{ORGANIZATION_KEY}/scans"

BODY_PARTS_NAME = ['forearmGirthR', 'kneeGirthR', 'upperArmGirthR', 'calfGirthR']

# example:{
            #     "name": "calfGirthR",
            #     "unit": "mm",
            #     "value": 391
            # },
class RequestData(BaseModel):
    name: str
    height: int
    weight: int
    age: int
    gender: str
    triceps_skinfold: int
    subscapular_skinfold: int
    supraspinale_skinfold: int


class ResponseData(BaseModel):
    name: str
    height: int
    weight: int
    age: int
    gender: str
    skeletal_muscle_mass: int
    body_fat_percentage: float
    mesomorphy: float
    endomorphy: float
    ectomorphy: float
    bmi: float
    reference_somatotype_data: list[SomatotypeData]

    


# @app.post('/post_user_data')
# async def upload(userData: RequestData, 
#                  front_image: UploadFile = File(...),
#                  right_image: UploadFile = File(...),
#                  ) -> ResponseData:

@app.post('/post_user_data')
async def upload(name: str,
                height: int,
                weight: int,
                age: int,
                gender: str,
                triceps_skinfold: int,
                subscapular_skinfold: int,
                supraspinale_skinfold: int,
                front_image: UploadFile = File(...),
                right_image: UploadFile = File(...),
                 ):
    

    userData = RequestData(
        name=name, 
        height=height, 
        weight=weight, 
        age=age, 
        gender=gender, 
        triceps_skinfold=triceps_skinfold,
        subscapular_skinfold=subscapular_skinfold,
        supraspinale_skinfold=supraspinale_skinfold 
        )
    
    front_image_base64 = base64.b64encode(front_image.file.read()).decode('utf-8')
    right_image_base64 = base64.b64encode(right_image.file.read()).decode('utf-8')
    

    # front_image_base64 = "base64.b64encode(front_image.file.read()).decode('utf-8')"
    # right_image_base64 = "base64.b64encode(right_image.file.read()).decode('utf-8')"
    

    scanID = str(uuid.uuid4())
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json",
    }

    print(headers, "header", BODYGRAM_POST_SCAN_API)

    # Define the request data as a JSON string
    data = {
        "customScanId": scanID,
        "photoScan": {
            "age": userData.age,
            "weight": userData.weight,
            "height": userData.height,
            "gender": userData.gender,
            "frontPhoto": front_image_base64,  # Replace with your actual base64-encoded front photo
            "rightPhoto": right_image_base64,  # Replace with your actual base64-encoded right photo
        }
    }

    response = requests.post(BODYGRAM_POST_SCAN_API, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
    else:
        print("API Request Failed with Status Code:", response.status_code)

    measurements = response_data['entry']['measurements']
    """
    "bodyComposition": {
        "skeletalMuscleMass": 35250,
        "bodyFatPercentage": 25.45
        },
    """
    skeletalMuscleMass = response_data['entry']['bodyComposition']['skeletalMuscleMass']
    bodyFatPercentage = response_data['entry']['bodyComposition']['bodyFatPercentage']

    BODY_PARTS_VALUE = {key: None for key in BODY_PARTS_NAME}
    for measurement in measurements:
        if measurement['name'] in BODY_PARTS_NAME:
            BODY_PARTS_VALUE[measurement['name']] = measurement['value']
    

    user_endomorphy = get_endomorphy(userData)
    user_mesomorphy = get_mesomorphy(userData, BODY_PARTS_VALUE)
    user_ectomorphy = get_ectomorphy(userData)
    user_bmi = get_bmi(userData)

    
    
    response_data = ResponseData(
        name = userData.name,
        height = userData.height,
        weight = userData.weight,
        age = userData.age,
        gender = userData.gender,
        skeletal_muscle_mass =  skeletalMuscleMass,
        body_fat_percentage = bodyFatPercentage,
        mesomorphy = user_mesomorphy,
        endomorphy = user_endomorphy,
        ectomorphy = user_ectomorphy,
        bmi = user_bmi,
        reference_somatotype_data = somatotype_data_list
    )

    return response_data

"""
X: (sum of triceps, subscapular and supraspinale skinfolds 
multiplied by (170.18/height in cm); 
"""
def get_endomorphy(user: RequestData):
    X = (user.triceps_skinfold + user.subscapular_skinfold + user.supraspinale_skinfold)* (170.18/(user.height/10))
    return -0.7182 + 0.1451*X - 0.00068*(X**2)+ 0.0000014*(X**3)

"""
HB: Humeurus Breadth (cm)
FB: Femur Breadth (cm)
AG: upper arm grith (cm) 
CG: max calf grith (cm)
SH, standing height (cm); 
"""
def get_mesomorphy(user: RequestData, BODY_PARTS_VALUE):
    HB = ( BODY_PARTS_VALUE['forearmGirthR'] /10 ) / math.pi
    FB = ( BODY_PARTS_VALUE['kneeGirthR'] / 10 ) / math.pi
    AG = BODY_PARTS_VALUE['upperArmGirthR'] / 10
    CG = BODY_PARTS_VALUE['calfGirthR'] / 10
    SH = user.height / 10
    return 0.858*HB + 0.601*FB + 0.188*AG + 0.161*CG - 0.131*SH + 4.5 

"""
HWR, height in cm over cuberoot of weight. 
"""
def get_ectomorphy(user: RequestData,):

    PI = (user.height/10) / ((user.weight/1000)**(1/3))
    if PI > 40.74:
        return 0.732*PI - 28.58
    elif  39.65 <= PI <= 40.74:
        return (0.463*PI) - 17.615
    else:
        return 0.5
        
def get_bmi(user: RequestData):
    return round((user.weight / user.height**2),2)