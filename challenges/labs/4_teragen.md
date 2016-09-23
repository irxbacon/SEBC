```
Teragen statement

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-examples.jar teragen -D dfs.block.size=67108864 51200000 /user/christie/tgen64


Time output
Bytes Written=5120000000

real    3m3.251s
user    0m9.463s
sys     0m1.161s


[christie@ip-10-0-1-135 hadoop-mapreduce]$ hdfs dfs -ls /user/christie/tgen64
Found 3 items
-rw-r--r--   3 christie supergroup          0 2016-09-23 15:53 /user/christie/tgen64/_SUCCESS
-rw-r--r--   3 christie supergroup 2560000000 2016-09-23 15:53 /user/christie/tgen64/part-m-00000
-rw-r--r--   3 christie supergroup 2560000000 2016-09-23 15:53 /user/christie/tgen64/part-m-00001
[christie@ip-10-0-1-135 hadoop-mapreduce]$ 


Number of blocks : 78


Status: HEALTHY
 Total size:    5120000000 B
 Total dirs:    1
 Total files:   3
 Total symlinks:                0
 Total blocks (validated):      78 (avg. block size 65641025 B)
 Minimally replicated blocks:   78 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    3
 Average block replication:     3.0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)
 Number of data-nodes:          4
 Number of racks:               1
FSCK ended at Fri Sep 23 15:55:57 UTC 2016 in 6 milliseconds

```

