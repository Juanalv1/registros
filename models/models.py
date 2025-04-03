from odoo import models, fields, api
from datetime import timedelta, datetime
from odoo.tools import date_utils
from odoo.exceptions import ValidationError


class Registros(models.Model):
    _inherit = 'crm.lead'

    encargado = fields.Many2one('res.users', string="Encargado")
    med_contacto = fields.Selection([
    ('phone', 'Phone Number'),
    ('email', 'Email')
    ], default='email', string="Medio de contacto")

    deadline_valid = fields.Boolean(
        string="Deadline Valid",
        compute="_compute_deadline_valid",
        store=True
    )

    @api.constrains('date_deadline')
    def _check_deadline_date(self):
        for record in self:
            if record.date_deadline < fields.Date.today():
                raise ValidationError("La fecha de cierre no puede ser menor a la fecha actual")


    @api.depends('date_deadline')
    def _compute_deadline_valid(self):
        today = fields.Date.today()
        print('today', today)
        sub_day = date_utils.subtract(today, days=2)
        print(sub_day)
        for record in self:
        # Compara solo las fechas, sin tener en cuenta las horas
            print("comparacion", record.date_deadline and record.date_deadline >= 
                  
                  sub_day)
            record.deadline_valid = record.date_deadline and record.date_deadline >= sub_day
