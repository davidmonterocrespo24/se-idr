# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from datetime import datetime, date, time, timedelta

from odoo.exceptions import UserError, ValidationError
import re
import getpass

class RegistrarEstudiante(http.Controller):

    @http.route('/message_success', auth='public', website=True)
    def index1(self, **kw):
        return http.request.render('registro_alumno.message_success', {})

    # Registrar estudiante form metodo
    @http.route(['/registrar'], type='http', auth="public", website=True)
    def registrar_request(self):
        # modelo = request.env['vehicle.model'].search([])
        # marca = request.env['vehicle.model.brand'].search([])
        # values = {
        #     'modelo': modelo,
        #     'marca': marca
        # }
        # return request.render("registro_alumno.autos_form", values)
        return request.render("registro_alumno.registrar_form")


    # # Crear el estudiante
    # @http.route('/create_autos', auth='public', type='http', website=True)
    # def create_oportunidad_auto(self, **kw):
    #     request.env['crm.lead'].sudo().create({
    #         'name': 'Auto',
    #         'email_from': kw.get('email'),
    #         'contact_name': kw.get('contact_name'),
    #         'phone': kw.get('phone'),
    #         'cp': kw.get('cp'),
    #         'marca': kw.get('marca_id'),
    #         'sub_marca': kw.get('submarca_id'),
    #         'modelo': kw.get('modelo_id'),
    #         'description': kw.get('description'),
    #
    #     })
    #     return request.redirect('/message_success')