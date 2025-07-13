from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json
import random
import uvicorn
from function_templates import FUNCTION_TEMPLATES

app = FastAPI()

#this is a comment
# Sample function templates

with open("content.html", "r", encoding= "utf-8") as f:
    HTML_CONTENT = f.read()

@app.get("/", response_class=HTMLResponse)
async def get_app():
    return HTML_CONTENT

@app.post("/api/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    message = data.get("message", "")
    
    # Generate 2-3 random functions based on the message
    num_functions = random.randint(2, 3)
    selected_functions = random.sample(FUNCTION_TEMPLATES, num_functions)
    
    return {
        "functions": selected_functions,
        "response": f"Here are some functions for '{message}'"
    }

@app.post("/api/export")
async def export_graph(request: Request):
    data = await request.json()
    # In a real app, you'd save this to a database
    return {"status": "exported", "graph": data}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)