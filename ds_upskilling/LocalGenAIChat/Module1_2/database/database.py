import sqlite3
from config import DB

def con(): return sqlite3.connect(DB)

def create_table():
 c=con();cur=c.cursor();cur.execute('create table if not exists Conversation(id integer primary key, role text, content text)');c.commit();c.close()

def save(r,t):
 c=con();cur=c.cursor();cur.execute('insert into Conversation(role,content) values(?,?)',(r,t));c.commit();c.close()

def load_messages():
 c=con();cur=c.cursor();cur.execute('select role,content from Conversation order by id');rows=cur.fetchall();c.close();m=[{'role':'system','content':'You are a helpful AI assistant.'}];m.extend([{'role':r,'content':t} for r,t in rows]);return m
