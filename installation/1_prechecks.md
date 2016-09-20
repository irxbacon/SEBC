[root@ip-10-0-1-167 ~]# cat /proc/sys/vm/swappiness
60
[root@ip-10-0-1-167 ~]# 


Added to /etc/sysctl.conf
# Controls vm swappiness 
vm.swappiness=1

Then forced application with 
sysctl -p

checked ulimit -a 
[root@ip-10-0-1-144 ~]# ulimit -a
core file size          (blocks, -c) 0
data seg size           (kbytes, -d) unlimited
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited
pending signals                 (-i) 59564
max locked memory       (kbytes, -l) 64
max memory size         (kbytes, -m) unlimited
open files                      (-n) 1024
pipe size            (512 bytes, -p) 8
POSIX message queues     (bytes, -q) 819200
real-time priority              (-r) 0
stack size              (kbytes, -s) 10240
cpu time               (seconds, -t) unlimited
max user processes              (-u) 59564
virtual memory          (kbytes, -v) unlimited
file locks                      (-x) unlimited
[root@ip-10-0-1-144 ~]# 

Updated with 
 ulimit -n 16384

installed bind-utils (yum)

[root@ip-10-0-1-144 ~]# nslookup 10.0.1.143
Server:		10.0.0.2
Address:	10.0.0.2#53

Non-authoritative answer:
143.1.0.10.in-addr.arpa	name = ip-10-0-1-143.ec2.internal.

Authoritative answers can be found from:

[root@ip-10-0-1-144 ~]# nslookup ip-10-0-1-143.ec2.internal
Server:		10.0.0.2
Address:	10.0.0.2#53

Non-authoritative answer:
Name:	ip-10-0-1-143.ec2.internal
Address: 10.0.1.143

[root@ip-10-0-1-144 ~]# nscd -g
nscd configuration:

              0  server debug level
            21s  server runtime
              5  current number of threads
             32  maximum number of threads
              0  number of times clients had to wait
             no  paranoia mode enabled
           3600  restart internal
              5  reload count

passwd cache:

            yes  cache is enabled
            yes  cache is persistent
            yes  cache is shared
            211  suggested size
         216064  total data pool size
              0  used data pool size
            600  seconds time to live for positive entries
             20  seconds time to live for negative entries
              0  cache hits on positive entries
              0  cache hits on negative entries
              0  cache misses on positive entries
              0  cache misses on negative entries
              0% cache hit rate
              0  current number of cached values
              0  maximum number of cached values
              0  maximum chain length searched
              0  number of delays on rdlock
              0  number of delays on wrlock
              0  memory allocations failed
            yes  check /etc/passwd for changes

group cache:

            yes  cache is enabled
            yes  cache is persistent
            yes  cache is shared
            211  suggested size
         216064  total data pool size
              0  used data pool size
           3600  seconds time to live for positive entries
             60  seconds time to live for negative entries
              0  cache hits on positive entries
              0  cache hits on negative entries
              0  cache misses on positive entries
              0  cache misses on negative entries
              0% cache hit rate
              0  current number of cached values
              0  maximum number of cached values
              0  maximum chain length searched
              0  number of delays on rdlock
              0  number of delays on wrlock
              0  memory allocations failed
            yes  check /etc/group for changes

hosts cache:

            yes  cache is enabled
            yes  cache is persistent
            yes  cache is shared
            211  suggested size
         216064  total data pool size
              0  used data pool size
           3600  seconds time to live for positive entries
             20  seconds time to live for negative entries
              0  cache hits on positive entries
              0  cache hits on negative entries
              0  cache misses on positive entries
              0  cache misses on negative entries
              0% cache hit rate
              0  current number of cached values
              0  maximum number of cached values
              0  maximum chain length searched
              0  number of delays on rdlock
              0  number of delays on wrlock
              0  memory allocations failed
            yes  check /etc/hosts for changes

services cache:

            yes  cache is enabled
            yes  cache is persistent
            yes  cache is shared
            211  suggested size
         216064  total data pool size
              0  used data pool size
          28800  seconds time to live for positive entries
             20  seconds time to live for negative entries
              0  cache hits on positive entries
              0  cache hits on negative entries
              0  cache misses on positive entries
              0  cache misses on negative entries
              0% cache hit rate
              0  current number of cached values
              0  maximum number of cached values
              0  maximum chain length searched
              0  number of delays on rdlock
              0  number of delays on wrlock
              0  memory allocations failed
            yes  check /etc/services for changes

netgroup cache:

            yes  cache is enabled
            yes  cache is persistent
            yes  cache is shared
            211  suggested size
         216064  total data pool size
              0  used data pool size
          28800  seconds time to live for positive entries
             20  seconds time to live for negative entries
              0  cache hits on positive entries
              0  cache hits on negative entries
              0  cache misses on positive entries
              0  cache misses on negative entries
              0% cache hit rate
              0  current number of cached values
              0  maximum number of cached values
              0  maximum chain length searched
              0  number of delays on rdlock
              0  number of delays on wrlock
              0  memory allocations failed
            yes  check /etc/netgroup for changes

SELinux AVC Statistics:

              1  entry lookups
              0  entry hits
              1  entry misses
              0  entry discards
              1  CAV lookups
              0  CAV hits
              0  CAV probes
              1  CAV misses
[root@ip-10-0-1-144 ~]# 


[root@ip-10-0-1-167 ~]# service ntpd status
ntpd (pid  4601) is running...
[root@ip-10-0-1-167 ~]# 


