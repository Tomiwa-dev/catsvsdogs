from fastapi import FastAPI, File, UploadFile, status, HTTPException
from app import predictor
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]  # domains that can interact with our api "*" all domains

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict", status_code=status.HTTP_202_ACCEPTED)
async def predict(image: UploadFile = File(...)):
    image = await image.read()
    result = predictor.makeprediction(image)
    return result
