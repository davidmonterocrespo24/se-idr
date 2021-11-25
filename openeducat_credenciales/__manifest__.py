# -*- coding: utf-8 -*-
{
    'name': "OpenEduCat Credenciales",

    'summary': """
        OpenEduCat Credenciales""",

    'description': """
        OpenEduCat Credenciales
    """,

    'author': "Raul Rolando Jardinot Gonzalez",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'openeducat_erp', 'hr_employee_se_idr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/card_frontal_ok.xml',
        'views/card_trasera_ok.xml',
        'views/op_category_inherit.xml',
        'views/op_student_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}