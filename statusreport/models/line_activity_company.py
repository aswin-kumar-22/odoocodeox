from odoo import api,fields,models,_

class Project_report_lines_client(models.Model):
    _name="company.activity.report.lines"
    _description ="Company Report Lines"

    activity_line_company_id=fields.Many2one('status.report' )
    date =fields.Date(string="Date")
    activity =fields.Char(string="Activity")
    consultant =fields.Char(string="Consultant")
    planed_effect =fields.Integer(string="Planed Effort (In Hrs)")
    actual_effect =fields.Integer(string="Actual Effort (In Hrs)")
    planed_status =fields.Char(string="Planed Status")
    actual_status =fields.Char(string="Actual Status")
    remarks =fields.Char(string="Remarks")