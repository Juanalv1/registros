# -*- coding: utf-8 -*-
# from odoo import http


# class Registros(http.Controller):
#     @http.route('/registros/registros', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/registros/registros/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('registros.listing', {
#             'root': '/registros/registros',
#             'objects': http.request.env['registros.registros'].search([]),
#         })

#     @http.route('/registros/registros/objects/<model("registros.registros"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('registros.object', {
#             'object': obj
#         })

