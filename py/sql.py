#!/usr/bin/env python
#coding=utf-8
import torndb
addr="127.0.0.1:3306"
db_name="pycms"
user_name="root"
pass_word="root"
db = torndb.Connection(addr, db_name, user=user_name, password=pass_word)
def init_db(db):
    print "create table blog"
    cre='create table blog(id int,content text)'
    db.execute(cre)

def table_chk(db):
    sql="SELECT count( * ) as num FROM information_schema.TABLES WHERE table_name = %s AND TABLE_SCHEMA = %s"
    result=db.query(sql, 'blog', 'pycms')
    if result[0]['num'] != 0:
        return True
    else:
        return False
if __name__ == "__main__":
    if table_chk(db):
        print "db exist"
    else:
        print "db not exist"
        init_db(db)
