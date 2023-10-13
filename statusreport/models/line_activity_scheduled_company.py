from odoo import api,fields,models,_

class Project_report_lines_client(models.Model):
    _name="company.activity.scheduled.report.lines"
    _description ="Company Report Lines"

    scheduled_activity_line_company_id=fields.Many2one('status.report' )
    date =fields.Date(string="Date")
    activity =fields.Char(string="Activity")
    consultant =fields.Char(string="Consultant")
    planed_effect =fields.Integer(string="Planed Effort (In Hrs)")
    planed_status =fields.Char(string="Planed Status")
    remarks =fields.Char(string="Remarks")