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

    'depends': ['base', 'openeducat_erp', 'se_openeducat_se_idr','openeducat_core','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/card_student.xml',
        'views/op_category_inherit.xml',
        'views/op_student_inherit.xml',
        'views/card_student_website.xml',
        'views/portal_my_home_inherit.xml',
        'views/portal_layout_inherit.xml',
    ],
}