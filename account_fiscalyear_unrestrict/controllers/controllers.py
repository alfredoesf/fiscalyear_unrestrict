# -*- coding: utf-8 -*-
from odoo import http

# class AccountFiscalyearUnrestrict(http.Controller):
#     @http.route('/account_fiscalyear_unrestrict/account_fiscalyear_unrestrict/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_fiscalyear_unrestrict/account_fiscalyear_unrestrict/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_fiscalyear_unrestrict.listing', {
#             'root': '/account_fiscalyear_unrestrict/account_fiscalyear_unrestrict',
#             'objects': http.request.env['account_fiscalyear_unrestrict.account_fiscalyear_unrestrict'].search([]),
#         })

#     @http.route('/account_fiscalyear_unrestrict/account_fiscalyear_unrestrict/objects/<model("account_fiscalyear_unrestrict.account_fiscalyear_unrestrict"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_fiscalyear_unrestrict.object', {
#             'object': obj
#         })