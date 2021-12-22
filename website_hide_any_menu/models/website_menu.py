from odoo import fields, models


class WebsiteMenu(models.Model):
    _inherit = 'website.menu'

    def _compute_visible(self):
        # Override Existing _compute_visible Method To Hide Any Menu From Specific User
        for menu in self:
            visible = True
            if menu.page_id and not menu.page_id.sudo().is_visible and not menu.user_has_groups('base.group_user'):
                visible = False
            menu.is_visible = visible
            user = self.env.user

            if visible:
                # Check Current User is Internal User Or Public User Or Portal User Or
                generic_setting = self.env['website.hide.menu.page.setting'].sudo().search([], limit=1)
                if user.has_group('base.group_user'):  # Internal User
                    for menu_id in generic_setting.internal_menu_hide:
                        if menu.id == menu_id.id:
                            menu.is_visible = False
                            break
                if user.has_group('base.group_portal'):
                    for menu_id in generic_setting.portal_menu_hide:
                        if menu.id == menu_id.id:
                            menu.is_visible = False
                            break
                if user.login == 'public':
                    for menu_id in generic_setting.public_menu_hide:
                        if menu.id == menu_id.id:
                            menu.is_visible = False
                            break

                # User Specific Hide menu
                menu_ids = [w_menu.id for w_menu in user.website_menu_ids]
                if menu.id in menu_ids:
                    menu.is_visible = False

                # Check If Hide Menu Is Set In Any Group Or Not
                for group in user.groups_id:
                    if group.hide_menu_ids:
                        menu_ids = [w_menu.id for w_menu in group.hide_menu_ids]
                        if menu.id in menu_ids:
                            menu.is_visible = False


class Page(models.Model):
    _inherit = 'website.page'

    is_visible = fields.Boolean(compute='_compute_visible', string='Is Visible')

    def _compute_visible(self):
        for page in self:
            sudo_page = page.sudo()
            is_visible = sudo_page.website_published and (not sudo_page.date_publish or sudo_page.date_publish < fields.Datetime.now())
            page.is_visible = is_visible

            user = self.env.user
            if is_visible:
                # Check Current User is Internal User Or Public User Or Portal User Or
                generic_setting = self.env['website.hide.menu.page.setting'].sudo().search([], limit=1)
                if user.has_group('base.group_user'):  # Internal User
                    for page_id in generic_setting.internal_page_hide:
                        if page.id == page_id.id:
                            page.is_visible = False
                            return True
                if user.has_group('base.group_portal'):
                    for page_id in generic_setting.portal_page_hide:
                        if page.id == page_id.id:
                            page.is_visible = False
                            return True
                if user.login == 'public':
                    for page_id in generic_setting.public_page_hide:
                        if page.id == page_id.id:
                            page.is_visible = False
                            return True

                # User Specific Hide Page
                page_ids = [w_page.id for w_page in user.website_page_ids]
                if page.id in page_ids:
                    page.is_visible = False
                    return True

                # Check If Hide Page Is Set In Any Group Or Not
                for group in user.groups_id:
                    if group.hide_page_ids:
                        page_ids = [w_page.id for w_page in group.hide_page_ids]
                        if page.id in page_ids:
                            page.is_visible = False
                            return True
