# -*- coding: utf-8 -*-
{
    'name': "Modul Odoo",

    'summary': """
        Regitration Materials""",

    'description': """
        Untuk regitrasi material yg akan diual
    """,

    'author': "Maharani IP",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
