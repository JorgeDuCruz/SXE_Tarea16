# -*- coding: utf-8 -*-
# from odoo import http


# class FidelizacionClientes(http.Controller):
#     @http.route('/fidelizacion__clientes/fidelizacion__clientes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fidelizacion__clientes/fidelizacion__clientes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fidelizacion__clientes.listing', {
#             'root': '/fidelizacion__clientes/fidelizacion__clientes',
#             'objects': http.request.env['fidelizacion__clientes.fidelizacion__clientes'].search([]),
#         })

#     @http.route('/fidelizacion__clientes/fidelizacion__clientes/objects/<model("fidelizacion__clientes.fidelizacion__clientes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fidelizacion__clientes.object', {
#             'object': obj
#         })

