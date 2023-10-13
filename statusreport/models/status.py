from odoo import api,fields,models,_

class status(models.Model):
    _name="status.report"
    _description ="Status Report"
    _rec_name="record"


    record = fields.Char(string='Record',default=lambda self:('New'))
    project_id =fields.Many2one("project.project",required=True,string="Project")
    to_id =fields.Many2one("res.partner",string="To")
    from_id =fields.Many2one("res.partner",string="From")
    cc_ids =fields.Many2many("res.partner",string="CC")
    pages=fields.Integer(string="Pages")
    


    date =fields.Date(string="Meeting date")
    budgetdays = fields.Integer(string="Budget Days")
    averagetime = fields.Integer(string="Average Time")
    balance = fields.Integer(string="Balance Days")
    projectstatus = fields.Char(string="Current project status")
    psr = fields.Text(string="PSR")
    
    project_dates_ids= fields.One2many('project.dates.lines','project_dates_line_id',string="Project Dates")

    client_resolution_lines_ids = fields.One2many('client.resolution.report.lines','resolution_line_client_id',string="Resolution By Client")
    company_resolution_lines_ids = fields.One2many('company.resolution.report.lines','resolution_line_company_id',string="Resolution By Company")
    

    client_activity_lines_ids = fields.One2many('client.activity.report.lines','activity_line_client_id',string="Activity By Client")
    company_activity_lines_ids = fields.One2many('company.activity.report.lines','activity_line_company_id',string="Activity By Company")
    activity_from_date=fields.Date(string="Activity From Date")
    activity_to_date=fields.Date(string="Activity To Date")


    client_activity_scheduled_lines_ids = fields.One2many('client.activity.scheduled.report.lines','scheduled_activity_line_client_id',string="Scheduled Activity By Client")
    company_activity_scheduled_lines_ids = fields.One2many('company.activity.scheduled.report.lines','scheduled_activity_line_company_id',string="Scheduled Activity By Company")
    activity_scheduled_from_date=fields.Date(string="Scheduled Activity From Date")
    activity_scheduled_to_date=fields.Date(string="Scheduled Activity To Date")


    project_mitigation_lines_ids = fields.One2many('project.mitigation.lines','project_risk_mitigation_plan_lines_id',string="Project Risk Mitigation Plan")


    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            vals['record']=self.env['ir.sequence'].next_by_code('reportseq')
        return super (status,self).create(vals_list)
    
    @api.onchange('budgetdays','averagetime')
    def _onchange_balance (self):
        if self.budgetdays and self.averagetime:
            self.balance=(self.budgetdays) - (self.averagetime)
        else:
            self.balance=0




