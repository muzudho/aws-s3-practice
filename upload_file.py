import argparse
import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        _response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# Test
# python.exe -m upload_file --target hello-world.txt --bucket muzudho-h4b
#                                    ---------------
#                                    This file to upload
#                                                             -----------
#                                                             Bucket name
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='AWS S3 Practice.')
    parser.add_argument('--target', help='This file to upload')
    parser.add_argument('--bucket', help='Bucket name')
    args = parser.parse_args()

    upload_file(args.target, args.bucket)
    pass
