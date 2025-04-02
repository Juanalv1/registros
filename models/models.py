from odoo import models, fields, api

class Registros(models.Model):
    _inherit = 'crm.lead'

    encargado = fields.Many2one('res.users', string="Encargado")
    med_contacto = fields.Selection([
    ('phone', 'Phone Number'),
    ('email', 'Email')
    ], default='email', string="Medio de contacto")

