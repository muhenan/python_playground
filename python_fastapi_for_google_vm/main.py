from fastapi import FastAPI

# python -m uvicorn main:app --reload --port 8080
# python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8080

# sudo chmod +x entrypoint.sh

app = FastAPI()

# Define a route that returns a JSON response
@app.get("/hello")
def read_root():
    return "Hello FastAPI!!!"
