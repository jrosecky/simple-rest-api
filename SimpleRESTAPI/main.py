from fastapi import FastAPI
from models.item import Item
from fastapi import HTTPException

# crates the API app itself
app = FastAPI(title="My API")

# "database" (temporary in-memory storage)
items = []

# root endpoint
@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def add_item(item: Item):
    item_data = item.model_dump()
    items.append(item_data)
    return {"message": "Item added", "item": item_data}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if 0 <= item_id < len(items):
        deleted = items.pop(item_id)
        return {"message": "Item deleted", "item": deleted}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if 0 <= item_id < len(items):
        updated_item = item.model_dump()
        items[item_id] = update_item
        return{"message": "Item updated", "item": updated_item}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
