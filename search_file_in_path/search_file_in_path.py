#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os

def find_files_01(filename, search_path):
    result = []
    # Wlaking top-down from the root
    #for root, dir, files in os.walk(search_path):
    for path, subdir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(path, filename))
            print ("get file info " + path)
    return result

def find_path_01(pathname, search_path):
    result = []
    # Wlaking top-down from the root
    #for root, dir, files in os.walk(search_path):
    for path, subdir, files in os.walk(search_path):
        #print (".")
        if pathname in subdir:
            #result.append(os.path.join(path, filename))
            result.append(path)
            print ("get path info one time" + path)
    return result


def find_file(file_name, directory_name):
    files_found = []
    for path, subdirs, files in os.walk(directory_name):
        for name in files:
            if(file_name == name):
                file_path = os.path.join(path,name)
                print ("get file info " + file_path)
                files_found.append(file_path)
    return files_found

def main():
    file_got_after_search       =[]
    #['array1' ,'array2']
    #print (find_file('study.txt', '~/data/myenv'))
    #print (find_file('study.txt', '/home/fshan/data/myenv'))
    file_got_after_search+=(find_file('study.txt', '/home/fshan/data/myenv'))
    print (file_got_after_search)

    #file01_got_after_search = []
    #file01_got_after_search.append(find_files_01('study.txt', '/home/fshan/data/myenv'))
    file_got_after_search+=(find_files_01('study.txt', '/home/fshan/data/myenv'))
    print (file_got_after_search)

    path01_got_after_search = []
    #path01_got_after_search.append(find_path_01('_vim', '/home/fshan/data/myenv'))
    path01_got_after_search+=(find_path_01('_vim', '/home/fshan/data/myenv'))
    print (path01_got_after_search)



if __name__ == "__main__":
    # execute only if run as a script
    main()
