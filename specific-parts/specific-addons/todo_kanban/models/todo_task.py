# -*- coding: utf-8 -*-
# Copyright 2017 vonpupp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class TodoTask(models.Model):
    _inherit = 'todo.task'
    color = fields.Integer('Color index')
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'High')],
        'Priority', default='1')
    kanban_state = fields.Selection(
        [('normal', 'In Progress'),
         ('blocked', 'Bloqued'),
         ('done', 'Ready for next stage')],
        'Kanban State', default='normal')
