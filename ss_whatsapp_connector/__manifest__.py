{
    'name': 'Whatsapp Odoo Connector',
    'version': '14.0.0.1',
    'summary': 'Whatsapp Odoo Connector',
    'author': 'Saaragh Technologies Pte Ltd',
    'company': 'Saaragh Technologies Pte Ltd',
    'maintainer': 'Saaragh Technologies Pte Ltd',
    'images': ['static/description/Banner.png'],
    'sequence': 4,
    'license': 'LGPL-3',
    'description': """Whatsapp Odoo Connector""",
    'category': 'Connector',
    'depends': [
        'base', 'contacts', 'crm'
    ],
    'data': [
        'security/ir.model.access.csv',
        # 'models/whatsapp_template.xml',
        'views/whatsapp_button_views.xml',
        'wizard/whatsapp_wizard.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
