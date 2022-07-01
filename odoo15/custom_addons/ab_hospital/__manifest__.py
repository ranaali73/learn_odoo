{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'rAz',
    'sequence': -100,
    'summary': 'Hospital Management System',
    'website': 'https://kics.edu.pk/essl',
    'depends': ['mail', 'product'],
    'description': """Hospital Management process""",
    'data': [
        'security\ir.model.access.csv',
        'data\patient_tag_data.xml',
        'data\patient.tag.csv',
        'wizard\cancel_appointment_view.xml',
        'views\patient_tag_view.xml',
        'views\patient_view.xml',
        'views\ppointment_view.xml',
        'views\emale_patient_view.xml',
        'views\menu.xml',

    ],
    'qweb': [],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',

}
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
