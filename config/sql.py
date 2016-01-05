#!/usr/bin/env python
#coding=utf-8
#import torndb
import MySQLdb
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
def add_article(db,id=-1,title="",content=""):
    sql = "INSERT INTO blog (id,title,content) VALUES (%s,%s,%s)"
    db.insert(sql,id,title,content)
class DB(object):
    def __init__(self):
        host="127.0.0.1"
        port=3306
        db_name="pycms"
        user_name="root"
        pass_word="root"
        self.conn = MySQLdb.connect(
                host=host,
                port = port,
                user=user_name,
                passwd=pass_word,
                db=db_name,
                charset="utf8")
        self.cursor = self.conn.cursor()
    def __del__(self):
        self.conn.close()
    def get_articles(self,offset=0,rows=5):
        """返回查询到的记录
        Args:
            offset:偏移
            rows:取得记录条数，默认是5
        Returns:
            如果有数据返回一个元祖,元祖中每一个元素也是一个元祖，
            包含的元素依次为id,title,content,summary,tag,update_time。
            如果无数据返回一个空元祖"""
        sql="SELECT id,title,content,summary,tag,update_time from article LIMIT %d,%d"%(offset,rows)
        result=self.cursor.execute(sql)
        infos=self.cursor.fetchall()
        return infos

    def get_article(self,article_id):
        """返回查询到的记录
        Args:
            article_id:文章id
        Returns:
            如果有数据返回一个元祖,
            包含的元素依次为id,title,content,summary,tag,update_time。
            如果没有数据，则返回None"""
        sql="SELECT id,title,content,summary,tag,update_time from article WHERE id='%d'"%(article_id)
        result=self.cursor.execute(sql)
        info=self.cursor.fetchone()
        return info

if __name__ == "__main__":
    db=DB()
    #print db.get_articles(offset=0,rows=2)
    print db.get_article(1)

