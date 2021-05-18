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
            'view_type': 'form',
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


class Directory(models.Model):
    _inherit = 'muk_dms.directory'

    partner_relacionado_id = fields.Many2one(comodel_name="op.student", string="Estudiante Relacionado",
                                             required=False, )


