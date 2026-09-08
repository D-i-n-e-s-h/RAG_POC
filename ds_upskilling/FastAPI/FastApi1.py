from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Pydantic Model
class User(BaseModel):
    id: int
    name: str
    age: int
    email: str # Use EmailStr if you install pydantic[email] later

# In-memory database
users = []

# FIX: Added root route to eliminate the 404 error
@app.get("/")
def read_root():
    return {"status": "online", "message": "Welcome to the User Management API"}

@app.post("/users")
def create_user(user: User):
    for u in users:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User ID already exists")
    users.append(user)
    return {"message": "User created successfully", "user": user}

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

# OPTIMIZED: Changed from GET to PATCH and used dictionary update pattern
@app.patch("/users/{user_id}/name")
def update_user_name(user_id: int, user_name: str):
    for index, user in enumerate(users):
        if user.id == user_id:
            # Safely updates the field and maintains Pydantic validation
            stored_user_data = user.model_dump()
            stored_user_data["name"] = user_name
            users[index] = User(**stored_user_data)
            return {"message": "User Name Updated.", "user": users[index]}
            
    raise HTTPException(status_code=404, detail="User not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=63927, reload=True)