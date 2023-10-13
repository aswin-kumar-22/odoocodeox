from odoo import models

class Salexlsx(models.AbstractModel):
    _name="report.xl_report.report_order_xls"
    _inherit="report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, lines,):
        # print("wwwwwwwwwwwwwwwwww",data['sale_order'])
        sheet=workbook.add_worksheet('Sale Order')
        

        heading_format = workbook.add_format({
            'bold':True,
            'align':'center',
            'bg_color':'#bfbfbf',
            'valign':'vcenter',
            'font_size':'20',
            'border':1
        })

        head_format = workbook.add_format({
            'bold':True,
            'align':'center',
            'bg_color':'#d9d9d9',
            'valign':'vcenter',
            'border':1
        })
        body_format=workbook.add_format({'bold':False,
            'align':'center',
            'bg_color':'#f2f2f2',
            'valign':'vcenter',
            'border':1})

        row=0
        col=0
        sheet.merge_range(row,col,row+1,col+2,'Sale Order Details',heading_format)
        sheet.set_row(2,25)
        sheet.set_column('A:A',20)
        sheet.set_column('B:B',25)
        sheet.set_column('C:C',25)

        row=2
        col=0
        sheet.write(row,col,'Customer',head_format)
        sheet.write(row,col+1,'Order',head_format)
        sheet.write(row,col+2,'Amount',head_format)

        orders = self.env['sale.order'].browse(data['sale_order'])
        customers = orders.mapped('partner_id')
        row+=1
        for customer in customers:
            customer_orders = orders.filtered(lambda ord: ord.partner_id == customer)
            if len(customer_orders) > 1:
                sheet.merge_range(row,col,row+len(customer_orders)-1,col,customer.name,body_format)
            else:
                sheet.write(row,col,customer.name,body_format)
            for corder in customer_orders:
                sheet.write(row,col+1,corder.name,body_format)
                sheet.write(row,col+2,corder.amount_total,body_format)
                row +=1

           