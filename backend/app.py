from fastapi import FastAPI

app = FastAPI(
    title="Confluence Execution Engine",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "status": "running",
        "engine": "Confluence Execution Engine",
        "version": "1.0.0"
    }