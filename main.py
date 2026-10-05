from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI()

# 1. Your Root Route: Matches exactly "/"
@app.get("/")
def home():
    return {"message": "hi brooo"}

# 2. Your Dynamic Route: Matches "/vishnu", "/vivek", or any other name
@app.get("/{name}")
def greet_user(name: str):
    return {"message": f"hi {name}"}


# ==========================================
# 🎯 PRACTICE ROUTES FOR YOU TO TRY
# ==========================================

# Practice 1: Query Parameters (Matches "/search?query=python&limit=5")
@app.get("/search/")
def search_items(query: str, limit: int = 10):
    return {"message": f"Searching for '{query}' with a limit of {limit} items"}

# Practice 2: Type Validation (Matches "/square/5", fails on "/square/abc")
@app.get("/square/{number}")
def calculate_square(number: int):
    return {"result": number * number}

# Practice 3: Combining Path & Query Params (Matches "/user/42?status=active")
@app.get("/user/{user_id}")
def get_user_profile(user_id: int, status: str = "offline"):
    return {"user_id": user_id, "current_status": status}


if __name__ == "__main__":
    # Change "main:app" to match your actual file name if it isn't main.py
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
