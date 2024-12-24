import boto3
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_s3_connection():
    # Create an S3 client
    s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    
)
    return s3


def get_s3_object(bucket_name, object_key):
    # Create an S3 client
    s3 = get_s3_connection()

    # Get the object from the bucket
    response = s3.get_object(Bucket=bucket_name, Key=object_key)

    # Read the object's content
    data = response['Body'].read()
    return data


def create_s3_folder(bucket_name, folder_name):
    s3 = get_s3_connection()
    s3.put_object(Bucket= bucket_name, Key=f"{folder_name}/")


def update_s3_object(bucket_name, object_key, new_content):
    s3 = get_s3_connection()
    
    # Update the object's content
    s3.put_object(Bucket=bucket_name, Key=object_key, Body=new_content)
    print(f"Updated {object_key} with new content")


def copy_folder_from_base_to_replit_folder(bucket_name, source_folder, destination_folder):
    s3 = get_s3_connection()
    create_s3_folder(bucket_name, destination_folder)
    # List objects in the source folder
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=source_folder)
    
    if 'Contents' in response:
        print("content in source", response['Contents'])
        for obj in response['Contents']:
            source_key = obj['Key']
            destination_key = source_key.replace(source_folder, destination_folder, 1)
            
            # Copy the object to the destination folder
            copy_source = {'Bucket': bucket_name, 'Key': source_key}
            s3.copy_object(CopySource=copy_source, Bucket=bucket_name, Key=destination_key)
            print(f"Copied {source_key} to {destination_key}")


if __name__ == "__main__":
    bucket_name = 'replit-bucket-s3'
    object_key = 'base/python/main.py'
    updated_content = "#This is just a comment"
    
    # read_data = get_s3_object(bucket_name, object_key)
    # data = update_s3_object(bucket_name, object_key, updated_content)

    # copy_folder_from_base_to_replit_folder(bucket_name, 'base', 'code/repil-1')
    # print(read_data)