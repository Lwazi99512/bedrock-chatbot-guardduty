import os
import boto3
import psutil
from dotenv import load_dotenv

load_dotenv()

def test_aws_connection():
    region = os.getenv("AWS_REGION")
    try:
        ec2 = boto3.client("ec2", region_name=region)
        response = ec2.describe_regions()
        print("AWS Regions:")
        for r in response['Regions']:
            print(f" - {r['RegionName']}")
    except Exception as e:
        print(f"Error connecting to AWS: {e}")

def list_processes():
    print("\nLocal running processes:")
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")

if __name__ == "__main__":
    test_aws_connection()
    list_processes()
