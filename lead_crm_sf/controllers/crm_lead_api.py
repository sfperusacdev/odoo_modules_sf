from odoo import http
from odoo.http import request

class CrmLeadApi(http.Controller):

    @http.route('/api/crm/lead', auth='none', type='json', methods=['POST'], csrf=False)
    def create_lead(self, **kw):
        data = request.jsonrequest

        api_key = request.httprequest.headers.get('X-API-KEY')
        if not api_key or not request.env['api.key'].sudo().search([('key', '=', api_key)]):
            return {'error': 'Invalid API Key'}

        user = request.env.ref('base.user_admin')
        env = request.env['crm.lead'].with_user(user).sudo()

        lead = env.create({
            'name': data.get('name') or 'Lead desde API',
            'contact_name': data.get('contact_name'),
            'email_from': data.get('email'),
            'phone': data.get('phone'),
            'description': data.get('description'),
        })

        return {'id': lead.id}
