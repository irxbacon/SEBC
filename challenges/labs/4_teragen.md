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

```

