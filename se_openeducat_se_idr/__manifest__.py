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
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','openeducat_core','openeducat_fees'],

    'data': [
        'security/ir.model.access.csv',
        'views/op_student.xml',
        'views/student_view.xml',
        'views/account_payment_view'
    ],
}
