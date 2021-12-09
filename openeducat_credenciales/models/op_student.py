# -*- coding: utf-8 -*-

from odoo import fields, models, api
import logging
import time
import datetime
from odoo.exceptions import UserError, ValidationError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime, date, time, timedelta
import calendar


class EstudiantesInherit(models.Model):
    _inherit = 'op.student'

    vigencia_credencial = fields.Char(string='Vigencia Credencial', required=False,compute='compute_vigencia', store=True)
    centro_trabajo = fields.Char(string='CCT', required=False)

    @api.depends('registration_date')
    def compute_vigencia(self):
        # pass

        for model in self:
            model.vigencia_credencial = model.registration_date.year + 2
        # raise ValidationError(self.vigencia_credencial)

