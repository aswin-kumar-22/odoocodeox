from odoo import api,fields,models,_

class Project_report_lines_company(models.Model):
    _name="project.mitigation.lines"
    _description ="Company Report Lines"

    project_risk_mitigation_plan_lines_id=fields.Many2one('status.report' )
    risk_identified_date =fields.Date(string="Risk Identified Date")
    risk_identified_stage =fields.Char(string="Risk Identified Stage")
    risk_mitigation_date =fields.Date(string="Risk Mitigation Date")
    risk_decs =fields.Text(string="Risk Decs")
    impact=fields.Text(string="Impact")
    severity =fields.Char(string="Severity")
    suggested_mitigation =fields.Text(string="Suggested Mitigation")
    sponsibility =fields.Text(string="Sponsibility")
    status =fields.Char(string="Status")
    action_initiated =fields.Text(string="Action Initiated")
