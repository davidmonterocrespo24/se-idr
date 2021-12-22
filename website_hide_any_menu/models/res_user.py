# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Users(models.Model):
    _inherit = 'res.users'

    website_menu_ids = fields.Many2many('website.menu', 'user_website_menu_rel', 'user_id', 'menu_id',
                                        string='Menu To Hide', help='Select Menus To Hide From This User')
    website_page_ids = fields.Many2many('website.page', 'user_website_page_rel', 'user_id', 'page_id',
                                        string='Page To Hide', help='Select Page To Hide From This User')

    @api.model
    def create(self, values):
        self.env['website.menu'].clear_caches()
        self.env['website.page'].clear_caches()
        return super(Users, self).create(values)

    def write(self, values):
        self.env['website.menu'].clear_caches()
        self.env['website.page'].clear_caches()
        return super(Users, self).write(values)


class WebsiteMenu(models.Model):
    _inherit = 'website.menu'

    hide_user_ids = fields.Many2many('res.users', 'user_website_menu_rel', 'menu_id', 'user_id',
                                     string='Hide From Users', help='Select User To Hide This Menu')
    hide_group_ids = fields.Many2many('res.groups', 'group_website_menu_rel', 'menu_id', 'group_id',
                                      string='Hide From Groups', help='Select Groups To Hide This Menu')

    @api.model
    def create(self, values):
        self.env['website.menu'].clear_caches()
        self.env['website.page'].clear_caches()
        return super(WebsiteMenu, self).create(values)

    def write(self, values):
        self.env['website.menu'].clear_caches()
        self.env['website.page'].clear_caches()
        return super(WebsiteMenu, self).write(values)


class WebsitePage(models.Model):
    _inherit = 'website.page'

    hide_user_ids = fields.Many2many('res.users', 'user_website_page_rel', 'page_id', 'user_id', string='Hide From Users')
    hide_group_ids = fields.Many2many('res.groups', 'group_website_page_rel', 'page_id', 'group_id', string='Hide From Groups')

    @api.model
    def create(self, values):
        self.env['website.menu'].clear_caches()
        self.env['website.page'].clear_caches()
        return super(WebsitePage, self).create(values)

    def write(self, values):
        self.env['website.menu'].clear_caches()
        self.env['website.page'].clear_caches()
        return super(WebsitePage, self).write(values)


class ResGroups(models.Model):
    _inherit = 'res.groups'

    hide_menu_ids = fields.Many2many('website.menu', 'group_website_menu_rel', 'group_id', 'menu_id', string='Menu To Hide')
    hide_page_ids = fields.Many2many('website.page', 'group_website_page_rel', 'group_id', 'page_id', string='Page To Hide')

    @api.model
    def create(self, values):
        self.env['website.menu'].clear_caches()
        self.env['website.page'].clear_caches()
        return super(ResGroups, self).create(values)

    def write(self, values):
        self.env['website.menu'].clear_caches()
        self.env['website.page'].clear_caches()
        return super(ResGroups, self).write(values)


class WebsiteHideMenuPageSetting(models.Model):
    _name = 'website.hide.menu.page.setting'
    _description = 'Website Hide Menu Page Setting'

    name = fields.Char()
    internal_menu_hide = fields.Many2many('website.menu', 'internal_user_menu_rel', 'generic_setting_id', 'user_id',
                                          string='Hide Menu From All Internal Users')
    internal_page_hide = fields.Many2many('website.page', 'internal_user_page_rel', 'generic_setting_id', 'user_id',
                                          string='Hide Page From All Internal Users')
    portal_menu_hide = fields.Many2many('website.menu', 'portal_user_menu_rel', 'generic_setting_id', 'user_id',
                                        string='Hide Menu From Portal Users')
    portal_page_hide = fields.Many2many('website.page', 'portal_user_page_rel', 'generic_setting_id', 'user_id',
                                        string='Hide Page From Portal Users')
    public_menu_hide = fields.Many2many('website.menu', 'public_user_menu_rel', 'generic_setting_id', 'user_id',
                                        string='Hide Menu From Public Users')
    public_page_hide = fields.Many2many('website.page', 'public_user_page_rel', 'generic_setting_id', 'user_id',
                                        string='Hide Page From Public Users')
