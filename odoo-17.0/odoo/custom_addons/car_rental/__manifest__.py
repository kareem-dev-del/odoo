# __manifest__.py
{
    'name': "Car Rental",
    'author': "Kareem Hesham",
    'category': '',
    'version': '17.0.0.1.0',
    'depends': [
        'base',
    ],
    'data': [
        # ضع ملفات XML هنا لاحقاً
        'views/car_views.xml',
        'security/ir.model.access.csv',



    ],
    'application': True,
}