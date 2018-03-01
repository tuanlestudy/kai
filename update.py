import os

sudo_install = 'sudo apt-get install '
sudo = 'sudo apt '

print(sudo_install+'update -y')
os.system(sudo_install+'update -y')
print(sudo_install+'upgrade -y')
os.system(sudo_install+'upgrade -y')
print(sudo + 'autoremove -y')
os.system(sudo + 'autoremove -y')
print(sudo + 'autoclean -y')
os.system(sudo + 'autoclean -y')