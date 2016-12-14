# ODOO MODULE TUTORIAL

Example on how to [build a module based on v10]

[build a module based on v10]: https://www.odoo.com/documentation/10.0/howtos/backend.html

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
bin/start_odoo -d ubuntu -u openacademy --stop-after-init
```


## Roadmap

- [X] Use buildout
- [ ] Create a basic module skeleton
- [ ] Create first test
- [ ] Travis
- [ ] Use TDD
- [ ] Functional test
