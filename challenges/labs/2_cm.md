```
[cloudera-manager]
# Packages for Cloudera Manager, Version 5, on RedHat or CentOS 5 x86_64
name=Cloudera Manager
baseurl=https://archive.cloudera.com/cm5/redhat/5/x86_64/cm/5.8.0/
gpgkey =https://archive.cloudera.com/cm5/redhat/5/x86_64/cm/RPM-GPG-KEY-cloudera
gpgcheck = 1


MYSQL Grant
	grant all on *.* to 'scm'@'54.227.209.61' identified by 'scm';

Head output 

	[root@ip-10-0-1-135 cloudera-scm-server]# head -1 /var/log/cloudera-scm-server/cloudera-scm-server.log
	2016-09-23 14:52:44,880 INFO main:com.cloudera.server.cmf.Main: Starting SCM Server. JVM Args: [-Dlog4j.configuration=file:/etc/cloudera-scm-server/log4j.properties, -Dfile.encoding=UTF-8, -Dcmf.root.logger=INFO,LOGFILE, -Dcmf.log.dir=/var/log/cloudera-scm-server, -Dcmf.log.file=cloudera-scm-server.log, -Dcmf.jetty.threshhold=WARN, -Dcmf.schema.dir=/usr/share/cmf/schema, -Djava.awt.headless=true, -Djava.net.preferIPv4Stack=true, -Dpython.home=/usr/share/cmf/python, -XX:+UseConcMarkSweepGC, -XX:+UseParNewGC, -XX:+HeapDumpOnOutOfMemoryError, -Xmx2G, -XX:MaxPermSize=256m, -XX:+HeapDumpOnOutOfMemoryError, -XX:HeapDumpPath=/tmp, -XX:OnOutOfMemoryError=kill -9 %p], Args: [], Version: 5.8.0 (#42 built by jenkins on 20160714-1246 git: d08ac14ff050a108864fab00205c12e0d4043132)
	[root@ip-10-0-1-135 cloudera-scm-server]# 

Jetty Grep
	[root@ip-10-0-1-135 cloudera-scm-server]# grep "Started Jetty server" /var/log/cloudera-scm-server/cloudera-scm-server.log
	2016-09-23 14:54:12,903 INFO WebServerImpl:com.cloudera.server.cmf.WebServerImpl: Started Jetty server.
	[root@ip-10-0-1-135 cloudera-scm-server]# 

```
