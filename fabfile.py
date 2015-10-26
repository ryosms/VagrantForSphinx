from fabric.api import run, env, cd

env.hosts = ['127.0.0.1:2200']
env.user = 'vagrant'
env.password = 'vagrant'


def make(dir="/vagrant"):
    with cd(dir):
        run("make html")


def clean(dir="/vagrant"):
    with cd(dir):
        run("make clean")


def clean_make(dir="/vagrant"):
    with cd(dir):
        run("make clean")
        run("make html")
