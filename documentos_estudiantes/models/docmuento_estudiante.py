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



class File(models.Model):
    _inherit = 'muk_dms.file'

    @api.depends('name', 'directory', 'directory.parent_path')
    def _compute_path(self):
        rec.directory.parent_path

        return super(File, self)._compute_path
        records_with_directory = self - self.filtered(lambda rec: not rec.directory)
        updated = self.env['muk_dms.file']
        if records_with_directory:
            paths = [list(map(int, rec.directory.parent_path.split('/')[:-1])) for rec in records_with_directory]
            model = self.env['muk_dms.directory'].with_context(dms_directory_show_path=False)
            directories = model.browse(set(functools.reduce(operator.concat, paths)))
            data = dict(directories._filter_access('read').name_get())
            for record in self:
                path_names = []
                path_json = []
                for id in reversed(list(map(int, record.directory.parent_path.split('/')[:-1]))):
                    if id not in data:
                        break
                    path_names.append(data[id])
                    path_json.append({
                        'model': model._name,
                        'name': data[id],
                        'id': id,
                    })
                path_names.reverse()
                path_json.reverse()
                name = record.name_get()
                path_names.append(name[0][1])
                path_json.append({
                    'model': record._name,
                    'name': name[0][1],
                    'id': isinstance(record.id, int) and record.id or 0,
                })
                updated |= record
                record.update({
                    'path_names': '/'.join(path_names),
                    'path_json': json.dumps(path_json),
                })

        (self - updated).update({
            'path_names': False,
            'path_json': False,
        })