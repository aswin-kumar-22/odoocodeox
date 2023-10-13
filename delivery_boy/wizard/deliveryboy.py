from odoo import api ,fields,models ,_

class Wizard_delivery_boy(models.TransientModel):
    _name="delivery.wizard"

    name_id=fields.Many2one('delivery.boy',string="Name")
    pick_id =fields.Many2one("stock.picking",string="Pick Id")



    def action_wizard_submit(self):
        self.env['delivery.status'].create({
            'name_id':self.name_id.id,
            'pick_id':self.pick_id.id,
            'date':self.pick_id.scheduled_date,
            'address_id':self.pick_id.partner_id.id,
        })
        return