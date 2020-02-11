import os


class GitRepoCtrl:
    def __init__(self, remote_addr, locate_path='.', branch='master', depth=1):
        # repo config
        self.remote_addr = remote_addr
        self.reponame = remote_addr.split('/')[-1].split('.')[0]
        self.branch = branch
        self.depth = depth
        self.locate_path = locate_path

        # shell cmd
        self.git_cmd_getGit = 'whereis git'
        self.git_cmd_clone = 'git clone {} -b {} --depth {}'.format(
            remote_addr, branch, depth)
        self.git_cmd_gotolocation = 'cd {}'.format(locate_path)
        self.git_cmd_gotorepo = 'cd {}{}'.format(locate_path, self.reponame)
        self.git_cmd_fetch = 'git fetch'
        self.git_cmd_status = 'git status'
        self.git_cmd_createtmpbranch = 'git branch tmptmptmp'
        self.git_cmd_checkouttmpbranch = 'git checkout tmptmptmp'
        self.git_cmd_pull = 'git pull'
        self.git_cmd_checkoutdefaultbranch = 'git checkout {}'.format(branch)
        self.git_cmd_deltmpbranch = 'git branch -D tmptmptmp'

        # tips
        self.judge_uptodate = 'Your branch is up to date with'
        self.judge_timeout = 'Your branch is behind'

        # init repo
        if self.Git_exists:
            self.git_clone()
        else:
            print('found none of git')

    def Git_exists(self):
        pipeline = os.popen(self.git_cmd_getGit)
        result = pipeline.read().split('git:')[1]
        if result == '\n':
            return False
        else:
            return True

    def git_clone(self):
        os.system('{}&&{}'.format(
            self.git_cmd_gotolocation, self.git_cmd_clone))

    def repo_is_uptodate(self):
        os.system('{}&&{}'.format(
            self.git_cmd_gotorepo,
            self.git_cmd_fetch))

        pipline = os.popen('{}&&{}'.format(
            self.git_cmd_gotorepo,
            self.git_cmd_status))

        result = pipline.read()
        if self.judge_uptodate in result:
            return True
        elif self.judge_timeout in result:
            return False

    def updateRepo(self):
        print('updating repo')
        # os.system('{}&&{}'.format(
        #     self.git_cmd_gotorepo,
        #     self.git_cmd_createtmpbranch))
        # os.system('{}&&{}'.format(
        #     self.git_cmd_gotorepo,
        #     self.git_cmd_checkouttmpbranch))
        os.system('{}&&{}'.format(
            self.git_cmd_gotorepo,
            self.git_cmd_pull))
        # os.system('{}&&{}'.format(
        #     self.git_cmd_gotorepo,
        #     self.git_cmd_checkoutdefaultbranch))
        # os.system('{}&&{}'.format(
        #     self.git_cmd_gotorepo,
        #     self.git_cmd_deltmpbranch))
        print('your branch is up to date')

    def ensureRepoUptodate(self):
        if self.repo_is_uptodate():
            print('repo has already been up to date')
        else:
            self.updateRepo()