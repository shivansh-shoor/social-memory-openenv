import os
import requests
import time

HF_SPACE_URL = "https://shivanshd-meh.hf.space"   # ← Change to your actual Space URL

print("START")

for ep in range(1, 4):
    print(f"\n=== EPISODE {ep} ===")
    res = requests.post(f"{HF_SPACE_URL}/reset").json()
    print("Task:", res.get("task_type"))
    
    for step in range(1, 4):
        answer = "Priya and Rahul went to Goa. They planned a necklace gift for Priya's birthday with Shivansh contributing 2000."
        step_res = requests.post(f"{HF_SPACE_URL}/step", json={"action": "answer", "query": answer}).json()
        print(f"Step {step} Reward: {step_res.get('reward', 0)}")
        time.sleep(0.8)

print("\nEND")
