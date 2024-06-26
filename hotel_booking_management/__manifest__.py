{
    'name': 'Hotel Booking Management',
    'version': '15.0.1.0',
    'category': 'Human Resources/Employees',
    'summary': 'Hotel Booking Management',
    'description': """
        Hotel Booking Management
    """,
    'author': 'Le Hong Ngoc - Hc',
    'depends': ['website', 'product', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/feature_facility_management.xml',
        'views/booking_management.xml',
        'views/website_ui_templates.xml',
        'views/my_booking_website.xml',
        'views/menu_item.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'hotel_booking_management/static/src/css/style.css',
            'hotel_booking_management/static/src/js/booking.js',
        ],
        'web.assets_backend': [
            'hotel_booking_management/static/src/css/style.css',
        ],
    },
    'test': [],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True
}
