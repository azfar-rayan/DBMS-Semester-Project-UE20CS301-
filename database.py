import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agri_project"
)
c = mydb.cursor()


def create_farmer_table():
    c.execute('CREATE TABLE IF NOT EXISTS farmer(fid int(255) NOT NULL,fname varchar(255) NOT NULL,fusername varchar(255) NOT NULL,fpassword varchar(255) NOT NULL,femail varchar(255) NOT NULL,fmobile varchar(255) NOT NULL,faddress text NOT NULL)')

def create_buyer_table():
    c.execute('CREATE TABLE IF NOT EXISTS buyer(bid int(255) NOT NULL,bname varchar(255) NOT NULL,busername varchar(255) NOT NULL,bpassword varchar(255) NOT NULL,bemail varchar(255) NOT NULL,bmobile varchar(255) NOT NULL,baddress text NOT NULL)')


def add_farmer_data(fid, fname, fusername, fpassword, femail, fmobile, faddress):
    c.execute('INSERT INTO farmer(fid, fname, fusername, fpassword, femail, fmobile, faddress) VALUES (%d,%s,%s,%s,%s,%s,%s)',(fid, fname, fusername, fpassword, femail, fmobile, faddress))
    mydb.commit()

def add_buyer_data(bid, bname, busername, bpassword, bemail, bmobile, baddress):
    c.execute('INSERT INTO buyer(bid, bname, busername, bpassword, bemail, bmobile, baddress) VALUES (%d,%s,%s,%s,%s,%s,%s)',(bid, bname, busername, bpassword, bemail, bmobile, baddress))
    mydb.commit()


def view_all_farmer_data():
    c.execute('SELECT * FROM farmer')
    data = c.fetchall()
    return data

def view_all_buyer_data():
    c.execute('SELECT * FROM buyer')
    data = c.fetchall()
    return data

def view_only_farmer_names():
    c.execute('SELECT fname FROM farmer')
    data = c.fetchall()
    return data

def view_only_buyer_names():
    c.execute('SELECT bname FROM buyer')
    data = c.fetchall()
    return data


def get_farmer(fname):
    c.execute('SELECT * FROM farmer WHERE fname="{}"'.format(fname))
    data = c.fetchall()
    return data

def get_buyer(bname):
    c.execute('SELECT * FROM buyer WHERE bname="{}"'.format(bname))
    data = c.fetchall()
    return data


def edit_farmer_data(new_fid, new_fname, new_fusername, new_fpassword, new_femail, new_fmobile, new_faddress,fid, fname, fusername, fpassword, femail, fmobile, faddress):
    c.execute("UPDATE farmer SET fid=%d, fname=%s, fusername=%s, fpassword=%s, femail=%s, fmobile=%s, faddress=%s WHERE fid=%d and fname=%s and fusername=%s and fpassword=%s and femail=%s and fmobile=%s and faddress=%s", (new_fid, new_fname, new_fusername, new_fpassword, new_femail, new_fmobile, new_faddress,fid, fname, fusername, fpassword, femail, fmobile, faddress))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_buyer_data(new_bid, new_bname, new_busername, new_bpassword, new_bemail, new_bmobile, new_baddress,bid, bname, busername, bpassword, bemail, bmobile, baddress):
    c.execute("UPDATE buyer SET bid=%d, bname=%s, busername=%s, bpassword=%s, bemail=%s, bmobile=%s, baddress=%s WHERE bid=%d and bname=%s and busername=%s and bpassword=%s and bemail=%s and bmobile=%s and baddress=%s", (new_bid, new_bname, new_busername, new_bpassword, new_bemail, new_bmobile, new_baddress,bid, bname, busername, bpassword, bemail, bmobile, baddress))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_farmer_data(fname):
    c.execute('DELETE FROM farmer WHERE fname="{}"'.format(fname))
    mydb.commit()

def delete_buyer_data(bname):
    c.execute('DELETE FROM buyer WHERE fname="{}"'.format(bname))
    mydb.commit()
