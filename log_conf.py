import os

all_files_name_size = dict()
file_name_count = {'error.log': 0, 'debug.log': 0, 'task.log': 0}
dir_path = 'C:/Users/user/Documents/talTraining/files'
names = os.listdir(dir_path)
max_backup_file_count = 10
file_max_size_kb = 5242918
task_files=[]
error_files=[]
debug_files=[]


