# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager


class CustomerPortal(CustomerPortal):

    @http.route(['/credencial'], type='http', auth="public", website=True)
    def credencial(self, **kw):
        values = {}
        values.update({
            'docs': request.env.user.user_line,
        })

        return request.render("openeducat_credenciales.report_credencial_template_website", values)



