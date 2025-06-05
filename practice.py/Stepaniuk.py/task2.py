from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import requests
from typing import List
import secrets

app = FastAPI(title="Cat Facts Premium API", 
              description="API for getting interesting facts about cats ")
SECRET_PASSWORD = "meow123"
CAT_API_URL = "https://cat-fact.herokuapp.com/facts/random"
PREMIUM_CAT_API = "https://api.thecatapi.com/v1/images/search"

security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_password = secrets.compare_digest(credentials.password, SECRET_PASSWORD)
    if not correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized access. Password required!",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/free-fact", summary="Free cat fact")
async def free_cat_fact():
    """Get one random cat fact (no auth needed)"""
    response = requests.get(CAT_API_URL)
    return {
        "fact": response.json()["text"],
        "premium": False,
        "hint": "Use /premium-fact with password 'meow123' for more features!"
    }

@app.get("/premium-fact", summary="Premium fact + cat photo")
async def premium_cat_fact(username: str = Depends(authenticate)):
    """Get fact + random cat photo (requires auth)"""
    fact_response = requests.get(CAT_API_URL)
    photo_response = requests.get(PREMIUM_CAT_API)
    
    return {
        "fact": fact_response.json()["text"],
        "image_url": photo_response.json()[0]["url"],
        "premium": True,
        "message": f"Thank you, {username}, for being our premium user!"
    }

@app.get("/multi-facts", summary="Multiple facts")
async def multiple_cat_facts(
    count: int = 5, 
    username: str = Depends(authenticate)
):
    """Get several facts at once (max 10)"""
    if count > 10:
        count = 10
    
    facts = []
    for _ in range(count):
        response = requests.get(CAT_API_URL)
        facts.append(response.json()["text"])
    
    return {
        "count": count,
        "facts": facts,
        "bonus": "Cats are awesome!"
    }

@app.get("/cat-image", summary="Random cat image")
async def random_cat_image(
    size: str = "small",
    username: str = Depends(authenticate)
):
    """Get random cat image with parameters"""
    params = {"size": size, "mime_types": "jpg,png"}
    response = requests.get(PREMIUM_CAT_API, params=params)
    
    return {
        "image_url": response.json()[0]["url"],
        "size": size,
        "fun_comment": "This cat is specially for you!"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
