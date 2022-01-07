# -*- coding: utf-8 -*-
{
    'name': "OpenEducat Evaluaciones",

    'summary': """
        OpenEducat Evaluaciones""",

    'description': """
        OpenEducat Evaluaciones
    """,

    'author': "Raul Rolando Jardinot Gonzalez",

    'category': 'Uncategorized',
    'version': '13.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','openeducat_erp','website','se_openeducat_se_idr','portal','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/op_subject_inherit_view.xml',
        'views/views.xml',
        'views/card_student_website.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}