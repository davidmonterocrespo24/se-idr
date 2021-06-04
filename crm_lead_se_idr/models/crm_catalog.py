# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Catalog(models.Model):
    _name = 'crm.catalog'
    _description = "Catálogo"
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(string='Nombre')
    complete_name = fields.Char(
        'Nombre Completo', compute='_compute_complete_name',
        store=True)
    parent_id = fields.Many2one('crm.catalog', 'Categoría Padre', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('crm.catalog', 'parent_id', 'Categoría Hija')


    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError('No puede crear una categoría recursiva.')
        return True

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]