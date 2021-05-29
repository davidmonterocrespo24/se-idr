import base64

from odoo import http
from odoo.http import request

class WebsiteIdr(http.Controller):
     @http.route('/document/add', type='http', auth='user', website=True)
     def show_upload_webpage(self, url=None, upload=None, **post):
          if request.httprequest.method == 'POST':
               user_id = request.uid
               user = request.env['op.student'].sudo().search([('user_id','=',user_id)],limit=1)
               upload_file = request.httprequest.files.getlist('upload')
               Files = request.env['muk_dms.file'] 
               Directorys = request.env['muk_dms.directory']
               directory = Directorys.sudo().search([('name', '=', '['+user.name+']Expediente Alumno'), ('root_storage', '=', user.storage.id)],limit=1)
               if upload_file:
                    for i in range(len(upload_file)):
                         file_id = Files.sudo().create({
                              'name': upload_file[i].filename,
                              'content': base64.b64encode(upload_file[i].read()),
                              'directory': directory.id
                         })
               return http.request.render('documentos_estudiantes.upload_doc_ok_page', {})
          else:    
               return http.request.render('documentos_estudiantes.upload_doc_web_page', {})
     