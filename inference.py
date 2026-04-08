import os
import requests
import time

HF_TOKEN = os.getenv("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")                    # Will be set in HF Space environment
HF_SPACE_URL = "https://shivanshd-meh.hf.space"     # ← CHANGE THIS to your actual Space URL

print("START")

for episode in range(1, 4):
    print(f"\n=== EPISODE {episode} ===")
    
    # Reset
    try:
        res = requests.post(f"{HF_SPACE_URL}/reset", timeout=15).json()
        print("Task:", res.get("task_type", "Unknown"))
    except Exception as e:
        print("Reset failed:", e)
        continue

 
    for step in range(1, 4):
        print(f"Step {step}")
        answer = "Priya went to Goa with Rahul and they planned a necklace gift for her birthday from Tanishq with Shivansh contributing 2000"
        
        try:
            step_res = requests.post(
                f"{HF_SPACE_URL}/step", 
                json={"action": "answer", "query": answer},
                timeout=15
            ).json()
            print("Reward:", step_res.get("reward", 0))
        except Exception as e:
            print("Step error:", e)
        
        time.sleep(1)

print("\nEND")
