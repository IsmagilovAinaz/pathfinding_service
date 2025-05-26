from fastapi import FastAPI
from pydantic import BaseModel
from .path_finder import find_path

app = FastAPI()

class PathRequest(BaseModel):
    start: tuple[int, int]
    goal: tuple[int, int]
    grid: list[list[int]]

@app.post("/find-path")
def path_finding(req: PathRequest):
    path = find_path(req.grid, req.start, req.goal)
    return {"path": path}