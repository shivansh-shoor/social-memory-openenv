from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import uuid
import random
import os

app = FastAPI(title="Personal Social Memory Agent")

# Load data safely
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "sample_data.json")

try:
    with open(DATA_PATH) as f:
        DATA = json.load(f)
except Exception:
    DATA = {"posts": [], "threads": [], "chats": []}

class Action(BaseModel):
    action: str
    query: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"status": "active"}

@app.post("/reset")
def reset():
    task_types = ["fact_extraction", "thread_summary", "multi_hop_qa"]
    task = random.choice(task_types)
    
    if task == "fact_extraction":
        obs = "Extract a fact from the social posts. Example: Who went to Goa?"
    elif task == "thread_summary":
        obs = "Summarize the Goa trip planning thread."
    else:
        obs = "What gift is planned for Priya's birthday and who contributes how much?"
    
    return {
        "observation": obs,
        "episode_id": str(uuid.uuid4()),
        "task_type": task
    }

@app.post("/step")
def step(action: Action):
    # Simple reward based on length and keywords
    text = action.query.lower()
    reward = 0.5
    
    if len(text) > 20:
        reward = 0.8
    if any(word in text for word in ["goa", "priya", "rahul", "necklace", "birthday"]):
        reward = 1.0
    
    return {
        "reward": round(reward, 2),
        "done": False,
        "observation": "Answer received.",
        "info": {"task": action.action}
    }

@app.get("/state")
def state():
    return {"status": "active", "message": "Episode in progress"}
