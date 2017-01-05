# ODOO MODULE TUTORIAL

Example on how to [build a module based on v10]

[build a module based on v10]: https://www.odoo.com/documentation/10.0/howtos/backend.html

[![Travis-CI](https://img.shields.io/travis/vonpupp/odoo-module-tutorial.svg)](https://travis-ci.org/vonpupp/odoo-module-tutorial)
[![Codecov](https://img.shields.io/codecov/c/github/vonpupp/odoo-module-tutorial/master.svg)](https://codecov.io/gh/vonpupp/odoo-module-tutorial)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/vonpupp/odoo-module-tutorial.svg)](https://scrutinizer-ci.com/g/vonpupp/odoo-module-tutorial/)
[![Stories in
Ready](https://badge.waffle.io/vonpupp/odoo-module-tutorial.png?label=ready&title=Ready)](http://waffle.io/vonpupp/odoo-module-tutorial)
[![Stories in
progress](https://badge.waffle.io/vonpupp/odoo-module-tutorial.png?label=progress&title=Progress)](http://waffle.io/vonpupp/odoo-module-tutorial)

Throughput Graph

[![Throughput
Graph](https://graphs.waffle.io/vonpupp/odoo-module-tutorial/throughput.svg)](https://waffle.io/vonpupp/odoo-module-tutorial/metrics)


## Creating a development environment using virtualbox

```
# Start the VM
vagrant up

# ssh to the VM
vagrant ssh

# Bootstrap packages
cd /vagrant
./provision/bootstrap-packages-ubuntu-xenial.sh

# Bootstrap database
./provision/bootstrap-database.sh

# Create a virtualenv locally
./provision/bootstrap-environment.sh

# Start odoo
bin/start_odoo

# Open the browser
firefox 192.168.33.10:8069
```

## Creating a module using mrbob odoo templates

```
# Create a virtual env
virtualenv2 .venv
source .venv/bin/activate

# Install bob templates
(.venv) > $ pip2 install bobtemplates.odoo

# Create a basic addon manifest
(.venv) > $ mrbob bobtemplates.odoo:addon

--> Addon name (with underscores): todo_kanban
--> Is it an OCA addon [n]: n
--> Summary: Kanban board for to-do tasks.
--> Version [10.0.1.0.0]:
--> Copyright holder name: vonpupp
--> Copyright year: 2017
--> Website:

# Restart the server
> $ bin/start_odoo

# Update the apps via the web interface
# Install the new app


# Create a model skeleton for the app
(.venv) > $ cd todo_kanban
(.venv) todo_kanban > $ mrbob bobtemplates.odoo:model

--> Odoo version (8|9|10) [10]: 10
--> Model name (dotted notation): todo.task
--> Inherit [y]: y
--> Form view [y]: y
--> Search view [y]: y
--> Tree view [y]: y
--> Action and menu entry [y]: y
--> ACL [y]: y
--> Demo data [y]: y
--> Copyright holder name: vonpupp
--> Copyright year: 2017


# Create tests skeleton for the app
(.venv) todo_kanban > $ mrbob bobtemplates.odoo:test

--> Odoo version (8|9|10) [10]: 10
--> Test file name (with underscores): test_kanban
--> Copyright holder name: vonpupp
--> Copyright year: 2017

```

## Updating the module

```
# Update a specific module
bin/start_odoo -d ubuntu -u todo_app --stop-after-init

# Unit test a specific app using
bin/start_odoo -d ubuntu -i todo_app --test-enable
```


## Roadmap

- [X] Use buildout
- [X] Create a basic module skeleton
- [X] Create first test
- [X] Travis
- [X] Create a view
- [X] Use TDD
- [X] Add code quality
- [ ] Add maintainer quality tools
- [ ] Add coverage
- [ ] Tests with runbot?
- [ ] Add documentation (sphinx)
- [ ] Add UML
- [ ] Deploy
- [ ] Docker
- [ ] Functional test
- [ ] HTML5 layer on top of the JSONRPC API
- [ ] Learn to use bob templates
- [ ] Learn to user openupgrade (OCA)?
- [ ] Learn commit style
- [ ] Use odoo-bin
- [ ] Use watchdog
