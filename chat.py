import os

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()

project_endpoint = os.getenv("PROJECT_ENDPOINT")
model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

project = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential()
)

openai_client = project.get_openai_client()

# 1. Create conversation history
conversation_history = []

print("Chat started. Type 'exit' to quit.")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    # 2. Add user input to history
    conversation_history.append({
        "role": "user",
        "content": question
    })

    # 3. Send conversation history to Responses API
    response = openai_client.responses.create(
        model=model_deployment,
        input=conversation_history
    )

    answer = response.output_text

    print("AI:", answer)

    # 4. Add model output to history
    conversation_history.append({
        "role": "assistant",
        "content": answer
    })