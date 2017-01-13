#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import xmlrpclib

# Testing the service
srv = 'http://192.168.33.10:8069'
common = xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % srv)
result = common.version()

print('result = %s' % result)


# Testing authentication
db = 'ubuntu'
user, pwd = 'admin', 'admin'
uid = common.authenticate(db, user, pwd, {})

print('uid = %s' % uid)


# Reading data from the server
api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % srv)
result = api.execute_kw(db, uid, pwd, 'res.partner', 'search_count', [[]])
print('result = %s' % result)

result = api.execute_kw(db, uid, pwd, 'res.partner', 'search', [[('country_id', '=', 'be'), ('parent_id', '!=', False)]])
print('result = %s' % result)

result = api.execute_kw(db, uid, pwd, 'res.partner', 'read', [[18]], {'fields': ['id', 'name', 'parent_id']})
print('result = %s' % result)

result = api.execute_kw(db, uid, pwd, 'res.partner', 'search_read', [[('country_id', '=', 'be'), ('parent_id', '!=', False)]], {'fields': ['id', 'name', 'parent_id']})
print('result = %s' % result)

# Calling other methods
#result = api.execute_kw(db, uid, pwd, 'res.partner', 'create', [{'name': 'PacktPub'}])
#print('result = %s' % result)
#
#result = api.execute_kw(db, uid, pwd, 'res.partner', 'write', [[45], {'name': 'PacktPub'}])
#print('result = %s' % result)
#
#result = api.execute_kw(db, uid, pwd, 'res.partner', 'read', [[45], ['id', 'name']])
#print('result = %s' % result)
#
#result = api.execute_kw(db, uid, pwd, 'res.partner', 'unlink', [[45]])
#print('result = %s' % result)
