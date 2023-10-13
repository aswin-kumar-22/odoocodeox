from odoo import api,fields,models,_


LOCKED_FIELD_STATES = {
    state: [('readonly', True)]
    for state in {'done', 'cancel'}
}


class Deliverycharge(models.Model):
    _inherit ="sale.order"

    d_charge=fields.Integer(string="Delivery Charge")
    order_line=fields.One2many()
    order_line_2 = fields.One2many(comodel_name='sale.order.line',
        inverse_name='order_id',
        string="Order Lines",
        states=LOCKED_FIELD_STATES,
        copy=True, auto_join=True ,domain=[('is_change','=',False)])


    @api.onchange('d_charge')
    def delivery_charge(self): 
        delivery=self.order_line.filtered(lambda line: line.is_change)
        if delivery:
            delivery.price_unit=self.d_charge
        else:
            template = self.env['product.template'].search([('is_dproduct','=',True)])      
            self.order_line=[(0,0,{
                'product_id': template.product_variant_id.id,
                'product_template_id': template.id,
                'price_unit':self.d_charge,
                'product_uom_qty':1,
                'product_uom':1,
                'name':'charged',
                'is_change':True
            })]

    

    

class linebool(models.Model):
    _inherit="sale.order.line"

    is_change=fields.Boolean(string="Is changed",default=False)
    

class Productbool(models.Model):
    _inherit="product.template"

    is_dproduct=fields.Boolean(string="Is Delivery Charge",default=False)


