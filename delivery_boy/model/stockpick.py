from odoo import api,fields,models,_

class Stockpick(models.Model):
    _inherit='stock.picking'


    def showwizard(self):
        return{
            'name':_("Delivery Boy"),
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'delivery.wizard',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context':{'default_pick_id':self.id}
        }


