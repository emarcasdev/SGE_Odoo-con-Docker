# -*- coding: utf-8 -*-
{
    'name': "lista_tareas",

    'summary': """Sencilla Lista de tareas""",

    'description': """Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevo modelo de datos""",

    'author': "Eder Martínez",
    'website': "https://www.practica3odoo.com",
    #Indicamos que es una aplicación
    'application': True,

    # Vamos a utilizar la categoría Productivity
    'category': 'Productivity',
    'version': '0.1',

    # Indicamos lista de módulos necesarios para que este funcione correctamente
    # En este ejemplo solo depende del módulo "base"
    'depends': ['base'],

    # Esto siempre se carga
    'data': [
        'security/ir.model.access.csv',
        #Este primero indica la politica de acceso del módulo
        'views/views.xml',
        #Cargamos las vistas y las plantillas
        'views/templates.xml',
    ]
}

