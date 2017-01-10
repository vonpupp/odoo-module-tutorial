# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Todo(http.Controller):

    """Controller example for the website frontend"""

    @http.route('/hello', auth='public')
    def hello_world(self, **kwargs):
        """TODO: to be defined1. """
        return request.render('todo_website.hello')
