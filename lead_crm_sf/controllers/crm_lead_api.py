from odoo import http
from odoo.http import request

class CrmLeadApi(http.Controller):

    @http.route('/api/crm/lead', auth='none', type='json', methods=['POST'], csrf=False)
    def create_lead(self, **payload):
        api_key = request.httprequest.headers.get('X-API-KEY')
        if not api_key or not request.env['api.key'].sudo().search([('key', '=', api_key)]):
            return {'error': 'Invalid API Key'}

        lead = request.env['crm.lead'].sudo().create({
            'name': payload.get('name'),
            'contact_name': payload.get('contact_name'),
            'email_from': payload.get('email'),
            'phone': payload.get('phone'),
            'description': payload.get('description'),
        })
        return {'id': lead.id}
