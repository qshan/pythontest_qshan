#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @FileName  :search_file_in_path.py
# @Author    :Frank Shan

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
            #debug#print ("[D] Get path name of file   : " + pathname)
            #debug#print ("[D] Get subdir info         : %s" % subdir)
            #debug##print ("Get subdir info        : ")
            #debug##print (subdir)
            #debug#print ("------------------------------")
            #result.append(os.path.join(path, filename))
            result.append(path)
            #debug#print ("[D] Get path info one time  : " + path)
    return result


def search_file_01(file_name, directory_name):
    files_found = []
    for path, subdirs, files in os.walk(directory_name):
        for name in files:
            if(file_name == name):
                file_name_with_path = os.path.join(path,name)
                #debug#
                #debug#print ("------------------------------")
                #debug#print ("[D] Get file name with path : " + file_name_with_path)
                #debug#print ("[D] Get path name of file   : " + path)
                #debug##print ("[D] Get subdirs info        : ")
                #debug##print (subdirs)
                #debug#print ("[D] Get subdirs info        : %s" % subdirs)
                #debug#print ("[D] Get file name info      : " + name)
                #debug#print ("------------------------------")
                files_found.append(file_name_with_path)
    return files_found

def main():

    import sys
    #TODO#Check the input argument info here
    print ("------------------------------")
    print ("[D] Get input arguments              : %s" % sys.argv)
    print ("[D] Get length of input arguments    : %s" % len(sys.argv))

    #i = len(sys.argv)
    i = 0
    while (i < len(sys.argv)) :
        #print ("[D] sys.argv[%d]                 : " % i + sys.argv[i])
        print ("[D] sys.argv[%d]                      : %s" % (i  ,sys.argv[i]))
        i = i+1
    print ("------------------------------")

    file_got_after_search = []
    #print (search_file('study.txt', '~/data/myenv'))
    #print (search_file('study.txt', '/home/fshan/data/myenv'))
    file_got_after_search+=(search_file_01('_emacs', '/home/fshan/data/myenv'))
    print ("Get the [files] : %s" % file_got_after_search)

    #file01_got_after_search = []
    #file01_got_after_search.append(search_files_01('study.txt', '/home/fshan/data/myenv'))
    file_got_after_search+=(search_files('study.txt', '/home/fshan/data/myenv'))
    print ("Get the [files] : %s" % file_got_after_search)

    file_got_after_search+=(search_files('matchit.vim', '/home/fshan/data/myenv'))
    print ("Get the [files] : %s" % file_got_after_search)

    path01_got_after_search = []
    #path01_got_after_search.append(search_path_01('_vim', '/home/fshan/data/myenv'))
    path01_got_after_search+=(search_path('_vim', '/home/fshan/data/myenv'))
    print ("Get the [paths] :%s" % path01_got_after_search)

    path01_got_after_search+=(search_path('pyim', '/home/fshan/data/myenv'))
    print ("Get the [paths] :%s" % path01_got_after_search)
#enf of def main():

if __name__ == "__main__":
    # execute only if run as a script
    main()
