from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_backend.product_recommend import recommend_similar_products
from fastapi_backend.product_recommend import recommend_best_offer_products

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/recommend/product/{product_id}")
def get_recommendations(product_id: int):
    data = recommend_similar_products(product_id)
    return {"recommendations": data}

@app.get("/recommend/best-offers")
def recommend_best_offers():
    return recommend_best_offer_products()