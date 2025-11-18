from odoo import http
from odoo.http import request
import json

class CrmLeadApi(http.Controller):

    @http.route('/api/crm/lead', auth='public', methods=['POST'], csrf=False)
    def create_lead(self):
        api_key = request.httprequest.headers.get('X-API-KEY')
        if not api_key or not request.env['api.key'].sudo().search([('key', '=', api_key)]):
            return request.make_json_response({"error": "Invalid API Key"}, status=401)

        try:
            data = json.loads(request.httprequest.data.decode('utf-8'))
        except:
            return request.make_json_response({"error": "Invalid JSON"}, status=400)

        user = request.env.ref('base.user_admin')
        env = request.env['crm.lead'].with_user(user).sudo()

        lead = env.create({
            'name': data.get('name') or 'Lead desde API',
            'contact_name': data.get('contact_name'),
            'email_from': data.get('email'),
            'phone': data.get('phone'),
            'description': data.get('description'),
        })

        return request.make_json_response({"id": lead.id})
