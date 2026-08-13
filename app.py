import os

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from dotenv import load_dotenv

load_dotenv()

project_endpoint = os.getenv("PROJECT_ENDPOINT")
model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

project = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential()
)

openai_client = project.get_openai_client()

response = openai_client.responses.create(
    model=model_deployment,
    input="Explain Microsoft Foundry in simple terms."
)

print(response.output_text)