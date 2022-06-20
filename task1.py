import enum
import os
import argparse
import filehash
from dirhash import dirhash
from pwd import getpwuid
from datetime import datetime
import json
import csv
import htmlText


def createParser(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', action='store_const', const=True)
    parser.add_argument('-s', action='store_const', const=True)
    parser.add_argument('-p')
    parser.add_argument('-d', action='store_const', const=True)
    parser.add_argument('-f', action='store_const', const=True)
    parser.add_argument('-v', action='store_const', const=True)
    parser.add_argument('-l', action='store_const', const=True)
    parser.add_argument('--unix', action='store_const', const=True)
    parser.add_argument('--utc', action='store_const', const=True)
    parser.add_argument('-t', action='store_const', const=True)
    parser.add_argument('-j', action='store_const', const=True)
    parser.add_argument('--html', action='store_const', const=True)
    parser.add_argument('-c', action='store_const', const=True)
    return parser


parser = createParser()
namespace = parser.parse_args()

class Path_Mode(enum.Enum):
    SCRIPT_PATH = 'local path'
    RUN_PATH = 'run path'
    DEFINED_PATH = 'custom path' 

class Time_Mode(enum.Enum):
    UNIX = 'UNIX'
    UTC = 'UTC'

class LS:
    @staticmethod
    def get_path(mode: Path_Mode) -> str:
        match mode:
            case Path_Mode.SCRIPT_PATH:
                return os.path.dirname(os.path.abspath(__file__))
            case Path_Mode.RUN_PATH:
                return os.path.abspath(os.curdir)
            case Path_Mode.DEFINED_PATH:
                global namespace
                return namespace.p
    
    @staticmethod
    def get_content_list(path: str) -> list:
            return os.listdir(path)
 
    @staticmethod
    def get_file_list(path: str) -> list:
        dir_content = LS.get_content_list(path)
        
        files=[]
        for file in dir_content:
            if os.path.isfile(os.path.join(path, file)): files.append(os.path.join(path, file))
        return files
    
    @staticmethod
    def get_directory_list(path: str) -> list:
        dir_content = LS.get_content_list(path)
        
        dirs=[]
        for dir in dir_content:
            if os.path.isdir(os.path.join(path, dir)): dirs.append(os.path.join(path, dir))
        return dirs

    @staticmethod
    def get_file_info(path: str, time_mode: Time_Mode) -> dict:
        size = os.path.getsize(path)

        hasher = filehash.FileHash('md5')
        file_hash = hasher.hash_file(path)
        owner = getpwuid(os.stat(path).st_uid).pw_name
        unix_mod_time = os.path.getmtime(path)
        unix_creat_time = os.path.getctime(path)

        utc_mod_time = datetime.utcfromtimestamp(unix_mod_time).strftime('%Y-%m-%d %H:%M:%S')
        utc_creat_time = datetime.utcfromtimestamp(unix_creat_time).strftime('%Y-%m-%d %H:%M:%S')
        time_mod = utc_mod_time
        time_creat = utc_creat_time
        if time_mode == Time_Mode.UNIX:
            time_mod = unix_mod_time
            time_creat = unix_creat_time

        return {
            'name': path,
            'size': size,
            'hash': file_hash,
            'owner': owner,
            'time creation': time_creat,
            'time modification': time_mod,
        }

    @staticmethod
    def get_directory_info(path: str, time_mode: Time_Mode) -> dict:
        size = os.path.getsize(path)
        if len(os.listdir(path)):
            dir_hash = dirhash(path, 'md5')
        else:
            dir_hash = "directory is empty"
        owner = getpwuid(os.stat(path).st_uid).pw_name
        unix_mod_time = os.path.getmtime(path)
        unix_creat_time = os.path.getctime(path)

        utc_mod_time = datetime.utcfromtimestamp(unix_mod_time).strftime('%Y-%m-%d %H:%M:%S')
        utc_creat_time = datetime.utcfromtimestamp(unix_creat_time).strftime('%Y-%m-%d %H:%M:%S')
        time_mod = utc_mod_time
        time_creat = utc_creat_time
        if time_mode == Time_Mode.UNIX:
            time_mod = unix_mod_time
            time_creat = unix_creat_time

        return {
            'name': path,
            'size': size,
            'hash': dir_hash,
            'owner': owner,
            'time creation': time_creat,
            'time modification': time_mod,
        }

    @staticmethod
    def save_as_txt(path: str, content: str) -> None:
        with open(path, "w") as txtfile:
            txtfile.write(content)

    @staticmethod
    def save_as_json(path: str, content: dict) -> None:
        with open(path, "w") as jsonfile:
            json.dump(content, jsonfile)

    @staticmethod
    def save_as_csv(path: str, content: dict) -> None:
       with open(path, "w", newline="") as csvfile:
        if type(content[0]) is dict:
            columns = ["name", "size", 'hash', 'owner', 'time creation', 'time modification']
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()
            writer.writerows(content)
        else:
            csvfile.write(str(content))

    @staticmethod        
    def save_as_html(path: str, content: str) -> None:
        result = htmlText.html(path, content)
        with open(path, "w") as htmlfile:
            htmlfile.write(result)

    @staticmethod
    def get_report_content(report_path: str) -> str:
        with open(report_path, "r") as report:
            content = report.read()
        return content

    @staticmethod
    def get_task_status() -> str:
        return '''module 1
        task 1 - done, 
        task 2 - done, 
        task 3 - done,
        task 4 - done, 
        task 5 - done, 
        task 6 - done,
        task 7 - done, 
        task 8 - done, 
        task 9 - done,
        task 10 - done, 
        '''

    @staticmethod
    def validate_option(): 
        global namespace

        if namespace.r:
            mode = Path_Mode.RUN_PATH
        elif namespace.p:
            mode = Path_Mode.DEFINED_PATH
        else:
            mode = Path_Mode.SCRIPT_PATH

        path = LS.get_path(mode)

        if os.path.isdir(path):
            if namespace.utc:
                time_mode = Time_Mode.UTC
            else:
                time_mode = Time_Mode.UNIX
            content = LS.get_content_list(path)


            if namespace.f:
                content = LS.get_file_list(path)
                if namespace.v:
                    content = []
                    for file in LS.get_file_list(path):
                        content.append(LS.get_file_info(file, time_mode))
            elif namespace.d:
                content = LS.get_directory_list(path)
                if namespace.v:
                    content = []
                    for dir in LS.get_directory_list(path):
                        content.append(LS.get_directory_info(dir, time_mode))

                        
        if namespace.t:
            LS.save_as_txt(os.path.join(LS.get_path(Path_Mode.SCRIPT_PATH), 'content.txt'), str(content))
            #extension = 'content.txt'
        elif namespace.j:
            LS.save_as_json(os.path.join(LS.get_path(Path_Mode.SCRIPT_PATH), 'content.json'), content)
            #extension = 'content.json'
        elif namespace.c:
            LS.save_as_csv(os.path.join(LS.get_path(Path_Mode.SCRIPT_PATH), 'content.csv'), content)
            #extension = 'content.csv'
        elif namespace.html:
            LS.save_as_html(os.path.join(LS.get_path(Path_Mode.SCRIPT_PATH), 'content.html'), content)
            #extension = 'content.html'
        return content



if __name__ == '__main__':
    print(LS.validate_option())

