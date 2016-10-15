"""
ATTENTION!!! This file has not been tested at all!
"""
import os
from contextlib import contextmanager as _contextmanager

from fabric import api
from fabric.api import env, lcd, local, run, runs_once
from fabric.context_managers import cd, prefix

api.env.hosts = ['lcrs@fair']

# NB! No trailing slashes
ENV_DIR = '/var/vhosts/lcrs/.virtualenvs/venv'
PROJECT_DIR = '/var/vhosts/lcrs/git'


def dirjoin(x):
    return os.path.join(PROJECT_DIR, x)

# Use the local .ssh/config
env.use_ssh_config = True

env.virtualenv = ENV_DIR
env.activate = 'source %(virtualenv)s/bin/activate' % env
env.code_dir = PROJECT_DIR


@_contextmanager
def virtualenv():
    with cd(env.virtualenv), prefix(env.activate), cd(env.code_dir):
        yield


def git_pull():
    """
    Pulls the latest master branch
    """

    with cd(PROJECT_DIR):
        run('git pull --ff origin master')


def syncdb():
    """
    Syncs the database
    """
    with virtualenv():
        run('python manage.py syncdb')


def migrate():
    """
    Migrates the project
    """
    with virtualenv():
        run('python manage.py migrate')


def collectstatic():
    """
    Runs collectstatic on the remote project
    """
    with virtualenv():
        run('python manage.py collectstatic --noinput')


def install():
    """
    Runs collectstatic on the remote project
    """
    with virtualenv():
        run('pip install -r requirements.txt')


def deploy():

    git_pull()
    install()
    migrate()
    api.run('touch /var/vhosts/lcrs/reload')
    register_deployment(".")
