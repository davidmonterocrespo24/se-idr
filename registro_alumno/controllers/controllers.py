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
    @http.route('/create_student', auth='public', type='http', website=True)
    def create_student_fathers(self, **kw):
        request.env['op.student'].sudo().create({
            'name': kw.get('name_student'),
            'first_name': kw.get('name_student'),
            'middle_name': kw.get('apellido_paterno_student'),
            'last_name': kw.get('apellido_materno_student'),
            # 'gender': kw.get('student_genero'),
            # 'birth_date': kw.get('date_birth'),
            # 'email': kw.get('email_student'),
            # 'mobile': kw.get('mobile_student'),
            # 'phone': kw.get('mobile_student'),
            # 'marca': kw.get('marca_id'),
            # # 'sub_marca': kw.get('submarca_id'),
            # # 'modelo': kw.get('modelo_id'),
            # # 'description': kw.get('description'),

        })

        # request.env['res.partner'].sudo().create({
        #     'is_parent': True,
        #     'name': kw.get('name_father') + kw.get('apellido_paterno_father') + kw.get('apellido_materno_father'),
        #     'email': kw.get('email_father'),
        #     'mobile': kw.get('mobile_father'),
        #     'phone': kw.get('phone_oficina'),
        #
        # })
        return request.redirect('/message_success')