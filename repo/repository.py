import os
import configparser
from .utils import repo_path, repo_file


class Repository(object):
    worktree = None
    gitdir = None
    conf = None
    def __init__(self, path, force=False):
        self.worktree = path
        self.gitdir = os.path.join(path, ".toygit")

        if not (force or os.path.isdir(self.gitdir)):
            raise Exception("Not a Git repository %s" % path)

        # Read configuration file in .git/config
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, "config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("Configuration file missing")

        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))
            if vers != 0:
                raise Exception("Unsupported repositoryformatversion %s" % vers)