# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import Warning
from datetime import date
from odoo import fields


class TestWizard(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestWizard, self).setUp(*args, **kwargs)
        # Close any open Todo task
        self.env['todo.task']\
            .search([('is_done', '=', False)])\
            .write({'is_done': True})
        # Demo user will be used to run tests
        demo_user = self.env.ref('base.user_demo')
        # Create two todo tasks to use in tests
        t0 = date.today()
        Todo = self.env['todo.task'].sudo(demo_user)
        self.todo1 = Todo.create({
            'name': 'Todo1',
            'date_deadline': fields.Date.to_string(t0)
        })
        self.todo2 = Todo.create({
            'name': 'Todo2'
        })

    def test_populate_tasks(self):
        "Populate tasks button should add two tasks"
        self.wizard.do_populate_tasks()
        count = len(self.wizard.task_ids)
        self.assertEqual(count, 2, 'Wrong number of populated tasks')

    def test_mass_change(self):
        "Mass change deadline date"
        self.wizard.do_populate_tasks()
        self.wizard.new_deadline = self.todo1.date_deadline
        self.wizard.do_mass_update()
        self.assertEqual(
            self.todo1.date_deadline,
            self.todo2.date_deadline)

    def test_count(self):
        "Test count button"
        with self.assertRaises(Warning) as e:
            self.wizard.do_count_tasks()
        self.assertIn(' 2 ', str(e.exception))
