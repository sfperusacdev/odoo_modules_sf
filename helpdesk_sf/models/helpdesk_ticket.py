from odoo import fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    descripcion_solucion = fields.Html(string="Descripción de Solución")
    consumidor = fields.Char(string="Descripción de Solución")
    fecha_solicitud = fields.Datetime(string="Fecha de Solicitud")
    respuesta_usuario = fields.Html(string="Respuesta al Usuario")
    num_horas = fields.Float(string="Número de Horas")
    hora_inicio = fields.Datetime(string="Hora de Inicio")
    hora_fin = fields.Datetime(string="Hora de Finalización")
