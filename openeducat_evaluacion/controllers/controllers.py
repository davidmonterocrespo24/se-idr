# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import route
from odoo.addons.portal.controllers.portal import CustomerPortal

class CustomerPortalInherit(CustomerPortal):
    @route(['/my', '/my/home'], type='http', auth="user", website=True)
    def home(self, **kw):
        print("**************** Estoy dentro del controlador*******************")
        values = self._prepare_portal_layout_values()
        return request.render("portal.portal_my_home", values)