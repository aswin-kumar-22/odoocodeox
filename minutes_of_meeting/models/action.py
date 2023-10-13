from odoo import api,fields,models,_

class Action(models.Model):
    _name = "mom.action"

    action = fields.Char(string='Action Plan')
    deadline = fields.Date(string='Dead Line')
    action_plan_id = fields.Many2one('mom.mom',string='Action Id')
    