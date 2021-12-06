# -*- coding: utf-8 -*-
{
    'name': "OpenEduCat Credenciales",

    'summary': """
        OpenEduCat Credenciales""",

    'description': """
        OpenEduCat Credenciales
    """,

    'author': "Raul Rolando Jardinot Gonzalez",

    'category': 'Uncategorized',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'openeducat_erp', 'hr_employee_se_idr'],

    # always loaded
    'data': [
        'views/card_frontal.xml',
        'views/card_trasera.xml',
        'views/op_category_inherit.xml',
        'views/op_student_inherit.xml',
    ],
}