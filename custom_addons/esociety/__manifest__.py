{
    "name": "Society Management System",
    "author": "POINT9 COMMERCE LLP",
    "license": "LGPL-3",
    "version": "18.0.1.0",
    'category': 'Management',
    'depends': ['base', 'contacts', 'stock', 'account'],
    "data": [
        "security/ir.model.access.csv",
        "views/master_views.xml",
        "views/member_views.xml",
        "views/society_flat_views.xml",
    ],
    'installable': True,
    'application': True,
}