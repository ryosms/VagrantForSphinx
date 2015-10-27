from fabric.api import run, env, cd, local


def make(dir="/vagrant", hostname="default"):
    setenv(hostname)
    with cd(dir):
        run("make html")


def clean(dir="/vagrant", hostname="default"):
    setenv(hostname)
    with cd(dir):
        run("make clean")


def clean_make(dir="/vagrant", hostname="default"):
    setenv(hostname)
    with cd(dir):
        run("make clean")
        run("make html")


def setenv(hostname="default"):
    output = local("vagrant ssh-config --host %s" % hostname, capture=True)
    for x in output.splitlines():
        config = x.strip().split(" ")
        if config[0] == "HostName":
            env.host_string = config[1]
        elif config[0] == "User":
            env.user = config[1]
        elif config[0] == "Port":
            env.port = config[1]
        elif config[0] == "IdentityFile":
            env.key_filename = config[1]
