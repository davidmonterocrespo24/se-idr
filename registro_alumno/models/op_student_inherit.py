# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from odoo.modules import get_module_resource
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, \
    DEFAULT_SERVER_DATETIME_FORMAT
import re
import logging

_logger = logging.getLogger(__name__)
try:
    from odoo.tools import image_colorize, image_resize_image_big
except:
    image_colorize = False
    image_resize_image_big = False

class prueba(models.Model):
    _inherit = 'op.student'

    edad = fields.Integer(string='Edad', readonly=True, required=False, compute="_compute_calcular_edad_")
    observaciones = fields.Text(string="Observaciones", required=False)

    @api.depends('birth_date')
    def _compute_calcular_edad_(self):
        if self.birth_date:
            d1 = datetime.strptime(str(self.birth_date),"%Y-%m-%d").date()
            d2 = date.today()
            self.edad = relativedelta(d2,d1).years