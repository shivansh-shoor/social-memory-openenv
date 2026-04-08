from fastapi import FastAPI
import json, os
app = FastAPI()
@app.get('/')
def read_root(): return {'Status': 'Active'}