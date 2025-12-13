# -*- coding: utf-8 -*-
{
    'name': "Biblioteca de Comics",  # Titulo del módulo
    'summary': "Gestionar comics",  # Resumen de la funcionaliadad
    'description': """
        Gestor de bibliotecas
    ==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Eder Martínez",
    'website': "https://tusitio.com",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        #Estos dos primeros ficheros:
        #1) El primero indica grupo de seguridad basado en rol
        #2) El segundo indica la politica de acceso del modelo
        #Mas información en https://www.odoo.com/documentation/17.0/es/developer/howtos/rdtraining/05_securityintro.html
        #Y en www.odoo.yenthevg.com/creating-security-groups-odoo/ 
        'security/groups.xml',
        'security/ir.model.access.csv',
        #Cargamos la vista de la biblioteca de comics y socios
        'views/biblioteca_comic.xml',
        'views/biblioteca_socio.xml',
        'views/biblioteca_ejemplar.xml'
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
