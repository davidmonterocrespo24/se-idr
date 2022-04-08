# -*- coding: utf-8 -*-
{
    'name': "Alta de estudiante de taller IDR.",

    'summary': """
        Alta de estudiante de taller IDR.""",

    'description': """
        Alta de estudiante de taller IDR.
    """,

    'author': "Raul Rolando Jardinot Gonzalez",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'openeducat_core', 'openeducat_parent'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_website.xml',
        'views/registrar_estudiante_form_website.xml',
        'views/message_success_website.xml',
        'views/view_op_student_inherit.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}