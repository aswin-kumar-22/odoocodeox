from odoo import api,fields,models,_

class Companystaff(models.Model):
    _name = "company.staff"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description ="Staff Record"
    

    name = fields.Char(string='Name',required=True,tracking=True)
    dob = fields.Date(string="Date Of Birth",tracking=True)
    age = fields.Integer(string='Age',tracking=True, compute='_compute_age',store=True)
    gender = fields.Selection([("male","Male"),("female","Female"),("other","Other")],string="Gender",tracking=True)
    ph_no = fields.Char(string="Phone Number",tracking=True)
    add = fields.Char(string="Address",tracking=True)
    doj = fields.Date(string="Date Of Joining",tracking=True)
    expi =fields.Boolean(string="Have 1 Year expirience.") 
    ref = fields.Char(string="Reference",default=lambda self:_('New'))
    job_id =fields.Many2one(comodel_name='company.job',string="Job role")
    active =fields.Boolean(default=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref']=self.env['ir.sequence'] .next_by_code('Staffsequence')
        return super (Companystaff,self).create(vals_list)

    @api.depends('dob')
    def _compute_age(self):
        for staff in self:
            if staff.dob:
                staff.age = (fields.Date.today() - staff.dob).days/364.25
            else:
                staff.age = False


    @api.onchange('doj')
    def _onchange_doj (self):
        if self.doj:
            today = fields.Date.today()
            exp = today - self.doj
            year = exp.days / 365.0
            if year >= 1:
                self.expi = True
            else:
                self.expi=False
        else:
            self.expi=False

    