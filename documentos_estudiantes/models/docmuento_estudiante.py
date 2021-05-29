# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models,_
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class OpStudent(models.Model):
    _inherit = 'op.student'

    storage = fields.Many2one(comodel_name="muk_dms.storage", string="Documentos", required=False, )

    @api.model
    def create(self, values):
        record = super(OpStudent, self).create(values)
        storage_model = self.env['muk_dms.storage']
        storage = storage_model.create({'name': record.name, 'save_type': 'database', })
        record.storage = storage.id
        model_directory = self.env['muk_dms.directory']
        if not model_directory.search([('name', '=', '['+record.name+']Expediente Alumno'), ('root_storage', '=', storage.id)]):
            model_directory.create({
                'name': '['+record.name+']Expediente Alumno',
                'is_root_directory': True,
                'partner_relacionado_id': record.id,
                'root_storage': storage.id,
            })

        return record

    def documentos_views(self):
        model_directory = self.env['muk_dms.directory']
        storage= self.storage
        if not self.storage:
            storage_model = self.env['muk_dms.storage']
            storage = storage_model.create({'name': self.name, 'save_type': 'database', })
            self.storage = storage

        if not model_directory.search([('name', '=', '['+self.name+']Expediente Alumno'), ('root_storage', '=', storage.id)]):
            model_directory.create({
                'name': '['+self.name+']Expediente Alumno',
                'is_root_directory': True,
                'partner_relacionado_id': self.id,
                'root_storage': storage.id,
            })



        return {
            'mame': "Documentos del Estudiante: " + self.name,
            'view_mode': 'kanban,tree,form',
            'res_model': 'muk_dms.directory',
            'domain': [("storage", "=", self.storage.id), ("is_hidden", "=", False), ],
            'context': {
                'default_root_storage': self.storage.id,
                'default_is_root_directory': True,
                'default_name': self.name,
               },
            'type': 'ir.actions.act_window',
        }


    def unlink(self):
        for record in self:
            model_directory = self.env['muk_dms.directory']
            model_directory.search([('root_storage', '=', record.storage.id)]).unlink()
            record.storage.unlink()
        return super(OpStudent, self).unlink()

    def action_send(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('documentos_estudiantes', 'email_document_template')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False

        partner_ids = []
        partner_ids.append(self.partner_id.id)
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        base_url += '/document/add'
        ctx = {
            'default_model': 'op.student',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_partner_ids': partner_ids,
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'base_url':base_url,
            #'custom_layout': "mail.mail_notification_paynow",
            #'proforma': self.env.context.get('proforma', False),
            'force_email': False
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }
class Directory(models.Model):
    _inherit = 'muk_dms.directory'

    partner_relacionado_id = fields.Many2one(comodel_name="op.student", string="Estudiante Relacionado",
                                             required=False, )


