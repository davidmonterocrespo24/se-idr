from odoo import fields, models, api


class OpstudentInherit(models.Model):
    _name = 'hola.hola'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']