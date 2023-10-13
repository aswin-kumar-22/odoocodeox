from odoo import api,fields,models,_
from odoo.exceptions import UserError

class Mom(models.Model):
    _name = "mom.mom"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ="M.O.M"
    _rec_name = "ref"


    project_id =fields.Many2one("project.project",string="Project"  )
    ref = fields.Char(string="Reference",default=lambda self:_('New') )
    meeting_date = fields.Date(string="Meeting Date" )
    meeting_place = fields.Char(string="Meeting Place" )
    duration = fields.Float(string="Meeting Duration" )
    meeting_purpose = fields.Char(string="Meeting Purpose" )
    att_name_ids = fields.One2many('mom.attendees', 'mom_id',string="Attendees" )
    points_ids = fields.One2many('mom.points' ,'mom_id',string="Points Discussed" )
    action_ids = fields.One2many('mom.action' ,'action_plan_id',string="Action Plan" )
    active =fields.Boolean(default=True)
    # but_invi_ids=fields.One2many('mom.stages','butt_id',string="Button Invisible")
    action_confirm_visible=fields.Boolean(string="won is", compute='_compute_button_invisible',default=True)
    stage_id=fields.Many2one('mom.stages',string="Stages", compute='_compute_stage_id', store=True, readonly=False
                             ,index=True, Tracking=True, copy=False, ondelete='restrict')
    
    

    @api.depends('stage_id')
    def _compute_button_invisible(self):
        if self.stage_id.is_won==True:
            self.action_confirm_visible=False
        else:
            self.action_confirm_visible=True


    def _compute_stage_id(self):
        for rec in self:
            if not rec.stage_id:
                rec.stage_id=rec._stage_find(domain=[('fold','=',False)]).id
   
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref']=self.env['ir.sequence'] .next_by_code('momseq')
        return super (Mom,self).create(vals_list)
    

    @api.model
    def default_get(self, fields_list):
        vals=super(Mom,self).default_get(fields_list)
        default_stage=self.env['mom.stages'].search([('is_default','=',True)],limit=1)
        if not default_stage:
            raise UserError(_("Default stage not found"))
        vals['stage_id']=default_stage.id
        return vals
    
    def action_confirm(self):
        rec=self.env['mom.stages'].search([('is_won', '=', True)])
        self['stage_id']=rec.id
        


        
        