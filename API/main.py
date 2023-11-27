from fastapi import FastAPI
import uvicorn

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
test_user_db = [{"user_id": "1"}, {"user_id": "2"}, {"user_id": "3"}]

@app.get("/")
def read_root():
    return fake_items_db 

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/me")
def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


