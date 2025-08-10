from fastapi_backend.models_django import add_product
import random
from django.db.models import F
from random import shuffle

def recommend_similar_products(product_id: int):
    try:
        product = add_product.objects.get(id=product_id)
        print("Product Category:", product.product_category)  

        similar = (
            add_product.objects
            .filter(product_category=product.product_category)
            .exclude(id=product_id)
            .order_by('?')[:4]
        )

        if not similar.exists():
            print("No similar products found. Falling back to random.")
            similar = add_product.objects.exclude(id=product_id).order_by('?')[:4]

        return [
            {
                "id": p.id,
                "name": p.product_name,
                "price": p.product_offer_price if p.product_offer_price else p.product_price,
                "original_price": p.product_price,
                "image_url": p.product_image.url,
                "size": p.product_size,
            }
            for p in similar
        ]
    except add_product.DoesNotExist:
        return []
    
def recommend_best_offer_products():
    all_products = add_product.objects.filter(product_offer__gte=15)

    if not all_products.exists():
        return {"recommendations": []}

    selected_products = random.sample(list(all_products), min(12, all_products.count()))

    recommendations = [
        {
            "id": p.id,
            "name": p.product_name,
            "price": p.product_offer_price,
            "original_price": p.product_price,
            "offer_percent": int(((p.product_price - p.product_offer_price) / p.product_price) * 100),
            "image_url": p.product_image.url,
            "size": p.product_size,
            "offer": p.product_offer
        }
        for p in selected_products
    ]

    return {"recommendations": recommendations}