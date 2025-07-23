from fastapi import FastAPI
from fastapi_backend.product_recommend import recommend_similar_products

app = FastAPI()

@app.get("/recommend/product/{product_id}")
def get_recommendations(product_id: int):
    data = recommend_similar_products(product_id)
    return {"recommendations": data}