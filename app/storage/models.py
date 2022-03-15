import boto3
from os import environ
from botocore.exceptions import ClientError


class Storage:
    project_name = "ddd-giuliano"
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name='nyc3',
                            endpoint_url='http://nyc3.digitaloceanspaces.com',
                            aws_access_key_id=environ.get('AWS_ACCESS_KEY_ID'),
                            aws_secret_access_key=environ.get('AWS_SECRECT_ACCESS_KEY'))

    def upload_file(self, file_key, file) -> tuple:
        try:
            response = self.client.upload_fileobj(file, 'storage-fluxo', f'{self.project_name}/{file_key}')
        except ClientError as e:
            return False, e
        return True, ''

    def get_url(self, file_key):
        return self.cliente.generate_presigned_url(ClientMethod='get_object',
                                                    Params={'Bucket':'storage-fluxo',
                                                            'Key':f'{self.project_name}/{file_key}'},
                                                    ExpiresIn=300)

    def delete_object(self, file_key):
        self.client.delete_object(Bucket='storage-fluxo',
                                  Key=f'{self.project_name}/{file_key}')

storage = Storage()