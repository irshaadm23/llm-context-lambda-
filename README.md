# llm-context-lambda-
Serverless LLM inference pipeline on AWS using Lambda, S3, and SageMaker, demonstrating lightweight RAG via prompt-based context injection and cost-aware deployment.
# Serverless LLM Context Injection on AWS

## Overview
This project demonstrates how large language models (LLMs) can be integrated into real-world cloud systems using a serverless architecture. Rather than focusing on model training, the project explores how contextual data can be dynamically injected into prompts at inference time using AWS-native services.

The system uses AWS Lambda for orchestration, Amazon S3 for storing contextual data, and Amazon SageMaker as the intended inference layer for a foundation model.

## Key Components

### AWS Lambda
- Orchestrates request handling
- Retrieves contextual data from S3
- Injects context into prompts
- Invokes a SageMaker endpoint (placeholder)

### Amazon S3
- Stores JSON-based contextual data
- Acts as a simple, lightweight knowledge source

### IAM
- Least-privilege permissions for Lambda
- Controlled access to S3 and SageMaker APIs

### Amazon SageMaker
- Intended hosting environment for the foundation model
- Endpoint deployment deferred due to GPU quota limits

## Current Status
- Lambda function implemented
- S3 context data configured
- IAM permissions defined
- SageMaker endpoint invocation logic implemented (endpoint not deployed)

Model deployment was intentionally paused due to GPU quota restrictions and cost considerations.

## Key Learnings
- How LLMs are integrated into cloud-native systems
- Prompt-based context injection as a lightweight RAG approach
- IAM role design and least-privilege access
- Cost and quota constraints in real-world AI deployments

## Future Improvements
- Deploy SageMaker endpoint once GPU quotas are available
- Add API Gateway for external access
- Experiment with structured context formats
- Introduce embeddings or vector search if needed


## Disclaimer
This project focuses on architectural design and integration patterns. It is not intended as a production-ready system.
