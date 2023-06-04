# Databases

## Berkeley DB

```
python
>>> import bsddb
>>> db = bsddb.btopen('demo.db', 'r')
>>> print ('The name of student 2 is ' + db['2'])
>>> db.close()
```

## CSV

```
awk -F, '{ print $2 }'
```

## XML

```
sudo yum -y install java
curl -O -L http://files.basex.org/releases/9.3.2/BaseX932.jar
java -cp BaseX932.jar org.basex.BaseX
CREATE DB demo demo.xml
xquery /users/user[ID=1]/Name
xquery /users/user[Name="Sue"]/ID
```

## Json

```
curl -O -L https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64
chmod +x jq-linux64
./jq-linux64 '.users[].Department' demo.json
./jq-linux64 '.users[1].Name,.users[1].ID' demo.json
```

## PostgreSQL

```
sudo -u postgres psql demo
demo=# \dt
demo=# \dt+
demo=# \d+ users
demo=# \! clear
select name from users where ID = 3;
select ID from users where name = 'David';
```

## MariaDB

```
sudo mysql -h localhost -u root demo 
show tables;
DESCRIBE users;
select name from users where ID = 3;
select ID from users where name = "David";
```

## Couchbase

```
/opt/couchbase/bin/couchbase-cli

/opt/couchbase/bin/cbq

doc0; name:David, department:Engineering
doc1; name:Clay, department:HR
doc2; name:Sue, department:Sales
doc3; name:Betty, department:Marketing

/opt/couchbase/bin/couchbase-cli bucket-create -c 127.0.0.1:8091 --username Administrator --password xx  --bucket demo-bucket --bucket-type couchbase --bucket-ramsize 512

/opt/couchbase/bin/cbq -e http://localhost:8091 -u=Administrator
cbq> INSERT INTO `demo-bucket` ( KEY, VALUE ) Values ( "doc0",{"name": "David", "department": "Engineering"} ) RETURNING META().id as docid, *;

CREATE PRIMARY INDEX `demo-index` ON `demo-bucket`;
SELECT * FROM `demo-bucket` WHERE name= "Betty";
UPDATE `demo-bucket` set department = "Sales" WHERE name= "Betty";
SELECT * FROM `demo-bucket` WHERE name= "Betty";
```

## MongoBD

```
mongo
> use demo;
> db.inventory.insertMany([
    { id: 0, name: "David", department: "Engineering", expensecode: 200 },
    { id: 1, name: "Clay", department: "HR", expensecode: 100 },
    { id: 2, name: "Sue", department: "Sales", expensecode: 300 },
    { id: 3, name: "Betty", department: "Marketing", expensecode: 400 },
])
> db.inventory.find( {} )
> db.inventory.updateOne(
    { name: "Betty" },
    {
      $set: { department: "HR" }
    }
)

> db.inventory.find( { name: "Betty" } )
```

## Cassandra

```
/bin/cqlsh
CREATE KEYSPACE demo WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 1};
USE demo;
CREATE TABLE users (ID int PRIMARY KEY, Name text, Department text, ExpenseCode int);
DESCRIBE users;
INSERT INTO users (ID, Name, Department, ExpenseCode) values (0, 'David', 'Engineering', 200);
INSERT INTO users (ID, Name, Department, ExpenseCode) values (1, 'Clay', 'HR', 100);
INSERT INTO users (ID, Name, Department, ExpenseCode) values (2, 'Sue', 'Sales', 300);
INSERT INTO users (ID, Name, Department, ExpenseCode) values (3, 'Betty', 'Marketing', 400);
SELECT * from users;
SELECT Name, Department from users;
```

## PostgreSQL replication

```
# Replica
sudo -u postgres psql
\l
create database demo; # ERROR

# Primary
sudo -u postgres psql
create database demo; # OK
\l

# Replica
sudo -u postgres psql
\l
```

