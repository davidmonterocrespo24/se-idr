# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custom_addons/se-idr/se_openeducat_se_idr(models.Model):
#     _name = 'custom_addons/se-idr/se_openeducat_se_idr.custom_addons/se-idr/se_openeducat_se_idr'
#     _description = 'custom_addons/se-idr/se_openeducat_se_idr.custom_addons/se-idr/se_openeducat_se_idr'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
