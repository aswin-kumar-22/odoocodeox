from odoo import api,fields,models,_

class Stages(models.Model):
    _name="mom.stages"

    sequence=fields.Integer(string='sequence' ,default="1" )
    name=fields.Char(string="Name")
    is_won=fields.Boolean(string="Is won")
    fold = fields.Boolean(string="Folded in pipeline")
    is_default=fields.Boolean(string="Is Default Stage")
    # butt_id=fields.Many2one('mom.mom',string="Button ID")