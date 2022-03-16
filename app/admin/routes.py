from app.admin.controller import AdminG, AdminID, AdminLogin
from flask import Blueprint


admin_api = Blueprint('admin_api', __name__)

admin_api.add_url_rule('/admin', view_func=AdminG.as_view('admin_geral'), methods = ['POST', 'GET'])
admin_api.add_url_rule('/admin/<int:id>', view_func=AdminID.as_view('admin_id'), methods = ['GET', 'PATCH', 'DELETE'])
admin_api.add_url_rule('/admin/login', view_func=AdminLogin.as_view('admin_login'), methods = ['POST'])