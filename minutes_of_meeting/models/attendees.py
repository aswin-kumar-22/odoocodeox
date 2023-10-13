from odoo import api,fields,models,_

class Attendees(models.Model):
    _name = "mom.attendees"

    employee_id = fields.Many2one('hr.employee', string='Employee')
    client_id = fields.Many2one('res.partner', string='Client')
    mom_id = fields.Many2one('mom.mom', string='MoM')
