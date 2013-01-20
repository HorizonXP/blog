import os
import time

from fabric.api import local, lcd, settings, run
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
        local("python -m SimpleHTTPServer 8100")


def git_change_branch(branch):
    """Changes from one branch to other in a git repo"""
    local("git checkout {0}".format(branch))


def git_merge_branch(branch):
    """Merges a branch in other branch"""
    local("git merge {0}".format(branch))


def s3_push(bucket):
    """Pushes the git changes to the S3 bucket."""
    with lcd(ABS_OUTPUT_PATH):
        local("s3cmd --delete-removed --add-header='Content-Encoding: gzip' -M -m 'text/html' sync . s3://{0}".format(bucket))

def dirEntries(dir_name, subdir, *args):
    '''Return a list of file names found in directory 'dir_name'
    If 'subdir' is True, recursively access subdirectories under 'dir_name'.
    Additional arguments, if any, are file extensions to match filenames. Matched
        file names are added to the list.
    If there are no additional arguments, all files found in the directory are
        added to the list.
    Example usage: fileList = dirEntries(r'H:\TEMP', False, 'txt', 'py')
        Only files with 'txt' and 'py' extensions will be added to the list.
    Example usage: fileList = dirEntries(r'H:\TEMP', True)
        All files and all the files in subdirectories under H:\TEMP will be added
        to the list.
    '''
    fileList = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            if not args:
                fileList.append(dirfile)
            else:
                if os.path.splitext(dirfile)[1][1:] in args:
                    fileList.append(dirfile)
        # recursively access file names in subdirectories
        elif os.path.isdir(dirfile) and subdir:
            print "Accessing directory:", dirfile
            fileList.extend(dirEntries(dirfile, subdir, *args))
    return fileList

def minify():
    """Minifies HTML, JS, and CSS in output directory."""
    fileList = dirEntries(ABS_OUTPUT_PATH, True, 'html', 'css', 'js')
    for thefile in fileList:
        local("jitify --minify {0} > {1}".format(thefile, thefile + ".min"))
    for thefile in fileList:
        local("mv {0} {1}".format(thefile + ".min", thefile))
    fileList = dirEntries(os.path.join(ABS_OUTPUT_PATH, '2012'), True, 'html')
    for thefile in fileList:
        local("mv {0} {1}".format(thefile, thefile.replace('.html', '')))
    imgList = dirEntries(os.path.join(ABS_OUTPUT_PATH, 'static'), True, 'png')
    for theImg in imgList:
        theNewImg = theImg.replace('.png', '.jpg')
        local("convert {0} {1}".format(theImg, theNewImg))
    for theImg in imgList:
        local("rm {0}".format(theImg))
    imgList = dirEntries(os.path.join(ABS_OUTPUT_PATH, 'static'), True, 'jpg')
    for theImg in imgList:
        local("mogrify -compress JPEG -quality 60 {0}".format(theImg))
    fileList = dirEntries(ABS_OUTPUT_PATH, True)
    for thefile in fileList:
        local("gzip {0}".format('"' + thefile + '"'))
    for thefile in fileList:
        local("mv {0} {1}".format('"' + thefile + '.gz' + '"', '"' + thefile + '"'))

def git_push(remote, branch):
    """Pushes the git changes to git remote repo"""
    local("git push {0} {1}".format(remote, branch))

def git_commit_all(msg):
    """Commits all the changes"""
    local("git add .")
    local("git commit -m \"{0}\"".format(msg))


def publish():
    """Generates and publish the new site in Amazon S3"""
    master_branch = "master"
    publish_branch = "s3-pages"
    bucket = "www.xitijpatel.com"
    remote = "origin"

    with lcd(ABS_OUTPUT_PATH):
        local("rm -rf *")
    # Push original changes to master
    git_push(remote, master_branch)

    # Change to gh-pages branch
    # git_change_branch(publish_branch)

    # Merge master into gh-pages
    # git_merge_branch(master_branch)

    # Generate the html
    generate(ABS_OUTPUT_PATH)
    minify()

    # Commit changes
    # now = time.strftime("%d %b %Y %H:%M:%S", time.localtime())
    # git_commit_all("Publication {0}".format(now))

    # Push to gh-pages branch
    #git_push(remote, publish_branch)
    s3_push(bucket)

    # go to master
    git_change_branch(master_branch)
