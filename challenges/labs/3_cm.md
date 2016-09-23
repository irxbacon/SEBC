```
Grant commands

	grant all on rman.* TO 'rman'@'%' IDENTIFIED BY 'rman_password';
	grant all on hive.* TO 'hive'@'%' IDENTIFIED BY 'hive_password';
	grant all on oozie.* TO 'oozie'@'%' IDENTIFIED BY 'oozie_password';
	grant all on hue.* TO 'hue'@'%' IDENTIFIED BY 'hue_password';
	grant all on sentry.* TO 'sentry'@'%' IDENTIFIED BY 'sentry_password';

Show Grants
mysql> show grants for rman;
+-----------------------------------------------------------------------------------------------------+
| Grants for rman@%                                                                                   |
+-----------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'rman'@'%' IDENTIFIED BY PASSWORD '*AEF345BFE495D8E678EA9D3D5708FD110AD2F08E' |
| GRANT ALL PRIVILEGES ON `rman`.* TO 'rman'@'%'                                                      |
+-----------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)

mysql> show grants for hive;
+-----------------------------------------------------------------------------------------------------+
| Grants for hive@%                                                                                   |
+-----------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'hive'@'%' IDENTIFIED BY PASSWORD '*8AC2E431CC7A9F2C4C0E51A65B8D8175892D9F22' |
| GRANT ALL PRIVILEGES ON `hive`.* TO 'hive'@'%'                                                      |
+-----------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)

mysql> show grants for oozie;
+------------------------------------------------------------------------------------------------------+
| Grants for oozie@%                                                                                   |
+------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'oozie'@'%' IDENTIFIED BY PASSWORD '*81A1BB46F79EBD0AA76E6EFAA31D62458CFCAF62' |
| GRANT ALL PRIVILEGES ON `oozie`.* TO 'oozie'@'%'                                                     |
+------------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)

mysql> 

Output for hadoop ls
[root@ip-10-0-1-135 cloudera-scm-server]# hadoop fs -ls /user
Found 6 items
drwxr-xr-x   - christie supergroup          0 2016-09-23 15:32 /user/christie
drwxrwxrwx   - mapred   hadoop              0 2016-09-23 15:30 /user/history
drwxrwxr-t   - hive     hive                0 2016-09-23 15:31 /user/hive
drwxrwxr-x   - hue      hue                 0 2016-09-23 15:31 /user/hue
drwxrwxr-x   - oozie    oozie               0 2016-09-23 15:32 /user/oozie
drwxr-xr-x   - weiner   supergroup          0 2016-09-23 15:33 /user/weiner
[root@ip-10-0-1-135 cloudera-scm-server]# 

Hadoop classpath
[root@ip-10-0-1-135 cloudera-scm-server]# hadoop classpath
/etc/hadoop/conf:/usr/lib/hadoop/lib/*:/usr/lib/hadoop/.//*:/usr/lib/hadoop-hdfs/./:/usr/lib/hadoop-hdfs/lib/*:/usr/lib/hadoop-hdfs/.//*:/usr/lib/hadoop-yarn/lib/*:/usr/lib/hadoop-yarn/.//*:/usr/lib/hadoop-mapreduce/lib/*:/usr/lib/hadoop-mapreduce/.//*
[root@ip-10-0-1-135 cloudera-scm-server]# 

Item from API call
"items" : [ {
    "hostId" : "i-e1bdcef7",
    "ipAddress" : "10.0.1.133",
    "hostname" : "ip-10-0-1-133.ec2.internal",
    "rackId" : "/default",
    "hostUrl" : "http://ip-10-0-1-135.ec2.internal:7180/cmf/hostRedirect/i-e1bdcef7",
    "maintenanceMode" : false,
    "maintenanceOwners" : [ ],
    "commissionState" : "COMMISSIONED",
    "numCores" : 4,
    "numPhysicalCores" : 4,
    "totalPhysMemBytes" : 15740305408
  },



Missed the "install hive sample data" until after time was called.  I intend to leave mine up and mess with it later.


```
