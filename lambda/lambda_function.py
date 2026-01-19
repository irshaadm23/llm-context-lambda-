import json
import boto3

# AWS clients
s3_client = boto3.client("s3")
sagemaker_client = boto3.client("sagemaker-runtime")

def lambda_handler(event, context):
    """
    Lambda handler that:
    1. Reads contextual data from S3
    2. Injects it into a prompt (lightweight RAG)
    3. Invokes a SageMaker-hosted LLM endpoint
    """

    user_input = event.get("user_input", "")

    try:
        # Retrieve context data from S3
        s3_response = s3_client.get_object(
            Bucket="YOUR_S3_BUCKET_NAME",
            Key="console_pricing.json"
        )

        context_data = json.loads(
            s3_response["Body"].read().decode("utf-8")
        )

        # Simple keyword routing to decide whether to inject context
        if any(word in user_input.lower() for word in ["price", "cost", "console"]):
            prompt = f"""
User question:
{user_input}

You are a gaming expert. Use the reference data below to answer accurately.

Reference data:
{context_data}
"""
        else:
            prompt = f"""
User question:
{user_input}

You are a gaming expert. Answer clearly and concisely.
"""

        # Invoke SageMaker endpoint (placeholder)
        response = sagemaker_client.invoke_endpoint(
            EndpointName="YOUR_SAGEMAKER_ENDPOINT_NAME",
            ContentType="application/json",
            Body=json
