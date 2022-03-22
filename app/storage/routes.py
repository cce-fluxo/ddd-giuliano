from flask import Blueprint
from app.storage.controller import MediaStorage, GetMedia

storage_api = Blueprint('storage_api', __name__)

storage_api.add_url_rule('/files/upload_file', view_func=MediaStorage.as_view('upload_file'), methods=['POST'])
storage_api.add_url_rule('/files/get_file', view_func=GetMedia.as_view('get_file'), methods=['GET'])