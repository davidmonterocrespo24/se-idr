# -*- coding: utf-8 -*-
{
    'name': "se_openeducat_se_idr",

    'summary': """
        se_openeducat_se_idr
        """,

    'description': """
        Openeducat SE IDR
    """,

    'author': "Alejandro",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
