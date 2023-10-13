from odoo import api,fields,models,_

class Xlreport(models.TransientModel):
    _name="xlreport.report"

    from_date = fields.Datetime(string='From Date')
    to_date = fields.Datetime(string='To Date')
    customer_ids=fields.Many2many('res.partner',string="Customer")

    def action_wizard_submit(self):
        domain=[]
        cust_id=self.customer_ids
        
        if cust_id:
            domain+=[('partner_id','in',cust_id.ids)]
        date_from=self.from_date
        if date_from:
            domain+=[('date_order','>=',date_from)]
        date_to=self.to_date
        if date_to:
            domain+=[('date_order','<=',date_to)]

        sale_orders=self.env['sale.order'].search(domain)
        
        data={
            'sale_order':sale_orders.ids,

            'form_data':self.read()[0]
        }
        return self.env.ref('xl_report.report_sale_order_report').report_action(self,data=data)