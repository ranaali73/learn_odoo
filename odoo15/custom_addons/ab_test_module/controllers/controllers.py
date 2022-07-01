# -*- coding: utf-8 -*-
# from odoo import http


# class AbTestModule(http.Controller):
#     @http.route('/ab_test_module/ab_test_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ab_test_module/ab_test_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ab_test_module.listing', {
#             'root': '/ab_test_module/ab_test_module',
#             'objects': http.request.env['ab_test_module.ab_test_module'].search([]),
#         })

#     @http.route('/ab_test_module/ab_test_module/objects/<model("ab_test_module.ab_test_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ab_test_module.object', {
#             'object': obj
#         })
