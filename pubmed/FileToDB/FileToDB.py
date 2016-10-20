# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:30:15 2016

@author: liyan
"""

import os
import MySQLdb

import sys
reload(sys)
#python默认环境编码时ascii
sys.setdefaultencoding("utf-8")


PATH = r'C:\Users\liyan\Documents\pubmed\data1'


def get_date(date):
    if not date:
        return 
    date = date.split(';')[0].split()
    year = date[0]
    
    if len(date) > 1:
        if 'Feb' in date[1]:
            month = '02'
        elif 'Mar' in date[1]:
            month = '03'
        elif 'Apr' in date[1]:
            month = '04'
        elif 'May'in date[1]:
            month = '05'
        elif 'Jun' in date[1]:
            month = '06'
        elif 'Jul' in date[1]:
            month = '07'
        elif 'Aug' in date[1]:
            month = '08'
        elif 'Sep' in date[1]:
            month = '09'
        elif 'Oct' in date[1]:
            month = '10'
        elif 'Nov' in date[1]:
            month = '11'
        elif 'Dec' in date[1]:
            month = '12'
        else:
            month = '01'
    else:
        month = '01' 
        
    if len(date) > 2:
        day = date[2]
    else:
        day = '01'
    return year + '-' + month + '-' + day


def save_paper(pmid,title,date,journal,abstract,conn):
    try:
        cur=conn.cursor()
        cur.execute('insert into paper values (%s,"%s","%s","%s","%s")' % (int(pmid),title.replace('"','""'),date,journal,abstract.replace('"','""')))
        cur.close()
        conn.commit()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s,(%s)" % (e.args[0], e.args[1],pmid)
        #exit()


def save_author(authorline,pmid,conn):
    author_list = authorline.split('/')
    try:
        cur=conn.cursor()
        for author in author_list:
            cur.execute('insert into author values (%s,"%s")' % (int(pmid),author))
        cur.close()
        conn.commit()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s(%s)" % (e.args[0], e.args[1],pmid)
        #exit()
        

def main():
    conn=MySQLdb.connect(host='localhost',user='root',passwd='0000',db='Paper_Information',port=3306,charset='utf8',)
    #conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='0000',db='Paper_Information',port=3306,charset='utf8',)
    for filename in os.listdir(PATH):
        afile = open(PATH + '\\%s' % (filename))
        file_line_list = afile.read( ).split('\n')  
        
        if file_line_list[-2]:       #abstract is not empty
            pmid = filename.split('.')[0]
            #print pmid
            title = file_line_list[0]
            date = get_date(file_line_list[3])
            journal = file_line_list[2]
            abstract = file_line_list[4]
            author = file_line_list[1]
            save_paper(pmid,title,date,journal,abstract,conn)
            save_author(author,pmid,conn)
    conn.close()
  

main()
    
