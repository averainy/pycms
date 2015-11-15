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
    cre='create table blog(id int,title text,content text)'
    db.execute(cre)

def table_chk(db):
    sql="SELECT count( * ) as num FROM information_schema.TABLES WHERE table_name = %s AND TABLE_SCHEMA = %s"
    result=db.query(sql, 'blog', 'pycms')
    if result[0]['num'] != 0:
        return True
    else:
        return False
def get_articles(db,offset=0,rows=5):
    sql="SELECT id,title,content from blog LIMIT %s,%s"
    result=db.query(sql,offset,rows)
    print result
def add_article(db,id=-1,title="",content=""):
    sql = "INSERT INTO blog (id,title,content) VALUES (%s,%s,%s)"
    db.insert(sql,id,title,content)
if __name__ == "__main__":
    get_articles(db,offset=0,rows=5)
