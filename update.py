import subprocess
sudo_install = 'sudo apt-get install '
sudo = 'sudo apt '
result = subprocess.run([sudo_install + 'update', '-y'], stdout=subprocess.PIPE)
result.stdout
result = subprocess.run([sudo_install + 'upgrade', '-y'], stdout=subprocess.PIPE)
result.stdout
result = subprocess.run([sudo + 'autoremove', '-y'], stdout=subprocess.PIPE)
result.stdout
result = subprocess.run([sudo + 'autoclean', '-y'], stdout=subprocess.PIPE)
result.stdout