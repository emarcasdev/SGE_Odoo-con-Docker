# -*- coding: utf-8 -*-
{
    'name': "Gestión hospitalaria",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Eder Martínez",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'application': True,
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # Importamos las vistas
        'views/paciente.xml',
        'views/medico.xml',
        'views/consulta.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',''
    ],
}

