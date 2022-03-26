import streamlit as st
import boto3
import json

# Create a low-level client representing Amazon SageMaker Runtime
session = boto3.Session()
sagemaker_runtime = session.client('sagemaker-runtime', region_name="us-east-1")

# The name of the endpoint. The name must be unique within an AWS Region in your AWS account. 
endpoint_name='sm-endpoint-gpt-j-6b'


def generate_text(prompt):
    payload = {"inputs": prompt}

    response = sagemaker_runtime.invoke_endpoint(
                                EndpointName=endpoint_name, 
                                ContentType='application/json',
                                Body=json.dumps(payload)
                                )
                                
    result = json.loads(response['Body'].read().decode())
    text = result[0]['generated_text']
    return text


st.header("My very own GPT-J Playground")
prompt = st.text_area("Enter your prompt here:")

if st.button("Run"):
    generated_text = generate_text(prompt)
    st.write(generated_text)