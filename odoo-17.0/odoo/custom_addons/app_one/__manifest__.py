{
    'name': "App One",
    'author': "Kareem Hesham",
    'category': 'Sales',
    'version': '17.0.0.1.0',
    'depends': [
        'base',
        'sale_management',
        'mail',
        #'account_accountant',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_veiw.xml',
        'views/owner_veiw.xml',
        'views/tag_veiw.xml',
        'views/sale_order_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'app_one/static/src/css/property.css'  # ✅ استخدم / بدل \
        ]
    },
    'application': True,
    'license': 'LGPL-3',
    'installable': True,
}