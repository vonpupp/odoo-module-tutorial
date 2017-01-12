# -*- coding: utf-8 -*-
# Copyright 2017 vonpupp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Todo Website',
    'description': """
        To-do task website""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'vonpupp',
    'depends': [
        'todo_kanban',
        'website',
        'website_form'
    ],
    'data': [
        'views/todo_web.xml',
        'views/todo_templates.xml',
        'data/config_data.xml'
    ],
    'demo': [
    ],
}
