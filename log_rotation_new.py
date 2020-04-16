import glob
import logging
import os
from datetime import datetime

from logRotation.log_conf import dir_path, file_name, file_max_size_kb, suffix, max_backup_file_count


def rename_file_big_then_max_size(name):
    """
    - get the file log size of logs from dir path
    - in case file log is big then max_size it will be rename with time stamp
     :param name: name - name of all logs in dir path
     :return
    """
    try:
        source = dir_path + "/" + name + suffix
        size = os.path.getsize(source)
        if size > file_max_size_kb:
            dest = dir_path + "/" + name + suffix + datetime.now().strftime('_%H_%M_%d_%m_%Y')
            os.rename(source, dest)
    except KeyError as e:
        logging.error("file is unknown\n" + e)
    except(OSError, IOError) as e:
        logging.error("file path not exist\n" + e)


def delete_old_log(name):
    """
    - delete all the old log above max_backup_file_count
    :param name: name - name of all logs in dir path
    :return:
    """
    list_log = []
    for name in glob.glob(dir_path + '/' + name + '*.*'):
        list_log.append(name)
    sorted(list_log)

    for i in range(max_backup_file_count, len(list_log)):
        try:
            print('try remove log' + list_log[i])
            os.remove(list_log[i])
        except UserWarning as e:
            logging.warning("file not exist anymore\n" + e)


def main():
    for i in file_name:
        rename_file_big_then_max_size(i)
        delete_old_log(i)


if __name__ == '__main__':
    main()
