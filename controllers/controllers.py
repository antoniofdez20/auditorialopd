# -*- coding: utf-8 -*-
#from odoo import http

#class Auditorialopd(http.Controller):
#     @http.route('/auditorialopd/auditorialopd', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/auditorialopd/auditorialopd/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('auditorialopd.listing', {
#             'root': '/auditorialopd/auditorialopd',
#             'objects': http.request.env['auditorialopd.auditorialopd'].search([]),
#         })

#     @http.route('/auditorialopd/auditorialopd/objects/<model("auditorialopd.auditorialopd"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('auditorialopd.object', {
#             'object': obj
#         })

