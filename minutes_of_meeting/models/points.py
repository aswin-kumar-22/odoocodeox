from odoo import api,fields,models,_

class Points(models.Model):
    _name = "mom.points"

    points = fields.Char(string='Points Discussed')
    mom_id = fields.Many2one('mom.mom',string='Point Id')
    