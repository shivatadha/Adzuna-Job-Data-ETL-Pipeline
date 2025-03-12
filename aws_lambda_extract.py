import os
import json
import boto3
import requests

def lambda_handler(event, context):
    # Fetch environment variables
    app_id = os.getenv("ADZUNA_APP_ID")
    app_key = os.getenv("ADZUNA_APP_KEY")
    bucket_name = os.getenv("S3_BUCKET_NAME")
    folder_name = os.getenv("S3_FOLDER")

    if not all([app_id, app_key, bucket_name, folder_name]):
        return {
            "statusCode": 500,
            "body": "Missing required environment variables."
        }
    
    # Define the Adzuna API parameters
    base_url = "https://api.adzuna.com/v1/api/jobs"
    country_code = "us"  # Example: US jobs
    endpoint = f"{base_url}/{country_code}/search/1"
    params = {
        "app_id": app_id,
        "app_key": app_key,
        "results_per_page": 50,
    }

    # Make the API request
    response = requests.get(endpoint, params=params)
    if response.status_code != 200:
        return {
            "statusCode": response.status_code,
            "body": f"Failed to fetch data: {response.text}"
        }

    # Parse the response JSON
    data = response.json()
    jobs = data.get("results", [])
    if not jobs:
        return {
            "statusCode": 200,
            "body": "No jobs found."
        }

    # Save data to S3
    s3_client = boto3.client("s3")
    file_name = f"{folder_name}/jobs.json"
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=json.dumps(jobs, indent=4),
            ContentType="application/json"
        )
        return {
            "statusCode": 200,
            "body": f"Data successfully saved to {bucket_name}/{file_name}"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Failed to save data to S3: {str(e)}"
        }
