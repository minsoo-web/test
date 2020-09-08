# -*- coding: utf-8 -*-

""".side Master

This module reflects information that can change dynamically during test execution in SIDE files.

Example:
    $ python master.py
"""


import ast
import fire
import glob
import platform
from typing import Any
from typing import Dict
from typing import List
from typing import NoReturn
from typing import Optional
from typing import Union
from typing import NewType
from colors import color

from decorators import timer
from exceptions import FileWriteError
from exceptions import ArgumentsError
from io_manager import FileManager
from url_manager import UrlChanger
from url_manager import UrlFinder
from user_manager import UserChanger
from utils import equals


FileInfo = NewType('Files', Dict[str, Optional[Union[str, dict]]])


OS = platform.system()


class Master(object):
    """This is the main class that takes charge of all tasks

    Attributes:
        changer (:obj: UrlChanger): UrlChanger class
        finder (:obj: UrlFinder): UrlFinder class
        reader (:obj: FileManager.Reader): This class is responsible for file input
        writer (:obj: FileManager.Writer): This class is responsible for file output
    """

    def __init__(self):
        """Init function

        Note:
            `self` is not an argument value
        """
        self.user_changer = UserChanger()
        self.url_changer = UrlChanger()
        self.finder = UrlFinder()
        self.reader = FileManager.Reader()
        self.writer = FileManager.Writer()

    def find_files(self, pathname: str) -> list:
        """
        """
        return glob.glob(pathname=pathname, recursive=True)

    def get_file_content(self, path: str, *, option='json') -> Union[str, dict, None]:
        res: Optional[str] = None

        if equals(option, 'json'):
            res = self.reader.read_JSON_file(file=path, mode='r')
        elif equals(option, 'text'):
            res = self.reader.read_raw_file(file=path, mode='r')

        return res

    def set_file_content(self, path: str, mode: str, data: Any, *, option='json') -> NoReturn:
        if equals(option, 'json'):
            res = self.writer.write_JSON_file(file=path, mode=mode, data=data)
        elif equals(option, 'text'):
            res = self.writer.write_raw_file(file=path, mode=mode, data=data)

        if not equals(res, True):
            raise FileWriteError(path)

    def find_url(self, data: str) -> str:
        res: str = self.finder.find(data=data)
        if not equals(res, ''):
            return res

    def change_url(self, old_url: str, new_url: str, data: str) -> str:
        res: str = self.url_changer.change(old_url=old_url, new_url=new_url, data=data)
        return res

    def change_user(self, new_user: str, new_password: str, data: str) -> str:
        res: str = self.user_changer.change(new_user=new_user, new_password=new_password, data=data)
        return res

    class SideMaster(object):

        def get_tests(self, data: Dict[str, str]) -> list:
            return data['tests']

        def get_test_id_and_name(self, data: List[str]) -> dict:
            return {x['name']: x['id'] for x in data}

        def get_test_suites(self, data: dict) -> list:
            return data['suites'][0]['tests']


class Skipper(object):
    def __init__(self):
        self.side: Master.SideMaster = Master.SideMaster()
        self.master: Master = Master()
        self.reader: FileManager.Reader = FileManager.Reader()

    def find_skip_tests(self, pathname: str) -> dict:
        file_list: List[str] = self.master.find_files(pathname=pathname)
        res: Dict[str, str] = {file: '' for file in file_list if 'skip-sample.txt' not in file}
        for file in res.keys():
            skip_test_list: List[str] = self.reader.read_raw_file(file=file, mode='r', option='line')
            res[file]: str = skip_test_list
        return res


class Pipeline(object):
    def __init__(self) -> NoReturn:
        self.master: Master = Master()
        self.side: Master.SideMaster = self.master.SideMaster()
        self.skipper: Skipper = Skipper()

    @timer
    def change_urls(self, files: List[FileInfo], new_url: str) -> list:
        print(color('Converting URL...', 'blue'), end=' ')
        for idx, data in enumerate(files):
            str_content: str = str(data['content'])
            old_url: str = self.master.find_url(data=str_content)
            data['content']: dict = ast.literal_eval(self.master.change_url(old_url=old_url, new_url=new_url, data=str_content))
            data['content']['url']: str = data['content']['url'].rstrip('/')
            data['content']['urls']: List[str] = [new_url]  # Init urls list
            files[idx]['content'] = data['content']
        print(color('✔', 'cyan'))
        return files

    @timer
    def change_users(self, files: List[FileInfo], new_user: str, new_password: str) -> list:
        print(color('Converting User...', 'blue'), end=' ')
        for idx, data in enumerate(files):
            str_content: str = str(data['content'])
            data['content': dict] = ast.literal_eval(self.master.change_user(new_user=new_user, new_password=new_password, data=data))
            files[idx]['content']
        print(color('✔', 'cyan'))
        return files

    @timer
    def reflect_skip_list(self, files: List[FileInfo], pathname: str) -> list:
        separator = '/' if OS != 'Windows' else '\\'
        skips = {}
        for key, value in self.skipper.find_skip_tests(pathname=pathname).items():
            clean_name = key.rstrip('.txt').split(sep=separator)[-1]
            skips[clean_name] = {
                'file': key,
                'list': value
            }

        for idx, data in enumerate(files):
            if (clean_file_name := data['file'].rstrip('.side').split(sep=separator)[-1]) in skips.keys():
                test_list = self.side.get_tests(data['content'])
                test_list = self.side.get_test_id_and_name(test_list)
                suites = self.side.get_test_suites(data['content'])
                for skip_list in skips[clean_file_name]['list']:
                    if skip_list in test_list.keys() and test_list[skip_list] in suites:
                        suites.remove(test_list[skip_list])
                files[idx]['content']['suites'][0]['tests'] = suites

    @timer
    def commit_file_changes(self, files: List[FileInfo]) -> NoReturn:
        print(color('Saving files...', 'blue'), end=' ')
        for data in files:
            self.master.writer.write_JSON_file(file=data['file'], mode='w', data=data['content'])
        print(color('✔', 'cyan'))


class Core(object):
    def __init__(self):
        self.master: Master = Master()
        self.pipe: Pipeline = Pipeline()

    def change(self, target: str, path: str, url=None, user=None, password=None):
        file_list: List[str] = self.master.find_files(path)
        contents: List[str] = [self.master.get_file_content(x) for x in file_list]
        files: List[FileInfo] = [{'file': file, 'content': content} for file, content in zip(file_list, contents)]
        if target == 'url':
            if url is None:
                raise ArgumentsError
            files = self.pipe.change_urls(files, url)
        elif target == 'user':
            if user is None or password is Nones:
                raise ArgumentsError
            files = self.pipe.change_users(files, user, password)
        else:
            raise ArgumentsError
        self.pipe.commit_file_changes(files)


if __name__ == "__main__":
    fire.Fire(Core)
