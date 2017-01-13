#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import erppeek

# Testing the service
srv = 'http://192.168.33.10:8069'
db = 'ubuntu'
user, pwd = 'admin', 'admin'
api = erppeek.Client(srv, db, user, pwd)

# Version
result = api.common.version()
print('result = %s' % result)

# Count
result = api.count('res.partner', [])
print('result = %s' % result)

# Search
result = api.search('res.partner', [('country_id', '=', 'be'), ('parent_id', '!=', 'False')])
print('result = %s' % result)

# Read
result = api.read('res.partner', [44], ['id', 'name', 'parent_id'])
print('result = %s' % result)

# Map a model
m = api.model('res.partner')
m = api.ResPartner
result = m.count([('name', 'like', 'Agro%')])
print('result = %s' % result)
result = m.search([('name', 'like', 'Agro%')])
print('result = %s' % result)

# Client side object
recs = m.browse([('name', 'like', 'Agro%')])
print('recs = %s' % recs)
result = recs.name
print('result = %s' % result)
