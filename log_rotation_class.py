import logging
import os
import shutil
from datetime import datetime

from logRotation.log_conf import all_files_name_size, file_name_count, dir_path, names, task_files, error_files, debug_files


def delete_last_old_file(file_dict):
    new_file_list = []
    file_to_delete = ""
    for i in range(1, len(file_dict)):
        new_file_list.append(file_dict[i])

    file_to_delete = dir_path + new_file_list[0][:-1] + "del"
    os.rename(dir_path + "/" + new_file_list[0], dir_path + new_file_list[0][:-1] + "del")

    for i in range(1, len(new_file_list)):
        os.rename(dir_path + "/" + new_file_list[i], dir_path + "/" + new_file_list[i][:-1] + str(i - 1))

    os.remove(file_to_delete)


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


def create_files_list_to_log_name(file_dict):
    for key in file_dict:
        if 'task' in key:
            task_files.append(key)
        if 'debug' in key:
            debug_files.append(key)
        if 'error' in key:
            error_files.append(key)
    return task_files, debug_files, error_files


def count_update_files(task_files_dict, debug_files_dict, error_files_dict):
    if 10 >= len(task_files) > 0 and task_files is not {}:
        file_name_count['task.log'] = len(task_files) - 1
    elif len(task_files) == 11:
        delete_last_old_file(task_files_dict)

    if 10 >= len(error_files) > 0 and error_files is not {}:
        file_name_count['error.log'] = len(error_files) - 1
    elif len(error_files) == 11:
        delete_last_old_file(error_files_dict)

    if 10 >= len(debug_files) > 0 and debug_files is not {}:
        file_name_count['debug.log'] = len(debug_files) - 1
    elif len(debug_files) == 11:
        delete_last_old_file(debug_files_dict)

    return file_name_count


def create_new_log(file_name, count):
    source = dir_path + "/" + file_name
    dest = shutil.copyfile(source,
                           dir_path + "/" + datetime.now().strftime(
                               file_name + '_%H_%M_%d_%m_%Y.log_' + str(count)))
    # delete_old_log


def check_file_capacity(file_dict):
    try:
        for key in file_name_count:
            # print(key)
            if (file_dict[key] > 5242918):
                create_new_log(key, file_name_count[key])
    except(KeyError, NameError):
        logging.error("test log")


def main():
    file_dict = get_file_name_and_size()
    task_files_dict, debug_files_dict, error_files_dict = create_files_list_to_log_name(file_dict)
    count_update_files(task_files_dict, debug_files_dict, error_files_dict)
    check_file_capacity(file_dict)


if __name__ == '__main__':
    main()
