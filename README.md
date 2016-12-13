# ODOO MODULE TUTORIAL

Example on how to [build a module based on v10]

[build a module based on v10]: https://www.odoo.com/documentation/10.0/howtos/backend.html

## Creating a development environment using virtualbox

```
# Start the VM
vagrant up

# Bootstrap
./bootstrap-ubuntu-xenial.sh

# Create a virtualenv locally
virtualenv . --system-site-packages

# Upgrade and install buildbot
bin/pip install -U pip zc.buildout

# Create config files
printf "[buildout]\n\nextends = https://raw.githubusercontent.com/odoo-brazil/odoo-brazil-buildout/10.0/default.cfg" >> common.cfg
printf "[buildout]\n\nextends = common.cfg" >> buildout.cfg

# Run buildout
bin/buildout

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
- [ ] Create a module
- [ ] Unit test
- [ ] Travis
- [ ] Functional test
