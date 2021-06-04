# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = "crm.lead"


    categ_id = fields.Many2one(
        'crm.catalog', 'Interesado en',
        change_default=True)


