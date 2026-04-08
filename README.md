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

```bash
yes | gcloud services enable orgpolicy.googleapis.com --project=$GOOGLE_CLOUD_PROJECT --quiet
export REGION=$(gcloud org-policies describe constraints/gcp.resourceLocations \
  --project=$GOOGLE_CLOUD_PROJECT \
  --format="value(spec.rules[0].values.allowedValues)" \
  | grep -oP '(?<=in:)(us|europe|asia)[a-z0-9-]+(?=-locations)' \
  | head -n 1)
echo $REGION
```
```bash
adk deploy agent_engine transcript_summarization_agent \
--display_name "Transcript Summarizer" \
--region $REGION \
--staging_bucket gs://$GOOGLE_CLOUD_PROJECT-bucket
```

## 👉 Task 3. Get and query an agent deployed to Agent Engine

```bash
PROJECT_NUMBER=$(gcloud projects describe $GOOGLE_CLOUD_PROJECT --format="value(projectNumber)")
echo $PROJECT_NUMBER
SERVICE_AGENT="service-$PROJECT_NUMBER@gcp-sa-aiplatform-re.iam.gserviceaccount.com"
echo $SERVICE_AGENT
```
```bash
gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
    --member="serviceAccount:$SERVICE_AGENT" \
    --role="roles/aiplatform.user"
```

```bash
cd ~/adk_to_agent_engine/transcript_summarization_agent
python3 query_agent_engine.py
```
Example output:
```bash
student_04_2365c655b4da@cloudshell:~/adk_to_agent_engine/transcript_summarization_agent (qwiklabs-gcp-00-56c8aff6759a)$ python3 query_agent_engine.py
[remote response] The user interacted with a virtual vehicle sales agent, expressing interest in buying a boat. After inquiring about the value of $50,000 for a boat, the agent confirmed it would purchase a "very nice boat," leading the user to agree to proceed with the purchase.
```

## 👉 Task 4. View and delete agents deployed to Agent Engine
