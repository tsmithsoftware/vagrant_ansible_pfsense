import subprocess
from jinja2 import Environment, FileSystemLoader

class VagrantVM:
  def __init__(self, host, hostname, user, port):
    self.host = host
    self.hostname = hostname
    self.user = user
    self.port = port

sshconfig = subprocess.run(["vagrant", "ssh-config"], capture_output=True)
sshconfig.check_returncode()
results=sshconfig.stdout.decode("utf-8")
trimmedResults=results.strip('\r\n')
myarray = trimmedResults.split("\n\n")
myvms=[]
for line in myarray:
    myvmunparsed = line.split("\n")
    host=""
    hostname=""
    user=""
    port=""
    for vmvalue in myvmunparsed:
        trimmedValue=vmvalue.lstrip() # remove tabs
        list=trimmedValue.split(" ")
        key = list[0]
        value = list[1]
        if(key == "Host"):
           host=value
        if(key == "HostName"):
           hostname=value
        if(key == "User"):
           user=value
        if(key == "Port"):
           port=value
    
    myVm=VagrantVM(host=host, hostname=hostname, user=user, port=port)
    myvms.append(myVm)

print(str(len(myvms)) + " VM objects created!")
print("Creating Ansible inventory...")

environment = Environment(loader=FileSystemLoader(""))
template = environment.get_template("inventory_template.txt")
firstvm = myvms[0]
secondvm = myvms[1]

firstVmString=f"{firstvm.host} ansible_ssh_host={firstvm.hostname} ansible_port={firstvm.port}"
secondVmString=f"{secondvm.host} ansible_ssh_host={secondvm.hostname} ansible_port={secondvm.port}"

content = template.render(
    user=user,
    host1=firstVmString,
    host2=secondVmString
)

filename=f"inventory_gen.ini"

with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
    print("write")