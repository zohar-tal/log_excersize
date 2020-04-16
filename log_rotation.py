import fnmatch
import logging
import os
import shutil
from datetime import datetime

from logRotation.log_conf import all_files_name_size, file_name_count, dir_path, names


def get_file_name_and_size():
    try:
        for i in range(0, len(names)):
            size = os.path.getsize(dir_path + "/" + names[i])
            all_files_name_size[names[i]] = size
    except KeyError as e:
        logging.error("file is unknown\n" + e)
    except(OSError, IOError) as e:
        logging.error("file path not exist\n" + e)
    return all_files_name_size


def create_new_log(file_name):
    for key in file_name_count:
        if fnmatch.fnmatch(file_name, '*.log_*'):
            length = len(file_name)
            last_char = file_name[length - 1]
            print (last_char)
            continue
        if key != file_name:
            continue
        else:
            prefix_file_name = key.split(".")
            source = dir_path + "/" + key
            dest = shutil.copyfile(source, dir_path + "/" + datetime.now().strftime(
                prefix_file_name[0] + '_%H_%M_%d_%m_%Y.log_' + str(file_name_count[key])))


def check_file_capacity(file_dict):
    print(file_dict)
    try:
        for key in file_dict:
            # print(key)
            if (file_dict[key] > 5242918):
                # if fnmatch.fnmatch(key, '*.log_'):
                create_new_log(key)
    except(KeyError, NameError):
        logging.error("test log")


get_file_name_and_size()
check_file_capacity(all_files_name_size)
