vagrant up
task runs a python script to generate inventories
task run ansible playbook to create tunnel

in order to ru this
switch to WSL (ubuntu-22.04)
follow https://blog.thenets.org/how-to-run-vagrant-on-wsl-2/
install plugin vagrant-vbguest https://github.com/dotless-de/vagrant-vbguest/issues/56
set permissions on SSH key https://github.com/hashicorp/vagrant/issues/8742
set env var: export VAGRANT_WSL_WINDOWS_ACCESS_USER_HOME_PATH="/mnt/c/temp/{directory of vagrant file}"

then python venv
sudo apt install python3.10-venv
python3 -m venv ./venv
source ./venv/bin/activate

and install jinja2
pip install jinja2 

creds: 
root/opnsense

then vagrant destroy