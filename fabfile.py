import os
import time

from fabric.api import local, lcd, settings
from fabric.utils import puts

#If no local_settings.py then settings.py
try:
    from publishconf import OUTPUT_PATH
    SETTINGS_FILE = "publishconf.py"
except ImportError:
    from pelicanconf import OUTPUT_PATH
    SETTINGS_FILE = "pelicanconf.py"


# Get directories
ABS_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ABS_SETTINGS_FILE = os.path.join(ABS_ROOT_DIR, SETTINGS_FILE)
ABS_OUTPUT_PATH = os.path.join(ABS_ROOT_DIR, OUTPUT_PATH)


# Commands
def generate(output=None):
    """Generates the pelican static site"""

    if not output:
        cmd = "pelican -v -s {0}".format(ABS_SETTINGS_FILE)
    else:
        cmd = "pelican -v -s {0} -o {1}".format(ABS_SETTINGS_FILE, output)

    local(cmd)


def destroy(output=None):
    """Destroys the pelican static site"""

    if not output:
        cmd = "rm -r {0}".format(os.path.join(ABS_ROOT_DIR, OUTPUT_PATH))
    else:
        cmd = "rm -r {0}".format(output)

    with settings(warn_only=True):
        result = local(cmd)
    if result.failed:
        puts("Already deleted")


def serve():
    """Serves the site in the development webserver"""
    print(ABS_OUTPUT_PATH)
    with lcd(ABS_OUTPUT_PATH):
        local("python -m SimpleHTTPServer")


def git_change_branch(branch):
    """Changes from one branch to other in a git repo"""
    local("git checkout {0}".format(branch))


def git_merge_branch(branch):
    """Merges a branch in other branch"""
    local("git merge {0}".format(branch))


def s3_push(bucket):
    """Pushes the git changes to the S3 bucket."""
    with lcd(ABS_OUTPUT_PATH):
        local("s3cmd sync . s3://{0}".format(bucket))


def git_commit_all(msg):
    """Commits all the changes"""
    local("git add .")
    local("git commit -m \"{0}\"".format(msg))


def publish():
    """Generates and publish the new site in Amazon S3"""
    master_branch = "master"
    publish_branch = "s3-pages"
    bucket = "xrpblog"
    remote = "origin"

    # Push original changes to master
    push(remote, master_branch)

    # Change to gh-pages branch
    # git_change_branch(publish_branch)

    # Merge master into gh-pages
    # git_merge_branch(master_branch)

    # Generate the html
    generate(ABS_ROOT_DIR)

    # Commit changes
    # now = time.strftime("%d %b %Y %H:%M:%S", time.localtime())
    # git_commit_all("Publication {0}".format(now))

    # Push to gh-pages branch
    #git_push(remote, publish_branch)
    s3_push(bucket)

    # go to master
    git_change_branch(master_branch)
