{
    'name': 'CRM Lead Endpoint',
    'version': '1.0',
    'summary': 'Habilita un endpoint para pre-registrar leads en CRM',
    'category': 'CRM',
    'author': 'SF PERU SAC',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'view/view.xml'
    ],
    'installable': True,
}
