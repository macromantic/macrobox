
from fabric.api import *

env.hosts = [
    'vagrant@127.0.0.1:2222'
]

env.password = "vagrant"

@parallel
def cmd(command):
    run(command)

def scmd(command):
    sudo(command)

def osinfo():
    run("cat /etc/redhat-release")

def pyversion():
    run("python3 --version")

def djangoversion():
    run("python3 -m django --version")

def gitversion():
	run("git --version")

def clone(command):
    run("git clone https://github.com/macromantic/macroweb.git")
