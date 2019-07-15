import os

name = str(raw_input("enter the first command:"))
pwd = str(raw_input("enter the second command:"))

thisdict = {
  "name": name,
  "pwd": pwd
}
cmd = 'ansible-playbook -i localhost  play.yaml -e',thisdict

view = '"{}"'.format(thisdict)

cmd = 'ansible-playbook -i localhost  play.yaml -e '

test = cmd + view

print(test)
os.system(test)
