from json import dumps as json_encode
from json import loads as json_decode
import os


def jsonDecode(json_str):
    return json_decode(json_str)


def jsonEncode(data_obj):
    return json_encode(data_obj)


class FileConCtrl:  # ctrl file
    def __init__(self, filePath, fileFolder='data'):
        if os.path.exists(fileFolder):
            pass
        else:
            os.mkdir(fileFolder)
        self.filePath = filePath

    def write_append(self, str):
        with open(self.filePath, 'a') as filefd:
            filefd.write(str + '\n')

    def write_cover(self, str):
        with open(self.filePath, 'w') as filefd:
            filefd.write(str)

    def read(self, AUTOCREATE=0):
        data_to_return = ""
        if os.path.isfile(self.filePath):
            # if file exists
            # read file and return data
            with open(self.filePath, 'r') as filefd:
                data_to_return = filefd.read()
        else:
            # if file not exists
            if AUTOCREATE == 1:
                with open(self.filePath, 'w') as filefd:
                    filefd.write("")
                pass
        return data_to_return


class DataArray:
    def __init__(self, filePath):
        self.dataArray = []
        self.fileCtrl = FileConCtrl(filePath)
        json_datatmp = self.fileCtrl.read(AUTOCREATE=1)
        if json_datatmp != "":
            self.dataArray = json_decode(json_datatmp)

    def get(self):
        return self.dataArray

    def getbyId(self, id):
        return self.dataArray[id]

    def add(self, new):
        self.dataArray.append(new)
        self.fileCtrl.write_cover(json_encode(self.dataArray))

    def clear(self):
        self.dataArray = []
        self.fileCtrl.write_cover(json_encode(self.dataArray))

    def delbyId(self, id):
        self.dataArray.pop(int(id))
        self.fileCtrl.write_cover(json_encode(self.dataArray))


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
        self.git_cmd_gotorepo = 'cd {}/{}'.format(locate_path, self.reponame)
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


if __name__ == '__main__':
    gitRepoCtrl = GitRepoCtrl(
        'https://github.com/alone-wolf/ifTheDoorOpen.git')
    gitRepoCtrl.ensureRepoUptodate()

# git branch tmp
# git checkout tmp
# git pull
# git checkout master
# git branch -D tmp
