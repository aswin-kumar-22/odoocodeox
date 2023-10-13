from odoo import api,fields,models,_

class Project_report_lines_client(models.Model):
    _name="client.resolution.report.lines"
    _description ="Client Report Lines"

    resolution_line_client_id=fields.Many2one('status.report' )
    issue =fields.Text(string="Issue")
    impact =fields.Text(string="Impact")
    respossibility =fields.Text(string="Responsibility")
    resolution_required_by =fields.Date(string="Resolution Required By")
    age_in_days =fields.Integer(string="Age In Days")