# -*- coding: utf-8 -*-
# from odoo import http


# class MyCustomModule(http.Controller):
#     @http.route('/ab_odoo_inheritance/ab_odoo_inheritance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ab_odoo_inheritance/ab_odoo_inheritance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ab_odoo_inheritance.listing', {
#             'root': '/ab_odoo_inheritance/ab_odoo_inheritance',
#             'objects': http.request.env['ab_odoo_inheritance.ab_odoo_inheritance'].search([]),
#         })

#     @http.route('/ab_odoo_inheritance/ab_odoo_inheritance/objects/<model("ab_odoo_inheritance.ab_odoo_inheritance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ab_odoo_inheritance.object', {
#             'object': obj
#         })
