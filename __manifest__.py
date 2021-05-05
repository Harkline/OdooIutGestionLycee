# -*- coding: utf-8 -*-
{
    'name': "IutGestionLyceeYL",

    'summary': """This is my summary""",

    'description': """
        Module permettant de gérer un lycée.
    """,

    'author': "Yanis Levesque",
    'website': "https://github.com/Harkline/OdooIutGestionLycee",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    # Ajouter les vues ici (.xml)
    'data': [
        #'security/ir.model.access.csv',

        "views/agenda_view.xml",
        "views/cours_view.xml",
        "views/eleve_view.xml",


        "views/arborescence_menu_view.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
