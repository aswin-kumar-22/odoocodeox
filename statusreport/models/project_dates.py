from odoo import api,fields,models,_

class Project_report_lines_client(models.Model):
    _name="project.dates.lines"
    _description ="Project Dates Lines"

    project_dates_line_id=fields.Many2one('status.report' )
    project_name =fields.Char(string="Project Name")
    project_start_date =fields.Date(string="Project Start Date")
    orginal_live_date =fields.Date(string="Orginal Live Date ")
    revised_live_date =fields.Date(string="Revised Live Date ")
    orginal_completion_date =fields.Date(string="Orginal Completion Date")
    exp_project_completion_date =fields.Date(string="Exp Project Completion Date")
