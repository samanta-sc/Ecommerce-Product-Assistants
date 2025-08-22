from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run

from dotenv import load_dotenv
from ecommbot.retrieval_generation import generation
from ecommbot.ingest import ingestdata

# Initialize FastAPI application
app = FastAPI()

load_dotenv()

# Mount the 'static' directory for serving static files (like CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 template engine for rendering HTML templates
templates = Jinja2Templates(directory='templates')

# Allow all origins for Cross-Origin Resource Sharing (CORS)
origins = ["*"]

# Configure middleware to handle CORS, allowing requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vstore=ingestdata("done")
chain=generation(vstore)

# Route to render the main page with the form
@app.get("/", tags=["authentication"])
async def index(request: Request):
    """
    Renders the main HTML form page for vehicle data input.
    """
    return templates.TemplateResponse(
            "chat.html",{"request": request, "context": "Rendering"})

# Route to handle form submission and make predictions
@app.post("/get")
async def chat(msg: str = Form(...)):
    """
    Handles the chat requests.
    It takes a message from the form, invokes the generation chain,
    and returns the result.
    """

    input_text = msg
    print(f"Received message: {input_text}")
    try:
        # Invoke the generation chain with the user's input
        result = chain.invoke(input_text)
        print("Response : ", result)
        return str(result)
    except Exception as e:
        print(f"Error invoking chain: {e}")
        return "An error occurred while processing your request."

# Main entry point to start the FastAPI server
if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=5000)
