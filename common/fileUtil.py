import shutil


# old_file_path ファイルパス
# new_path 移動先パス
def move_file(old_file_path, new_path):
    move_path = shutil.move(old_file_path, new_path)
    print("移動完了：" + move_path)

# old_directory_path ディレクトリパス
# new_path 移動先パス
def move_dilectory(old_directory_path, new_path):
    move_path = shutil.movw(old_directory_path, new_path)
    print("移動完了：" + move_path)