# 🟢 Google Skills Lab - **Deploy ADK agents to Agent Engine**   

* Lab - https://www.skills.google/paths/3273/course_templates/1275/labs/606597

## 👉 Task 1. Install ADK and set up your environment

```bash
gh auth login  ## Login GitHub
```
```bash
git clone https://github.com/nov05/gcp-adk-to-agent-engine.git adk_to_agent_engine
export PATH=$PATH:"/home/${USER}/.local/bin"
python3 -m pip install -r adk_to_agent_engine/requirements.txt
```
```bash
cd ~/adk_to_agent_engine
cat << EOF > .env
GOOGLE_GENAI_USE_VERTEXAI=TRUE
# GOOGLE_CLOUD_PROJECT=qwiklabs-gcp-02-917014665a34
GOOGLE_CLOUD_LOCATION=us-central1
MODEL=gemini-2.5-flash
EOF
```
```bash
cp .env transcript_summarization_agent/.env
```

## 👉 Task 2. Deploy to Agent Engine using the command line deploy method
## 👉 Task 3. Get and query an agent deployed to Agent Engine
Task 4. View and delete agents deployed to Agent Engine
