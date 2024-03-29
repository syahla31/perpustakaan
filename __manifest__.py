# -*- coding: utf-8 -*-
{
    'name': "perpustakaan",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'sale', 'board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/dashboard.xml',
        'views/data_buku_views.xml',
        'views/data_anggota_views.xml',
        'views/data_petugas_views.xml',
        'views/peminjaman_views.xml',
        'views/returnbuku_views.xml',
        'report/buku_report.xml',
        'views/menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'css': [
        'static/src/css/my_module.css',
    ],

    'assets': {
        'web.assets_backend': [
            'perpustakaan/static/src/components/**/*.js',
            'perpustakaan/static/src/components/**/*.xml',
            'perpustakaan/static/src/components/**/*.scss',
        ],
    },
}
