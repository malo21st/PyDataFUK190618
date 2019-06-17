#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# PythonでWeb上のファイルをダウンロードする
# source https://qiita.com/yuukiclass/items/88e9ac6c5a3b5ab56cc4
# このプログラムと同じ場所に保存される。
'''
import urllib.request
#import sys

URL = "https://www.data.jma.go.jp/fcd/yoho/typhoon/position_table/"
TBL = "table"

def download(url, path_file):

#    url = sys.argv[1]
#    title = sys.argv[2]
    urllib.request.urlretrieve(url,path_file)
    
def main():
    for i in range(2001,2019):
        file_name = TBL + str(i) + ".csv"
        url_file = URL + file_name # table2001.csv 〜 table2018.csv
        download(url_file, file_name)
    print('Finish!')
    
if __name__ == "__main__":
    main()
    