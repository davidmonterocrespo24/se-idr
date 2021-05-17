# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAddons/se-idr/seOpeneducatSeIdr(http.Controller):
#     @http.route('/custom_addons/se-idr/se_openeducat_se_idr/custom_addons/se-idr/se_openeducat_se_idr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addons/se-idr/se_openeducat_se_idr/custom_addons/se-idr/se_openeducat_se_idr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addons/se-idr/se_openeducat_se_idr.listing', {
#             'root': '/custom_addons/se-idr/se_openeducat_se_idr/custom_addons/se-idr/se_openeducat_se_idr',
#             'objects': http.request.env['custom_addons/se-idr/se_openeducat_se_idr.custom_addons/se-idr/se_openeducat_se_idr'].search([]),
#         })

#     @http.route('/custom_addons/se-idr/se_openeducat_se_idr/custom_addons/se-idr/se_openeducat_se_idr/objects/<model("custom_addons/se-idr/se_openeducat_se_idr.custom_addons/se-idr/se_openeducat_se_idr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addons/se-idr/se_openeducat_se_idr.object', {
#             'object': obj
#         })
