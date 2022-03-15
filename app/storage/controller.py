import uuid
from flask import request
from flask.views import MethodView
from app.storage.models import storage

class MediaStorage(MethodView):                 #/files/upload_file
    def post(self):                              
        file = request.files.get("file")
        if not file:
            return {"Erro:":"Não foi enviado um arquivo."}, 400
        file_format = request.args.get("file_format")
        file_name = f'{uuid.uuid4().hex}.{file_format}'
        response = storage.upload_file(file_key=file_name, file=file)
        if not response[0]:
            print(response)
            return {"erro":response[1]},400
        return {"nome_da_file":file_name},200

class GetMedia(MethodView):                     #/files/get_file
    def get(self):                               
        file_key = request.json.get("key", "")
        url = storage.get_url(file_key)
        return {"key":url}, 200