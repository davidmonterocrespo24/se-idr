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
        relationship = request.env['op.parent.relationship'].sudo().search([])
        # marca = request.env['vehicle.model.brand'].search([])
        values = {
            'relationship': relationship,
        }
        # return request.render("registro_alumno.autos_form", values)
        return request.render("registro_alumno.registrar_form", values)


    # # Crear el estudiante
    @http.route('/create_student', auth='public', type='http', website=True)
    def create_student_fathers(self, **kw):
        estudent = request.env['op.student'].sudo().create({
            'name': kw.get('name_student') + " " + kw.get('apellido_paterno_student') + " " + kw.get('apellido_materno_student'),
            'first_name': kw.get('name_student'),
            'middle_name': kw.get('apellido_paterno_student'),
            'last_name': kw.get('apellido_materno_student'),
            'gender': kw.get('student_genero'),
            'birth_date': kw.get('date_birth'),
            'email': kw.get('email_student'),
            'mobile': kw.get('mobile_student'),
            'observaciones': kw.get('observaciones'),
        })
        contacto_padre = request.env['res.partner'].sudo().create({
            'is_parent': True,
            'name': kw.get('name_1') + " " + kw.get('apellido_paterno_1') + " " + kw.get('apellido_materno_1'),
            'email': kw.get('email_1'),
            'mobile': kw.get('mobile_1'),
            'phone': kw.get('phone_1'),
        })

        # estudent_id = request.env['op.parent.relationship'].search([('first_name', '=', kw.get('name_student'))])
        # print(estudent.id)
        # print(contacto_padre.id)
        request.env['op.parent'].sudo().create({
            # 'is_parent': True,
            'name': contacto_padre.id,
            # 'email': kw.get('email_father'),
            'mobile': kw.get('mobile_father'),
            # 'phone': kw.get('phone_oficina'),
            'relationship_id': kw.get('relationship_id_1'),
            'student_ids': estudent,

        })
        if kw.get('name_2'):
            otro_contacto = request.env['res.partner'].sudo().create({
                'is_parent': True,
                'name': kw.get('name_2') + " " + kw.get('apellido_paterno_2') + " " + kw.get('apellido_materno_2'),
                'email': kw.get('email_2'),
                'mobile': kw.get('mobile_2'),
                'phone': kw.get('phone_2'),
            })

            request.env['op.parent'].sudo().create({
                # 'is_parent': True,
                'name': otro_contacto.id,
                # 'email': kw.get('email_father'),
                'mobile': kw.get('mobile_father'),
                # 'phone': kw.get('phone_oficina'),
                'relationship_id': kw.get('relationship_id_2'),
                'student_ids': estudent,
            })
        return request.redirect('/message_success')