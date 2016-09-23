[cloudera-manager]
# Packages for Cloudera Manager, Version 5, on RedHat or CentOS 5 x86_64
name=Cloudera Manager
baseurl=https://archive.cloudera.com/cm5/redhat/5/x86_64/cm/5.8.0/
gpgkey =https://archive.cloudera.com/cm5/redhat/5/x86_64/cm/RPM-GPG-KEY-cloudera
gpgcheck = 1


MYSQL Grant
	grant all on *.* to 'scm'@'54.227.209.61' identified by 'scm';
