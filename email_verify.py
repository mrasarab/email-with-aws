import boto3
from dotenv import load_dotenv
import os

load_dotenv()


def verify(email: str):
  
    session = boto3.Session(aws_access_key_id=os.getenv('aws_access_key_id'),
                                aws_secret_access_key=os.getenv('aws_secret_access_key'), region_name=os.getenv('region_name'))
    client = session.client('ses')
    response = client.verify_email_identity(EmailAddress=email)
    
    
