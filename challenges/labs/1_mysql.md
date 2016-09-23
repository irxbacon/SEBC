```
MYSQL Version --- As noted moved to 5.1 after 5.5 failed to install due to dependencies
	[root@ip-10-0-1-136 ~]# mysql --version
	mysql  Ver 14.14 Distrib 5.1.73, for redhat-linux-gnu (x86_64) using readline 5.1
	[root@ip-10-0-1-136 ~]# 

Show Databases
	mysql> show databases;
	+--------------------+
	| Database           |
	+--------------------+
	| information_schema |
	| hive               |
	| hue                |
	| mysql              |
	| oozie              |
	| rman               |
	| scm                |
	| sentry             |
	| test               |
	+--------------------+
	9 rows in set (0.00 sec)
	
	mysql> 

Show Grants
	mysql> select * from information_schema.USER_PRIVILEGES;
	+------------------------+---------------+-------------------------+--------------+
	| GRANTEE                | TABLE_CATALOG | PRIVILEGE_TYPE          | IS_GRANTABLE |
	+------------------------+---------------+-------------------------+--------------+
	| 'root'@'localhost'     | NULL          | SELECT                  | YES          |
	| 'root'@'localhost'     | NULL          | INSERT                  | YES          |
	| 'root'@'localhost'     | NULL          | UPDATE                  | YES          |
	| 'root'@'localhost'     | NULL          | DELETE                  | YES          |
	| 'root'@'localhost'     | NULL          | CREATE                  | YES          |
	| 'root'@'localhost'     | NULL          | DROP                    | YES          |
	| 'root'@'localhost'     | NULL          | RELOAD                  | YES          |
	| 'root'@'localhost'     | NULL          | SHUTDOWN                | YES          |
	| 'root'@'localhost'     | NULL          | PROCESS                 | YES          |
	| 'root'@'localhost'     | NULL          | FILE                    | YES          |
	| 'root'@'localhost'     | NULL          | REFERENCES              | YES          |
	| 'root'@'localhost'     | NULL          | INDEX                   | YES          |
	| 'root'@'localhost'     | NULL          | ALTER                   | YES          |
	| 'root'@'localhost'     | NULL          | SHOW DATABASES          | YES          |
	| 'root'@'localhost'     | NULL          | SUPER                   | YES          |
	| 'root'@'localhost'     | NULL          | CREATE TEMPORARY TABLES | YES          |
	| 'root'@'localhost'     | NULL          | LOCK TABLES             | YES          |
	| 'root'@'localhost'     | NULL          | EXECUTE                 | YES          |
	| 'root'@'localhost'     | NULL          | REPLICATION SLAVE       | YES          |
	| 'root'@'localhost'     | NULL          | REPLICATION CLIENT      | YES          |
	| 'root'@'localhost'     | NULL          | CREATE VIEW             | YES          |
	| 'root'@'localhost'     | NULL          | SHOW VIEW               | YES          |
	| 'root'@'localhost'     | NULL          | CREATE ROUTINE          | YES          |
	| 'root'@'localhost'     | NULL          | ALTER ROUTINE           | YES          |
	| 'root'@'localhost'     | NULL          | CREATE USER             | YES          |
	| 'root'@'localhost'     | NULL          | EVENT                   | YES          |
	| 'root'@'localhost'     | NULL          | TRIGGER                 | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | SELECT                  | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | INSERT                  | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | UPDATE                  | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | DELETE                  | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | CREATE                  | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | DROP                    | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | RELOAD                  | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | SHUTDOWN                | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | PROCESS                 | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | FILE                    | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | REFERENCES              | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | INDEX                   | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | ALTER                   | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | SHOW DATABASES          | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | SUPER                   | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | CREATE TEMPORARY TABLES | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | LOCK TABLES             | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | EXECUTE                 | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | REPLICATION SLAVE       | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | REPLICATION CLIENT      | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | CREATE VIEW             | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | SHOW VIEW               | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | CREATE ROUTINE          | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | ALTER ROUTINE           | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | CREATE USER             | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | EVENT                   | YES          |
	| 'root'@'ip-10-0-1-136' | NULL          | TRIGGER                 | YES          |
	| 'root'@'127.0.0.1'     | NULL          | SELECT                  | YES          |
	| 'root'@'127.0.0.1'     | NULL          | INSERT                  | YES          |
	| 'root'@'127.0.0.1'     | NULL          | UPDATE                  | YES          |
	| 'root'@'127.0.0.1'     | NULL          | DELETE                  | YES          |
	| 'root'@'127.0.0.1'     | NULL          | CREATE                  | YES          |
	| 'root'@'127.0.0.1'     | NULL          | DROP                    | YES          |
	| 'root'@'127.0.0.1'     | NULL          | RELOAD                  | YES          |
	| 'root'@'127.0.0.1'     | NULL          | SHUTDOWN                | YES          |
	| 'root'@'127.0.0.1'     | NULL          | PROCESS                 | YES          |
	| 'root'@'127.0.0.1'     | NULL          | FILE                    | YES          |
	| 'root'@'127.0.0.1'     | NULL          | REFERENCES              | YES          |
	| 'root'@'127.0.0.1'     | NULL          | INDEX                   | YES          |
	| 'root'@'127.0.0.1'     | NULL          | ALTER                   | YES          |
	| 'root'@'127.0.0.1'     | NULL          | SHOW DATABASES          | YES          |
	| 'root'@'127.0.0.1'     | NULL          | SUPER                   | YES          |
	| 'root'@'127.0.0.1'     | NULL          | CREATE TEMPORARY TABLES | YES          |
	| 'root'@'127.0.0.1'     | NULL          | LOCK TABLES             | YES          |
	| 'root'@'127.0.0.1'     | NULL          | EXECUTE                 | YES          |
	| 'root'@'127.0.0.1'     | NULL          | REPLICATION SLAVE       | YES          |
	| 'root'@'127.0.0.1'     | NULL          | REPLICATION CLIENT      | YES          |
	| 'root'@'127.0.0.1'     | NULL          | CREATE VIEW             | YES          |
	| 'root'@'127.0.0.1'     | NULL          | SHOW VIEW               | YES          |
	| 'root'@'127.0.0.1'     | NULL          | CREATE ROUTINE          | YES          |
	| 'root'@'127.0.0.1'     | NULL          | ALTER ROUTINE           | YES          |
	| 'root'@'127.0.0.1'     | NULL          | CREATE USER             | YES          |
	| 'root'@'127.0.0.1'     | NULL          | EVENT                   | YES          |
	| 'root'@'127.0.0.1'     | NULL          | TRIGGER                 | YES          |
	| ''@'localhost'         | NULL          | USAGE                   | NO           |
	| ''@'ip-10-0-1-136'     | NULL          | USAGE                   | NO           |
	+------------------------+---------------+-------------------------+--------------+
	83 rows in set (0.00 sec)
		
	mysql> 

```
