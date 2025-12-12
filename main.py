from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from datetime import datetime

app = FastAPI()

templates = Jinja2Templates(directory="templates")

messages = []

@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "messages": messages}
    )

@app.post("/send", response_class=HTMLResponse)
async def send_msg(request: Request, text: str = Form(...), name: str = Form(...)):
    if text.strip() and name.strip():
        messages.append({"name": name, "message": text, "time": datetime.now().strftime("%H:%M")})
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "messages": messages}
    )

@app.post("/clear", response_class=HTMLResponse)
async def clear_chat(request: Request):
    messages.clear()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "messages": messages}
    )
