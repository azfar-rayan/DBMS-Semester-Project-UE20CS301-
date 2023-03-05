CREATE TABLE buyer (
  bid int(100) NOT NULL,
  bname varchar(100) NOT NULL,
  busername varchar(100) NOT NULL,
  bpassword varchar(100) NOT NULL,
  bemail varchar(100) NOT NULL,
  bmobile varchar(100) NOT NULL,
  baddress text NOT NULL
)
INSERT INTO buyer (bid, bname, busername, bpassword, bemail, bmobile, baddress) VALUES
(1, 'buyer 1', 'buyer1', 'buyer1', 'mno@gmail.com', '7878787878', 'chennai'),
(2, 'buyer 2', 'buyer2', 'buyer2', 'msn@gmail.com', '7878787879', 'kolar');


CREATE TABLE farmer (
  fid int(255) NOT NULL,
  fname varchar(255) NOT NULL,
  fusername varchar(255) NOT NULL,
  fpassword varchar(255) NOT NULL,
  femail varchar(255) NOT NULL,
  fmobile varchar(255) NOT NULL,
  faddress text NOT NULL
)
INSERT INTO farmer (fid, fname, fusername, fpassword, femail, fmobile, faddress) VALUES
(1, 'azfar rayan', 'rayan', 'rayan_pass', 'xyz@gmail.com', '8600611198', 'abcde');
INSERT INTO farmer (fid, fname, fusername, fpassword, femail, fmobile, faddress) VALUES
(3, 'rohan kumar', 'rohan', 'rohan_pass', 'farm@yahoo.com', '7560934321', 'bijapur');



CREATE TABLE fproduct (
  fid int(255) NOT NULL,
  pid int(255) NOT NULL,
  product varchar(255) NOT NULL,
  pcat varchar(255) NOT NULL,
  pinfo varchar(255) NOT NULL,
  price float NOT NULL
)

INSERT INTO fproduct (fid, pid, product, pcat, pinfo, price) VALUES
(1, 27, 'Mango', 'Fruit', 'fresh mango', 500),
(1, 28, 'Ladyfinger', 'Vegetable', 'tasty ladyfinger', 1000),
(2, 29, 'Bajra', 'Grains', 'healthy bajra', 400),
(2, 30, 'Banana', 'Fruit', 'fresh Jalgaon banana', 400);
INSERT INTO fproduct (fid, pid, product, pcat, pinfo, price) VALUES (3, 31, 'Corn', 'Grains', 'Premium Export Quality Corn', 350);
INSERT INTO fproduct (fid, pid, product, pcat, pinfo, price) VALUES (3, 32, 'Watermelon', 'Fruit', 'Organic Watermelons', 255);
INSERT INTO fproduct (fid, pid, product, pcat, pinfo, price) VALUES (3, 33, 'Nagpur Oranges', 'Fruit', 'Juicy Oranges', 500),
    -> (1, 34, 'Sweet Dates', 'Fruit', 'Imported Dates', 325),
    -> (1, 35, 'Bitter Gourd', 'Vegetable', 'Fresh', 90),
    -> (2, 36, 'Potato', 'Vegetable', 'Fresh', 60),
    -> (2, 37, 'Tomato', 'Fruit', 'Fresh', 90),
    -> (3, 38, 'Carrot', 'Vegetable', 'Organic & Fresh', 100);


CREATE TABLE mycart (
  bid int(10) NOT NULL,
  pid int(10) NOT NULL
)
INSERT INTO mycart (bid, pid) VALUES (1, 27),(1, 30);

'''
CREATE TABLE transaction(
  tid int(10) NOT NULL,
  bid int(10) NOT NULL,
  pid int(10) NOT NULL, 
  bname varchar(255) NOT NULL,
  city varchar(255) NOT NULL,
  mobile varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  pincode varchar(255) NOT NULL,
  addr varchar(255) NOT NULL
)
INSERT INTO transaction (tid, bid, pid, name, city, mobile, email, pincode, addr) VALUES
(1, 3, 28, 'sa,j,cns', 'sajc', 'sajch', 'kmendki98@gmail.com', 'sacu', 'ckaskjc');
'''
------------------------------------------
-- JOIN STATEMENTS

select f.fid, f.fname, f.fmobile, f.faddress
    -> from farmer as f left outer join mycart as c
    -> on f.fid=c.fid;

select b.bid, b.bname, b.bmobile, b.baddress
    -> from (( buyer as b
    -> join mycart as mc on mc.bid=b.bid)
    -> join fproduct as f on f.pid=mc.pid)
    -> where f.pcat='Fruit';

select f.fid, f.fname, f.faddress, p.product,p.pcat
    -> from (( fproduct as p
    -> inner join mycart as c on c.pid= p.pid)
    -> inner join farmer as f on f.fid = c.bid)
    -> where p.pcat = "Vegetable";

select b.bid, b.bname, fp.product, fp.pcat, fp.price
    -> from (( fproduct as fp
    -> inner join mycart as c on c.pid = fp.pid)
    -> inner join buyer as b on b.bid = c.bid)
    -> where fp.price > 200;

-----------------------------------------------------------------------

-- AGGREGATE FUNCTIONS
select bid, count(pid) as num_items
    -> from mycart group by bid;

select pid, product, pinfo, MAX(price) as maximum_cost
    -> from fproduct;

select pcat, AVG(price) as avg_cost
    -> from fproduct group by pcat;

------------------------------------------------------------------------

--SET OPERATIONS
select b.bid,b.bname,b.baddress,mc.pid, mc.fid
    -> from mycart as mc inner join buyer as b on mc.bid=b.bid inner join fproduct as fp on fp.pid=mc.pid
    -> where fp.price>(select AVG(price) from fproduct)
    -> UNION
    -> select b.bid,b.bname,b.baddress,mc.pid, mc.fid
    -> from mycart as mc inner join buyer as b on mc.bid=b.bid inner join fproduct as fp on fp.pid=mc.pid
    -> where b.bid>2;

select mc.bid, fp.product, fp.pinfo, fp.price
    -> from fproduct as fp inner join mycart as mc on mc.pid=fp.pid where fp.price>100
    -> INTERSECT
    -> select mc.bid, fp.product, fp.pinfo, fp.price
    -> from fproduct as fp inner join mycart as mc on mc.pid=fp.pid where fp.pcat='Fruit';

select mc.bid, fp.product, fp.pinfo,fp.pcat,fp.price
    -> from fproduct as fp inner join mycart as mc on mc.pid=fp.pid where fp.price>250
    -> EXCEPT
    -> select mc.bid, fp.product, fp.pinfo,fp.pcat,fp.price
    -> from fproduct as fp inner join mycart as mc on mc.pid=fp.pid where fp.pcat='Grains';

select f.fid, f.fname, f.femail, mc.pid
    -> from farmer as f inner join mycart as mc where f.fid>1
    -> INTERSECT
    -> select f.fid, f.fname, f.femail, mc.pid
    -> from farmer as f inner join mycart as mc where mc.bid=2 OR mc.bid=3;

---------------------------------------------------------------------------------------------
--FUNCTIONS
DELIMITER $$

CREATE FUNCTION final_price(p_price FLOAT)
RETURNS FLOAT
DETERMINISTIC
BEGIN 
DECLARE taxed_price FLOAT;
IF  p_price >= 100 THEN 
SET taxed_price = p_price+(0.2*p_price);
ELSE
SET  taxed_price = p_price+(0.02*p_price);
END IF;
RETURN taxed_price;
END; $$

DELIMITER ;

--PROCEDURE
DELIMITER $$

CREATE PROCEDURE cost(
IN t_price INT,
OUT output_fid INT(11),
OUT output_product varchar(50),
OUT output_pcat varchar(50),
OUT output_price float)
BEGIN
SELECT fid, product, pcat, price
INTO output_fid, output_product, output_pcat, output_price
FROM fproduct WHERE fid=1 AND price<= t_price;
END;
$$
DELIMITER ;
CALL check(100, @fid, @product, @pcat, @price);
SELECT @fid, @product, @pcat, @price;
------------------------------------------------------------------
--TRIGGER
DELIMITER $$
CREATE TRIGGER price_update
AFTER UPDATE
ON mycart FOR EACH ROW
BEGIN
UPDATE fproduct SET fid = fid-old.fid WHERE fproduct.pid=new.pid;
UPDATE fproduct SET fid = fid+old.fid WHERE fproduct.pid=new.pid;
END; $$
DELIMITER;

UPDATE fproduct set fid=1
WHERE pid=32;
------------------------------------------------------------------
--CURSOR
DELIMITER $$
CREATE PROCEDURE backup_farmers()
BEGIN
DECLARE used INT DEFAULT 0;
DECLARE fid INT(11);
DECLARE fname varchar(255);
DECLARE fusername varchar(255);
DECLARE fpassword varchar(255);
DECLARE femail varchar(255);
DECLARE fmobile varchar(255);
DECLARE faddress text;
DECLARE farmer_cursor CURSOR FOR SELECT * FROM farmer;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET used = 1;
OPEN farmer_cursor;
label: LOOP
FETCH farmer_cursor INTO fid, fname, fusername, fpassword, femail, fmobile, faddress;
INSERT INTO backup_farmers VALUES(fid, fname, fusername, fpassword, femail, fmobile, faddress);
IF used = 1 THEN LEAVE label;
END IF;
END LOOP;
CLOSE farmer_cursor;
END $$
DELIMITER ;

CREATE TABLE backup_farmers (
  fid int(255),
  fname varchar(255),
  fusername varchar(255),
  fpassword varchar(255),
  femail varchar(255),
  fmobile varchar(255),
  faddress text
)
SELECT * FROM backup_farmers;
CALL backup_farmers();
SELECT * FROM backup_farmers;
--------------------------------------------------------------------
