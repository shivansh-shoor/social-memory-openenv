import os
hf_token = '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'
remote_url = f'https://SHIVANSHD:{hf_token}@huggingface.co/spaces/SHIVANSHD/MEH'
os.system('git config --global user.email "shivansh.dev.shoor@gmail.com"')
os.system('git config --global user.name "SHIVANSHD"')
os.system(f'git remote set-url origin {remote_url}')
os.system('git add .')
os.system('git commit -m "Deployment from ZIP package"')
os.system('git push origin main --force')
