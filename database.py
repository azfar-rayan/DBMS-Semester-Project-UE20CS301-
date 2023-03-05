import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agri_project"
)
c = mydb.cursor()

def view_table(table):
    c.execute('SELECT * FROM {}'.format(table))
    data = c.fetchall()
    return data

def add_farmer_data(fid, fname, fusername, fpassword, femail, fmobile, faddress):
    c.execute('INSERT INTO farmer(fid, fname, fusername, fpassword, femail, fmobile, faddress) VALUES (%s,%s,%s,%s,%s,%s,%s)',(fid, fname, fusername, fpassword, femail, fmobile, faddress))
    mydb.commit()

def add_buyer_data(bid, bname, busername, bpassword, bemail, bmobile, baddress):
    c.execute('INSERT INTO buyer(bid, bname, busername, bpassword, bemail, bmobile, baddress) VALUES (%s,%s,%s,%s,%s,%s,%s)',(bid, bname, busername, bpassword, bemail, bmobile, baddress))
    mydb.commit()

def add_fproduct_data(fid, pid, product, pcat, pinfo, price):
    c.execute('INSERT INTO fproduct(fid, pid, product, pcat, pinfo, price) VALUES (%s,%s,%s,%s,%s,%s)',(fid, pid, product, pcat, pinfo, price))
    mydb.commit()

def view_fids():
    c.execute('SELECT fid FROM farmer')
    data = c.fetchall()
    return data

def view_bids():
    c.execute('SELECT bid FROM buyer')
    data = c.fetchall()
    return data

def view_pids():
    c.execute('SELECT pid FROM fproduct')
    data = c.fetchall()
    return data    

def delete_farmer_data(fid):
    c.execute('DELETE FROM farmer WHERE fid="{}"'.format(fid))
    mydb.commit()

def delete_buyer_data(bid):
    c.execute('DELETE FROM buyer WHERE bid="{}"'.format(bid))
    mydb.commit()

def delete_product_data(pid):
    c.execute('DELETE FROM fproduct WHERE pid="{}"'.format(pid))
    mydb.commit()

def get_farmer(fid):
    c.execute('SELECT * FROM farmer WHERE fid="{}"'.format(fid))
    data = c.fetchall()
    return data

def get_buyer(bid):
    c.execute('SELECT * FROM buyer WHERE bid="{}"'.format(bid))
    data = c.fetchall()
    return data

def get_product(pid):
    c.execute('SELECT * FROM fproduct WHERE pid="{}"'.format(pid))
    data = c.fetchall()
    return data

def edit_farmer_data(new_fid, new_fname, new_fusername, new_fpassword, new_femail, new_fmobile, new_faddress,fid, fname, fusername, fpassword, femail, fmobile, faddress):
    c.execute("UPDATE farmer SET fid=%s, fname=%s, fusername=%s, fpassword=%s, femail=%s, fmobile=%s, faddress=%s WHERE fid=%s and fname=%s and fusername=%s and fpassword=%s and femail=%s and fmobile=%s and faddress=%s", (new_fid, new_fname, new_fusername, new_fpassword, new_femail, new_fmobile, new_faddress,fid, fname, fusername, fpassword, femail, fmobile, faddress))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_buyer_data(new_bid, new_bname, new_busername, new_bpassword, new_bemail, new_bmobile, new_baddress,bid, bname, busername, bpassword, bemail, bmobile, baddress):
    c.execute("UPDATE buyer SET bid=%s, bname=%s, busername=%s, bpassword=%s, bemail=%s, bmobile=%s, baddress=%s WHERE bid=%s and bname=%s and busername=%s and bpassword=%s and bemail=%s and bmobile=%s and baddress=%s", (new_bid, new_bname, new_busername, new_bpassword, new_bemail, new_bmobile, new_baddress,bid, bname, busername, bpassword, bemail, bmobile, baddress))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_fproduct_data(new_fid, new_pid, new_product, new_pcat, new_pinfo, new_price,fid, pid, product, pcat, pinfo, price):
    c.execute("UPDATE fproduct SET fid=%s, pid=%s, product=%s, pcat=%s, pinfo=%s, price=%s WHERE fid=%s and pid=%s and product=%s and pcat=%s and pinfo=%s and price=%s", (new_fid, new_pid, new_product, new_pcat, new_pinfo, new_price,fid, pid, product, pcat, pinfo, price))
    mydb.commit()
    data = c.fetchall()
    return data












'''
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS DEALER(dealer_id TEXT, dealer_name TEXT, dealer_city TEXT, dealer_pin TEXT, '
              'dealer_street TEXT)')


def add_data(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street):
    c.execute('INSERT INTO DEALER(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street) VALUES (%s,%s,%s,'
              '%s,%s)',
              (dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM DEALER')
    data = c.fetchall()
    return data


def view_only_dealer_names():
    c.execute('SELECT dealer_name FROM DEALER')
    data = c.fetchall()
    return data


def get_dealer(dealer_name):
    c.execute('SELECT * FROM DEALER WHERE dealer_name="{}"'.format(dealer_name))
    data = c.fetchall()
    return data


def edit_dealer_data(new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street):
    c.execute("UPDATE DEALER SET dealer_id=%s, dealer_name=%s, dealer_city=%s, dealer_pin=%s, dealer_street=%s WHERE "
              "dealer_id=%s and dealer_name=%s and dealer_city=%s and dealer_pin=%s and dealer_street=%s", (new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(dealer_name):
    c.execute('DELETE FROM DEALER WHERE dealer_name="{}"'.format(dealer_name))
    mydb.commit()
'''