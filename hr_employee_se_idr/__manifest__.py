# -*- coding: utf-8 -*-
{
    'name': "hr_employee_se_idr",

    'summary': """
        hr_employee_se_idr""",

    'description': """
        hr_employee_se_idr
    """,

    'author': "Alejandro Aparicio",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee.xml',
    ]
}
