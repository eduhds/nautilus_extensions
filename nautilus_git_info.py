from gi.repository import Nautilus, GObject
from urllib.parse import urlparse, unquote
from subprocess import call, STDOUT
import os

git_file_status = [
    # ' ',  # unmodified
    'M',  # modified
    'T',  # file type changed (regular file, symbolic link or submodule)
    'A',  # added
    'D',  # deleted
    'R',  # renamed
    'C',  # copied (if config option status.renames is set to "copies")
    'U',  # updated but unmerged
    '?',  # untracked
    # '!',  # ignored
]


def is_git_repo(path):
    command = ['git', '-C', path, 'rev-parse']
    return call(command, stderr=STDOUT, stdout=open(os.devnull, 'w')) == 0


def git_root_dir(path):
    command = "git -C '%s' rev-parse --show-toplevel" % path
    stream = os.popen(command)
    return stream.read().strip()


def git_status_lines(path, parent_path=None):
    if parent_path is None:
        command = "git -C '%s' status --porcelain" % path
    else:
        path = path.replace('%s/' % parent_path, '')
        command = "git -C '%s' status --porcelain '%s'" % (parent_path, path)

    stream = os.popen(command)
    output = stream.readlines()
    return output


class GitInfoExtension(GObject.GObject, Nautilus.InfoProvider):
    def __init__(self):
        super().__init__()
        print("Initialized GitInfoExtension")

    def update_file_info_full(self, provider, handle, closure, file):
        file_path = unquote(urlparse(file.get_uri()).path)

        if file.is_directory():
            if is_git_repo(file_path):
                repo_root = git_root_dir(file_path)

                is_root_dir = repo_root == file_path

                if is_root_dir:
                    file.add_emblem('git')

                lines = git_status_lines(file_path, repo_root)

                for line in lines:
                    status = line.strip().split(' ')[0]
                    skip = False
                    for s in git_file_status:
                        if status.find(s) != -1:
                            file.add_emblem('dialog-warning')
                            if is_root_dir:
                                skip = True
                                break
                    if skip:
                        break
        else:
            parent_path = unquote(urlparse(file.get_parent_uri()).path)

            if is_git_repo(parent_path):
                lines = git_status_lines(file_path, parent_path)

                for line in lines:
                    status = line.strip().split(' ')[0]
                    for s in git_file_status:
                        if status.find(s) != -1:
                            file.add_emblem('dialog-warning')
