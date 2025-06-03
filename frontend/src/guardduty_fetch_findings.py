import boto3
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize GuardDuty client
client = boto3.client(
    'guardduty',
    region_name='us-east-2',  # Replace if your region is different
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

# Get the detector ID
def get_detector_id():
    response = client.list_detectors()
    detectors = response.get("DetectorIds", [])
    if not detectors:
        print("No detectors found. Is GuardDuty enabled?")
        return None
    return detectors[0]

# Get and print findings
def get_findings(detector_id):
    findings = client.list_findings(DetectorId=detector_id, MaxResults=10)
    finding_ids = findings.get("FindingIds", [])
    if not finding_ids:
        print("No findings detected. Your environment looks clean.")
        return

    detailed_findings = client.get_findings(DetectorId=detector_id, FindingIds=finding_ids)
    for finding in detailed_findings["Findings"]:
        print(f"\n--- Finding ID: {finding['Id']} ---")
        print(f"Type: {finding['Type']}")
        print(f"Severity: {finding['Severity']}")
        print(f"Resource: {finding['Resource']}")
        print(f"Description: {finding['Description']}\n")

if __name__ == "__main__":
    detector_id = get_detector_id()
    if detector_id:
        get_findings(detector_id)
