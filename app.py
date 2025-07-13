from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json
import random
import uvicorn

app = FastAPI()

#this is a comment
# Sample function templates

with open("content.html", "r", encoding= "utf-8") as f:
    HTML_CONTENT = f.read()
    
FUNCTION_TEMPLATES = [
    {
        "name": "add_numbers",
        "inputs": [{"name": "a", "type": "int"}, {"name": "b", "type": "int"}],
        "outputs": [{"name": "result", "type": "int"}],
        "description": "Add two integers"
    },
    {
        "name": "to_string", 
        "inputs": [{"name": "value", "type": "int"}],
        "outputs": [{"name": "text", "type": "str"}],
        "description": "Convert integer to string"
    },
    {
        "name": "get_length",
        "inputs": [{"name": "text", "type": "str"}],
        "outputs": [{"name": "length", "type": "int"}],
        "description": "Get string length"
    },
    {
        "name": "concatenate",
        "inputs": [{"name": "a", "type": "str"}, {"name": "b", "type": "str"}],
        "outputs": [{"name": "result", "type": "str"}],
        "description": "Concatenate two strings"
    },
    {
        "name": "multiply",
        "inputs": [{"name": "a", "type": "int"}, {"name": "b", "type": "int"}],
        "outputs": [{"name": "result", "type": "int"}],
        "description": "Multiply two integers"
    },
    {
        "name": "split_string",
        "inputs": [{"name": "text", "type": "str"}, {"name": "delimiter", "type": "str"}],
        "outputs": [{"name": "parts", "type": "list"}],
        "description": "Split string by delimiter"
    },
    {
        "name": "filter_positive",
        "inputs": [{"name": "numbers", "type": "list"}],
        "outputs": [{"name": "positive", "type": "list"}],
        "description": "Filter positive numbers"
    },
    {
        "name": "format_text",
        "inputs": [{"name": "template", "type": "str"}, {"name": "value", "type": "int"}],
        "outputs": [{"name": "formatted", "type": "str"}],
        "description": "Format text with value"
    }
]

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