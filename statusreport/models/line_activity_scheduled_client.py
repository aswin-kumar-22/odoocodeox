from odoo import api,fields,models,_

class Project_report_lines_client(models.Model):
    _name="client.activity.scheduled.report.lines"
    _description ="Client Activity Scheduled Report Lines"

    scheduled_activity_line_client_id=fields.Many2one('status.report' )
    date =fields.Date(string="Date")
    activity =fields.Char(string="Activity")
    process_owner =fields.Char(string="Process Owner")
    planed_status =fields.Char(string="Planed Status")
    remarks =fields.Char(string="Remarks")