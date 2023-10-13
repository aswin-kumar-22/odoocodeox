from odoo import api,fields,models,_

class Companyjob(models.Model):
    _name = "company.job"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description ="Job Record"
    _rec_name ='ref'

    name = fields.Char(string='Name',required=True,tracking=True)
    ref = fields.Char(string="Reference",default=lambda self:_('New'))
    active =fields.Boolean(default=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref']=self.env['ir.sequence'] .next_by_code('Jobsequence')
        return super (Companyjob,self).create(vals_list)
    
    def name_get(self):
        res =[]
        for rec in self:
            res.append((rec.id,f'{rec.ref}-{rec.name}'))
        return res