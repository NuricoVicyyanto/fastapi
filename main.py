from fastapi import FastAPI

app = FastAPI(title="FastAPI", description="FastAPI Demo", version="0.1.0")


@app.get("/items/{item_id}", tags=["items"], description="Get an item")
async def read_item(item_id: int):
    return {
        "item_id": item_id,
        "title": "Item title"
    }
