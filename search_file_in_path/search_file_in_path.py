#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os

def search_files(filename, search_path):
    result = []
    # Wlaking top-down from the root
    #for root, dir, files in os.walk(search_path):
    for path, subdir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(path, filename))
            #debug#print ("Get file info " + path)
    return result

def search_path(pathname, search_path):
    result = []
    # Wlaking top-down from the root
    #for root, dir, files in os.walk(search_path):
    for path, subdir, files in os.walk(search_path):
        #print (".")
        if pathname in subdir:
            #debug#
            #debug#print ("------------------------------")
            #debug#print ("Get path name of file   : " + pathname)
            #debug##print ("Get subdir info        : ")
            #debug##print (subdir)
            #debug#print ("------------------------------")
            #result.append(os.path.join(path, filename))
            result.append(path)
            #debug#print ("Get path info one time" + path)
    return result


def search_file_01(file_name, directory_name):
    files_found = []
    for path, subdirs, files in os.walk(directory_name):
        for name in files:
            if(file_name == name):
                file_name_with_path = os.path.join(path,name)
                #debug#
                #debug#print ("------------------------------")
                #debug#print ("Get file name with path : " + file_name_with_path)
                #debug#print ("Get path name of file   : " + path)
                #debug##print ("Get subdirs info        : ")
                #debug##print (subdirs)
                #debug#print ("Get file name info      : " + name)
                #debug#print ("------------------------------")
                files_found.append(file_name_with_path)
    return files_found

def main():
    file_got_after_search = []
    #['array1' ,'array2']
    #print (search_file('study.txt', '~/data/myenv'))
    #print (search_file('study.txt', '/home/fshan/data/myenv'))
    file_got_after_search+=(search_file_01('_emacs', '/home/fshan/data/myenv'))
    print ("Get the [files] :")
    print (file_got_after_search)

    #file01_got_after_search = []
    #file01_got_after_search.append(search_files_01('study.txt', '/home/fshan/data/myenv'))
    file_got_after_search+=(search_files('study.txt', '/home/fshan/data/myenv'))
    print ("Get the [files] :")
    print (file_got_after_search)

    file_got_after_search+=(search_files('matchit.vim', '/home/fshan/data/myenv'))
    print ("Get the [files] :")
    print (file_got_after_search)

    #

    path01_got_after_search = []
    #path01_got_after_search.append(search_path_01('_vim', '/home/fshan/data/myenv'))
    path01_got_after_search+=(search_path('_vim', '/home/fshan/data/myenv'))
    print ("Get the [paths] :")
    print (path01_got_after_search)

    path01_got_after_search+=(search_path('pyim', '/home/fshan/data/myenv'))
    print ("Get the [paths] :")
    print (path01_got_after_search)



if __name__ == "__main__":
    # execute only if run as a script
    main()
