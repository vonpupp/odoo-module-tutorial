# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Main(http.Controller):

    """Controller example for the website frontend"""

    @http.route('/todo', auth='user', website=True)
    def index(self, **kwargs):
        TodoTask = request.env['todo.task']
        tasks = TodoTask.search([])
        return request.render(
            'todo_website.index', {'tasks': tasks})

    @http.route('/todo/<model("todo.task"):task>', website=True)
    def index(self, task, **kwargs):
        return request.render(
            'todo_website.detail', {'task': task})

    @http.route('/todo/add', website=True)
    def add(self, **kwargs):
        users = request.env['res.users'].search([])
        return request.render(
            'todo_website.add', {'users': users})
