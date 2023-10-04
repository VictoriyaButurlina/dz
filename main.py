from Module.filecommands import create_files, rename_files


if __name__ == '__main__':

    create_files(5, 'tmp', 'DZ7/dir')
    rename_files('new_file', 2, 'tmp', 'gb', [3, 6], 'DZ7/dir')