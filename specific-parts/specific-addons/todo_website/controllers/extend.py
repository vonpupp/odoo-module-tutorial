# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.todo_website.controllers.main import Main

class TodoExtend(Main):

    """Extended feature from controllers/main """

    @http.route('/extended')
    def hello(self, name=None, **kwargs):
        response = super(TodoExtend, self).hello()
        response.qcontext['name'] = name
        return response
