from odoo import api,fields,models,_

class DeliveryBoy(models.Model):
    _name = "delivery.boy"
    _inherit = ['mail.thread','mail.activity.mixin']


    ref = fields.Char(string="Reference",default=lambda self:_('New'))
    name= fields.Char(string="Delivery Boy")
    delivery_charge=fields.Integer(string="Delivery Charge")
    active =fields.Boolean(default=True)
    


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref']=self.env['ir.sequence'] .next_by_code('deliveryboyseq')
        return super (DeliveryBoy,self).create(vals_list)
    