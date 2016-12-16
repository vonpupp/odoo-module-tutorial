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
- [ ] Add coverage
- [ ] Add code quality
- [ ] Functional test
- [ ] HTML5 layer on top of the JSONRPC API
