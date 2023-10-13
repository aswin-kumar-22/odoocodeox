from odoo import api,fields,models,_

class Project_report_lines_company(models.Model):
    _name="company.resolution.report.lines"
    _description ="Company Report Lines"

    resolution_line_company_id=fields.Many2one('status.report' )
    issue =fields.Text(string="Issue")
    impact =fields.Text(string="Impact")
    respossibility =fields.Text(string="Responsibility")
    resolution_required_by =fields.Date(string="Resolution Required By")
    action_plan=fields.Text(string="Action Plan")
    age_in_days =fields.Integer(string="Age In Days")