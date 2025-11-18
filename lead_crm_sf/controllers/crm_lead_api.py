from odoo import http
from odoo.http import request

class CrmLeadApi(http.Controller):

    @http.route('/api/crm/lead', auth='none', type='json', methods=['POST'], csrf=False)
    def create_lead(self, **payload):
        api_key = request.httprequest.headers.get('X-API-KEY')
        if not api_key or not request.env['api.key'].sudo().search([('key', '=', api_key)]):
            return {'error': 'Invalid API Key'}

        user = request.env.ref('base.user_admin')
        env = request.env['crm.lead'].with_user(user).sudo()

        lead = env.create({
            'name': payload.get('name') or 'Lead desde API',
            'contact_name': payload.get('contact_name'),
            'email_from': payload.get('email'),
            'phone': payload.get('phone'),
            'description': payload.get('description'),
        })

        return {'id': lead.id}
