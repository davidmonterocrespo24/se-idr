from odoo import _, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def contacts_whatsapp(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Send Whatsapp Message'),
                'res_model': 'whatsapp.message.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_user_id': self.id},
                }

class WhatsappCrm(models.Model):
    _inherit = 'crm.lead'

    def crm_whatsapp(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Send Whatsapp Message'),
                'res_model': 'whatsapp.message.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_user_id': self.partner_id.id},
                }

class WhatsappEmployee(models.Model):
    _inherit = 'hr.employee'

    def employee_whatsapp(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Send Whatsapp Message'),
                'res_model': 'whatsapp.message.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_user_id': self.address_home_id.id},
                }

class WhatsappStudent(models.Model):
    _inherit = 'op.student'

    def student_whatsapp(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Send Whatsapp Message'),
                'res_model': 'whatsapp.message.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_user_id': self.partner_id.id},
                }
