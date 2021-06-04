# -*- coding: utf-8 -*-
{
    'name': "crm_lead_se_idr",

    'summary': """
        crm_lead_se_idr""",

    'description': """
        crm_lead_se_idr
    """,

    'author': "Alejandro Aparicio",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        'data/catalog_data.xml',
        'security/ir.model.access.csv',
        'views/crm_lead.xml',
    ],
}
