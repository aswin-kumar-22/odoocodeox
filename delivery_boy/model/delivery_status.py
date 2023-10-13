from odoo import api,fields,models,_
from datetime import date

class Deliverystatus(models.Model):
    _name="delivery.status"
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name="pref"

    pref = fields.Char(string="Reference",default=lambda self:_('New'))
    name_id=fields.Many2one("delivery.boy",string="Delivery Boy Name")
    pick_id =fields.Many2one("stock.picking",string="Pick Id")
    date=fields.Date(string="Scheduled Date")
    d_date=fields.Date(string="Delivery Date")
    address_id=fields.Many2one("res.partner",string="Address")
    delivery_charge_id=fields.Many2one("delivery.boy",string="Delivery Charge")
    extra_charge=fields.Integer(string="Extra Delivery charge")
    t_delivery_charge=fields.Integer(string="Total Delivery Charge")

    state = fields.Selection([
        ('draft','Out for Delivery'),
        ('deliverd','Deliverd'),
    ],string="Status",default="draft")
   


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['pref']=self.env['ir.sequence'] .next_by_code('pickingseq')
        return super (Deliverystatus,self).create(vals_list)
    
    def action_confirm(self):
        for res in self:
            res.state='deliverd'
            res.d_date = date.today()

    


