```
What is ubertask optimization?
	Ubertask optimization runs "sufficiently small" jobs sequentially within a single JVM. 
	"Small" is defined by the mapreduce.job.ubertask.maxmaps, 
	mapreduce.job.ubertask.maxreduces, and mapreduce.job.ubertask.maxbytes settings.

Where in CM is the Kerberos Security Realm value displayed?
	/cmf/settings#filterdisplayGroup=Kerberos
	/cmf/services/28/config?q=trusted_realms#filterfreeText=trusted_realms
	Additionally, each kerberos aware service has settings for their own kerberos principal

Which CDH service(s) host a property for enabling Kerberos authentication?
	HDF, Yarn, and Zookeper

How do you upgrade the CM agents?
	You can manually update/upgrade the cloudera manager service, shutting it down, getting the latest repository and then using the package manager to update the installation. Then, when you log back in to manager you are given the option of continuing and upgrading the agent packages.
	Alternatively, from the Hosts screen, select "rerun upgrade wizard" and then select "Yes, I would like to upgrade the Cloudera Manager Agent packages now."

Give the tsquery statement used to chart Hue's CPU utilization?
	SELECT cpu_system_rate + cpu_user_rate WHERE entityName = "hue-HUE_SERVER-e7516f7bb5c7b33da6966fbbaf8e0dbf" AND category = ROLE

Name all the roles that make up the Hive service
	Gateway, WebHCat Server, Hive Metastore Server, HiveServer 2

What steps must be completed before integrating Cloudera Manager with Kerberos?
	Kerberos key distribution center (KDC) and realm setup	
	openldap-clients on the Cloudera Manager Server host
	appropriate krb5 packages on ALL hosts (per OS)

```
