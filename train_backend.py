import sqlite3

def connect():
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS train1 (trainid INTEGER PRIMARY KEY,trainname varchar(200),carriages1 integer,cap1 integer,price1 varchar(200),carriages2 integer,cap2 integer,price2 varchar(200),carriages3 integer,cap3 integer,price3 varchar(200))")
    cur.execute("CREATE TABLE IF NOT EXISTS route (trainid INTEGER PRIMARY KEY,stationidsource integer,stationnamesource varchar(200),arrsource varchar(200),stationid1 integer,stationname1 varchar(200),arr1 varchar(200),dep1 varchar(200),stationid2 integer,stationname2 varchar(200),arr2 varchar(200),dep2 varchar(200),stationid3 integer,stationname3 varchar(200),arr3 varchar(200),dep3 varchar(200),stationiddest integer,stationnamedest varchar(200),arrdest varchar(200) )")
    cur.execute("CREATE TABLE IF NOT EXISTS station (stationidsource integer,stationnamesource varchar(200),stationid1 integer,stationname1 varchar(200),stationid2 integer,stationname2 varchar(200),stationid3 integer,stationname3 varchar(200),stationiddest integer,stationnamedest varchar(200))")
    conn.commit()
    conn.close()

def inserttrain(trainid,trainname,carriages1,cap1,price1,carriages2,cap2,price2,carriages3,cap3,price3):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("INSERT OR IGNORE INTO train1 (trainid,trainname,carriages1,cap1,price1,carriages2,cap2,price2,carriages3,cap3,price3) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(trainid,trainname,carriages1,cap1,price1,carriages2,cap2,price2,carriages3,cap3,price3))
    conn.commit()
    conn.close()

def insertroute(trainid,stationidsource ,stationnamesource,arrsource,stationid1,stationname1,arr1,dep1,stationid2,stationname2,arr2,dep2,stationid3,stationname3,arr3,dep3,stationiddest,stationnamedest,arrdest):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("INSERT OR IGNORE INTO route (trainid,stationidsource,stationnamesource,arrsource,stationid1,stationname1,arr1,dep1,stationid2,stationname2,arr2,dep2,stationid3,stationname3,arr3,dep3,stationiddest,stationnamedest,arrdest) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(trainid,stationidsource ,stationnamesource,arrsource,stationid1,stationname1,arr1,dep1,stationid2,stationname2,arr2,dep2,stationid3,stationname3,arr3,dep3,stationiddest,stationnamedest,arrdest))
    conn.commit()
    conn.close()


def insertstation(stationidsource,stationnamesource,stationid1,stationname1,stationid2,stationname2,stationid3,stationname3,stationiddest,stationnamedest):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("INSERT OR IGNORE INTO station (stationidsource,stationnamesource,stationid1,stationname1,stationid2,stationname2,stationid3 ,stationname3 ,stationiddest,stationnamedest)  VALUES (?,?,?,?,?,?,?,?,?,?)",(stationidsource,stationnamesource,stationid1,stationname1,stationid2,stationname2,stationid3,stationname3,stationiddest,stationnamedest))
    conn.commit()
    conn.close()



def searchtrainname(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT trainname FROM train1 WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchclass1carriages(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT carriages1 FROM train1 WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchclass1cap(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT cap1 FROM train1 WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchclass1price(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT price1 FROM train1 WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item








def searchclass2carriages(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT carriages2 FROM train1 WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchclass2cap(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT cap2 FROM train1 WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchclass2price(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT price2 FROM train1 WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item






def searchclass3carriages(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT carriages3 FROM train1 WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchclass3cap(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT cap3 FROM train1 WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchclass3price(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT price3 FROM train1 WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item









def searchssourceid(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT stationidsource FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchsourcename(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT stationnamesource FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchsourcedep(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT arrsource FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item






def searchstop1id(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT stationid1 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchstop1name(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT stationname1 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchstop1arr(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT arr1 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchstop1dep(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT dep1 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item








def searchstop2id(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT stationid2 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchstop2name(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT stationname2 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchstop2arr(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT arr2 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchstop2dep(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT dep2 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item








def searchstop3id(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT stationid3 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchstop3name(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT stationname3 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchstop3arr(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT arr3 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchstop3dep(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT dep3 FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item










def searchstopdestid(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT stationiddest FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchstopdestname(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT stationnamedest FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item

def searchstopdestarr(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("SELECT arrdest FROM route WHERE trainid=?", (trainid))
    item=cur.fetchall()
    conn.close()
    return item







def deletetrain(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("DELETE  FROM train1 WHERE trainid=?",(trainid))

    conn.commit()
    conn.close()

def deleteroute(trainid=""):
    conn=sqlite3.connect("Railway1.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM route WHERE trainid=?",(trainid))

    conn.commit()
    conn.close()


connect()
