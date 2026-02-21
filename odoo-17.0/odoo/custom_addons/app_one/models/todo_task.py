from odoo import models, fields, api
from datetime import date

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To Do Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # مهم

    reference = fields.Char(
        string="Task ID",
        required=True,
        copy=False,
        readonly=True,
        default="New"
    )

    name = fields.Char(string='Task Name', required=True)
    assign_to = fields.Many2one('res.users', string="Assign To")
    description = fields.Text(string="Description")
    due_date = fields.Date(string="Due Date", required=True)
    status = fields.Selection([
        ('new', 'New'),
        ('progress', 'In Progress'),
        ('done', 'Completed')
    ], string="Status", default='new', tracking=True)

    deadline_state = fields.Selection([
        ('normal', 'Normal'),
        ('due_soon', 'Due Soon'),
        ('late', 'Late')
    ], compute="_compute_deadline_state", store=True)

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            vals['reference'] = self.env['ir.sequence'].next_by_code('todo.task') or 'New'
        return super(TodoTask, self).create(vals)

    @api.depends('due_date')
    def _compute_deadline_state(self):
        today = date.today()
        for record in self:
            if not record.due_date:
                record.deadline_state = 'normal'
            elif record.due_date < today:
                record.deadline_state = 'late'
            elif (record.due_date - today).days <= 2:
                record.deadline_state = 'due_soon'
            else:
                record.deadline_state = 'normal'
