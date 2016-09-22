{
  "timestamp" : "2016-09-22T01:23:14.963Z",
  "clusters" : [ {
    "name" : "vtrhyno",
    "version" : "CDH5",
    "services" : [ {
      "name" : "zookeeper",
      "type" : "ZOOKEEPER",
      "config" : {
        "roleTypeConfigs" : [ {
          "roleType" : "SERVER",
          "items" : [ {
            "name" : "zookeeper_server_java_heapsize",
            "value" : "612368384"
          } ]
        } ],
        "items" : [ ]
      },
      "roles" : [ {
        "name" : "zookeeper-SERVER-12c514b2e52b51d6b90c528fd6d0cf35",
        "type" : "SERVER",
        "hostRef" : {
          "hostId" : "i-5f1b6f49"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "b7ng3jn6bl1fo68yx1mnm4fep"
          }, {
            "name" : "serverId",
            "value" : "2"
          } ]
        }
      }, {
        "name" : "zookeeper-SERVER-cfb3bf2e6c800c1a3845818c4f0be462",
        "type" : "SERVER",
        "hostRef" : {
          "hostId" : "i-501b6f46"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "2e6ztdoomdz2xe5b3900aj0h0"
          }, {
            "name" : "serverId",
            "value" : "3"
          } ]
        }
      }, {
        "name" : "zookeeper-SERVER-e7516f7bb5c7b33da6966fbbaf8e0dbf",
        "type" : "SERVER",
        "hostRef" : {
          "hostId" : "i-5c1b6f4a"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "11ink1a4vt6f9ysquntc883oj"
          }, {
            "name" : "serverId",
            "value" : "1"
          } ]
        }
      } ],
      "displayName" : "ZooKeeper"
    }, {
      "name" : "oozie",
      "type" : "OOZIE",
      "config" : {
        "roleTypeConfigs" : [ {
          "roleType" : "OOZIE_SERVER",
          "items" : [ {
            "name" : "oozie_database_host",
            "value" : "ip-10-0-1-121.ec2.internal"
          }, {
            "name" : "oozie_database_password",
            "value" : "oozie_password"
          }, {
            "name" : "oozie_database_type",
            "value" : "mysql"
          }, {
            "name" : "oozie_database_user",
            "value" : "oozie"
          }, {
            "name" : "oozie_java_heapsize",
            "value" : "612368384"
          } ]
        } ],
        "items" : [ {
          "name" : "hive_service",
          "value" : "hive"
        }, {
          "name" : "mapreduce_yarn_service",
          "value" : "yarn"
        }, {
          "name" : "zookeeper_service",
          "value" : "zookeeper"
        } ]
      },
      "roles" : [ {
        "name" : "oozie-OOZIE_SERVER-e7516f7bb5c7b33da6966fbbaf8e0dbf",
        "type" : "OOZIE_SERVER",
        "hostRef" : {
          "hostId" : "i-5c1b6f4a"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "axv5m0r3tya29bffrld4khlbg"
          } ]
        }
      } ],
      "displayName" : "Oozie"
    }, {
      "name" : "hue",
      "type" : "HUE",
      "config" : {
        "roleTypeConfigs" : [ ],
        "items" : [ {
          "name" : "database_host",
          "value" : "ip-10-0-1-121.ec2.internal"
        }, {
          "name" : "database_password",
          "value" : "hue_password"
        }, {
          "name" : "database_type",
          "value" : "mysql"
        }, {
          "name" : "hive_service",
          "value" : "hive"
        }, {
          "name" : "hue_webhdfs",
          "value" : "hdfs-NAMENODE-e7516f7bb5c7b33da6966fbbaf8e0dbf"
        }, {
          "name" : "oozie_service",
          "value" : "oozie"
        }, {
          "name" : "zookeeper_service",
          "value" : "zookeeper"
        } ]
      },
      "roles" : [ {
        "name" : "hue-HUE_SERVER-e7516f7bb5c7b33da6966fbbaf8e0dbf",
        "type" : "HUE_SERVER",
        "hostRef" : {
          "hostId" : "i-5c1b6f4a"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "bh25aty37bahbpznb1heolwci"
          }, {
            "name" : "secret_key",
            "value" : "rCMf7IJcpvK8uByutiYSMkFw97zkm0"
          } ]
        }
      } ],
      "displayName" : "Hue"
    }, {
      "name" : "hdfs",
      "type" : "HDFS",
      "config" : {
        "roleTypeConfigs" : [ {
          "roleType" : "BALANCER",
          "items" : [ {
            "name" : "balancer_java_heapsize",
            "value" : "612368384"
          } ]
        }, {
          "roleType" : "DATANODE",
          "items" : [ {
            "name" : "dfs_data_dir_list",
            "value" : "/dfs/dn"
          }, {
            "name" : "dfs_datanode_du_reserved",
            "value" : "5284468736"
          }, {
            "name" : "dfs_datanode_max_locked_memory",
            "value" : "4294967296"
          } ]
        }, {
          "roleType" : "GATEWAY",
          "items" : [ {
            "name" : "dfs_client_use_trash",
            "value" : "true"
          } ]
        }, {
          "roleType" : "NAMENODE",
          "items" : [ {
            "name" : "dfs_name_dir_list",
            "value" : "/dfs/nn"
          }, {
            "name" : "dfs_namenode_servicerpc_address",
            "value" : "8022"
          } ]
        }, {
          "roleType" : "SECONDARYNAMENODE",
          "items" : [ {
            "name" : "fs_checkpoint_dir_list",
            "value" : "/dfs/snn"
          } ]
        } ],
        "items" : [ {
          "name" : "dfs_ha_fencing_cloudera_manager_secret_key",
          "value" : "XYocHsrzLSB3AAMDiG5j3KHZcyKn8R"
        }, {
          "name" : "fc_authorization_secret_key",
          "value" : "UZaietIiUMft7w1LyEaUJm1uFQ6TXh"
        }, {
          "name" : "http_auth_signature_secret",
          "value" : "uvEdo8RU6NEtuMNGk0bcucAbbKPCwf"
        }, {
          "name" : "rm_dirty",
          "value" : "false"
        }, {
          "name" : "rm_last_allocation_percentage",
          "value" : "25"
        }, {
          "name" : "zookeeper_service",
          "value" : "zookeeper"
        } ]
      },
      "roles" : [ {
        "name" : "hdfs-BALANCER-e7516f7bb5c7b33da6966fbbaf8e0dbf",
        "type" : "BALANCER",
        "hostRef" : {
          "hostId" : "i-5c1b6f4a"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hdfs-DATANODE-12c514b2e52b51d6b90c528fd6d0cf35",
        "type" : "DATANODE",
        "hostRef" : {
          "hostId" : "i-5f1b6f49"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "1xb2vxaee8ablq0w6yxxf1czg"
          } ]
        }
      }, {
        "name" : "hdfs-DATANODE-2b4a35c9a6a999dee5c44996859524cd",
        "type" : "DATANODE",
        "hostRef" : {
          "hostId" : "i-5e1b6f48"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "874r5x7qxfv3zx2o2pr6rz1zq"
          } ]
        }
      }, {
        "name" : "hdfs-DATANODE-cfb3bf2e6c800c1a3845818c4f0be462",
        "type" : "DATANODE",
        "hostRef" : {
          "hostId" : "i-501b6f46"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "cemvqt1mw7uc2zml0nz1lz3rr"
          } ]
        }
      }, {
        "name" : "hdfs-DATANODE-d679b61f90e16864d627a1ecf9f85315",
        "type" : "DATANODE",
        "hostRef" : {
          "hostId" : "i-5d1b6f4b"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "5tei6kjbqjfz1h894ea4d5rey"
          } ]
        }
      }, {
        "name" : "hdfs-NAMENODE-e7516f7bb5c7b33da6966fbbaf8e0dbf",
        "type" : "NAMENODE",
        "hostRef" : {
          "hostId" : "i-5c1b6f4a"
        },
        "config" : {
          "items" : [ {
            "name" : "namenode_id",
            "value" : "46"
          }, {
            "name" : "role_jceks_password",
            "value" : "46fuwf4ut1a9ycfmmk1w2my9n"
          } ]
        }
      }, {
        "name" : "hdfs-SECONDARYNAMENODE-e7516f7bb5c7b33da6966fbbaf8e0dbf",
        "type" : "SECONDARYNAMENODE",
        "hostRef" : {
          "hostId" : "i-5c1b6f4a"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "8posev7spcan0yzhea108lhsn"
          } ]
        }
      } ],
      "displayName" : "HDFS"
    }, {
      "name" : "yarn",
      "type" : "YARN",
      "config" : {
        "roleTypeConfigs" : [ {
          "roleType" : "GATEWAY",
          "items" : [ {
            "name" : "mapred_reduce_tasks",
            "value" : "8"
          }, {
            "name" : "mapred_submit_replication",
            "value" : "2"
          } ]
        }, {
          "roleType" : "JOBHISTORY",
          "items" : [ {
            "name" : "mr2_jobhistory_java_heapsize",
            "value" : "612368384"
          } ]
        }, {
          "roleType" : "NODEMANAGER",
          "items" : [ {
            "name" : "yarn_nodemanager_heartbeat_interval_ms",
            "value" : "100"
          }, {
            "name" : "yarn_nodemanager_local_dirs",
            "value" : "/yarn/nm"
          }, {
            "name" : "yarn_nodemanager_log_dirs",
            "value" : "/yarn/container-logs"
          }, {
            "name" : "yarn_nodemanager_resource_cpu_vcores",
            "value" : "4"
          }, {
            "name" : "yarn_nodemanager_resource_memory_mb",
            "value" : "5250"
          } ]
        }, {
          "roleType" : "RESOURCEMANAGER",
          "items" : [ {
            "name" : "resource_manager_java_heapsize",
            "value" : "612368384"
          }, {
            "name" : "yarn_scheduler_maximum_allocation_mb",
            "value" : "5250"
          }, {
            "name" : "yarn_scheduler_maximum_allocation_vcores",
            "value" : "3"
          } ]
        } ],
        "items" : [ {
          "name" : "hdfs_service",
          "value" : "hdfs"
        }, {
          "name" : "rm_dirty",
          "value" : "false"
        }, {
          "name" : "rm_last_allocation_percentage",
          "value" : "75"
        }, {
          "name" : "yarn_service_cgroups",
          "value" : "false"
        }, {
          "name" : "yarn_service_lce_always",
          "value" : "false"
        }, {
          "name" : "zk_authorization_secret_key",
          "value" : "mpcIbnhv5k7WJVydd2qjvNBdsFj8qa"
        }, {
          "name" : "zookeeper_service",
          "value" : "zookeeper"
        } ]
      },
      "roles" : [ {
        "name" : "yarn-JOBHISTORY-e7516f7bb5c7b33da6966fbbaf8e0dbf",
        "type" : "JOBHISTORY",
        "hostRef" : {
          "hostId" : "i-5c1b6f4a"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "8c5qm1hci3f46eqzltinbj2pk"
          } ]
        }
      }, {
        "name" : "yarn-NODEMANAGER-12c514b2e52b51d6b90c528fd6d0cf35",
        "type" : "NODEMANAGER",
        "hostRef" : {
          "hostId" : "i-5f1b6f49"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "9mhe04pis809gsbqk52rts1bs"
          } ]
        }
      }, {
        "name" : "yarn-NODEMANAGER-2b4a35c9a6a999dee5c44996859524cd",
        "type" : "NODEMANAGER",
        "hostRef" : {
          "hostId" : "i-5e1b6f48"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "1jk6uxspa2vpqeyiggtzxckfz"
          } ]
        }
      }, {
        "name" : "yarn-NODEMANAGER-cfb3bf2e6c800c1a3845818c4f0be462",
        "type" : "NODEMANAGER",
        "hostRef" : {
          "hostId" : "i-501b6f46"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "8cld91v95ktzqk9d7nixccln0"
          } ]
        }
      }, {
        "name" : "yarn-NODEMANAGER-d679b61f90e16864d627a1ecf9f85315",
        "type" : "NODEMANAGER",
        "hostRef" : {
          "hostId" : "i-5d1b6f4b"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "80zmo41oahybg2on2wywkp5m0"
          } ]
        }
      }, {
        "name" : "yarn-RESOURCEMANAGER-e7516f7bb5c7b33da6966fbbaf8e0dbf",
        "type" : "RESOURCEMANAGER",
        "hostRef" : {
          "hostId" : "i-5c1b6f4a"
        },
        "config" : {
          "items" : [ {
            "name" : "rm_id",
            "value" : "53"
          }, {
            "name" : "role_jceks_password",
            "value" : "cy0pt1ncr6yjzhf29uc5aqflm"
          } ]
        }
      } ],
      "displayName" : "YARN (MR2 Included)"
    }, {
      "name" : "hive",
      "type" : "HIVE",
      "config" : {
        "roleTypeConfigs" : [ {
          "roleType" : "HIVEMETASTORE",
          "items" : [ {
            "name" : "hive_metastore_java_heapsize",
            "value" : "612368384"
          } ]
        }, {
          "roleType" : "HIVESERVER2",
          "items" : [ {
            "name" : "hiveserver2_java_heapsize",
            "value" : "612368384"
          }, {
            "name" : "hiveserver2_spark_driver_memory",
            "value" : "966367641"
          }, {
            "name" : "hiveserver2_spark_executor_cores",
            "value" : "4"
          }, {
            "name" : "hiveserver2_spark_executor_memory",
            "value" : "3571397427"
          }, {
            "name" : "hiveserver2_spark_yarn_driver_memory_overhead",
            "value" : "102"
          }, {
            "name" : "hiveserver2_spark_yarn_executor_memory_overhead",
            "value" : "601"
          } ]
        } ],
        "items" : [ {
          "name" : "hive_metastore_database_host",
          "value" : "ip-10-0-1-121.ec2.internal"
        }, {
          "name" : "hive_metastore_database_name",
          "value" : "hive"
        }, {
          "name" : "hive_metastore_database_password",
          "value" : "hive_password"
        }, {
          "name" : "mapreduce_yarn_service",
          "value" : "yarn"
        }, {
          "name" : "zookeeper_service",
          "value" : "zookeeper"
        } ]
      },
      "roles" : [ {
        "name" : "hive-GATEWAY-12c514b2e52b51d6b90c528fd6d0cf35",
        "type" : "GATEWAY",
        "hostRef" : {
          "hostId" : "i-5f1b6f49"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hive-GATEWAY-2b4a35c9a6a999dee5c44996859524cd",
        "type" : "GATEWAY",
        "hostRef" : {
          "hostId" : "i-5e1b6f48"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hive-GATEWAY-cfb3bf2e6c800c1a3845818c4f0be462",
        "type" : "GATEWAY",
        "hostRef" : {
          "hostId" : "i-501b6f46"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hive-GATEWAY-d679b61f90e16864d627a1ecf9f85315",
        "type" : "GATEWAY",
        "hostRef" : {
          "hostId" : "i-5d1b6f4b"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hive-GATEWAY-e7516f7bb5c7b33da6966fbbaf8e0dbf",
        "type" : "GATEWAY",
        "hostRef" : {
          "hostId" : "i-5c1b6f4a"
        },
        "config" : {
          "items" : [ ]
        }
      }, {
        "name" : "hive-HIVEMETASTORE-e7516f7bb5c7b33da6966fbbaf8e0dbf",
        "type" : "HIVEMETASTORE",
        "hostRef" : {
          "hostId" : "i-5c1b6f4a"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "7aw65l2p3bmu2b0jyohpzk82y"
          } ]
        }
      }, {
        "name" : "hive-HIVESERVER2-e7516f7bb5c7b33da6966fbbaf8e0dbf",
        "type" : "HIVESERVER2",
        "hostRef" : {
          "hostId" : "i-5c1b6f4a"
        },
        "config" : {
          "items" : [ {
            "name" : "role_jceks_password",
            "value" : "1yr628wvzrjoygy2gwtkcvply"
          } ]
        }
      } ],
      "displayName" : "Hive"
    } ]
  } ],
  "hosts" : [ {
    "hostId" : "i-5c1b6f4a",
    "ipAddress" : "10.0.1.121",
    "hostname" : "ip-10-0-1-121.ec2.internal",
    "rackId" : "/default",
    "config" : {
      "items" : [ {
        "name" : "host_config_suppression_memory_overcommitted_validator",
        "value" : "true"
      } ]
    }
  }, {
    "hostId" : "i-5d1b6f4b",
    "ipAddress" : "10.0.1.122",
    "hostname" : "ip-10-0-1-122.ec2.internal",
    "rackId" : "/default",
    "config" : {
      "items" : [ ]
    }
  }, {
    "hostId" : "i-5e1b6f48",
    "ipAddress" : "10.0.1.123",
    "hostname" : "ip-10-0-1-123.ec2.internal",
    "rackId" : "/default",
    "config" : {
      "items" : [ ]
    }
  }, {
    "hostId" : "i-5f1b6f49",
    "ipAddress" : "10.0.1.124",
    "hostname" : "ip-10-0-1-124.ec2.internal",
    "rackId" : "/default",
    "config" : {
      "items" : [ ]
    }
  }, {
    "hostId" : "i-501b6f46",
    "ipAddress" : "10.0.1.125",
    "hostname" : "ip-10-0-1-125.ec2.internal",
    "rackId" : "/default",
    "config" : {
      "items" : [ ]
    }
  } ],
  "users" : [ {
    "name" : "__cloudera_internal_user__mgmt-EVENTSERVER-e7516f7bb5c7b33da6966fbbaf8e0dbf",
    "roles" : [ "ROLE_USER" ],
    "pwHash" : "6a2bf913d15a86ba2966fecef5839b72a8bfc780437ab96dfc14e7fd599042f0",
    "pwSalt" : -2013233163859169336,
    "pwLogin" : true
  }, {
    "name" : "__cloudera_internal_user__mgmt-HOSTMONITOR-e7516f7bb5c7b33da6966fbbaf8e0dbf",
    "roles" : [ "ROLE_USER" ],
    "pwHash" : "ae9d3df5e8b9986d9339582d7cfc34a1c2c9a83f91a4eb829fc197b159c41a43",
    "pwSalt" : 8180174009041891860,
    "pwLogin" : true
  }, {
    "name" : "__cloudera_internal_user__mgmt-REPORTSMANAGER-e7516f7bb5c7b33da6966fbbaf8e0dbf",
    "roles" : [ "ROLE_USER" ],
    "pwHash" : "60870c6f45d5833ccc5b6e39a98b1cf69cf3e4cf967e3ad52645a13e25a79375",
    "pwSalt" : 2497564449682592998,
    "pwLogin" : true
  }, {
    "name" : "__cloudera_internal_user__mgmt-SERVICEMONITOR-e7516f7bb5c7b33da6966fbbaf8e0dbf",
    "roles" : [ "ROLE_USER" ],
    "pwHash" : "e9168a22e67fe673045b38fb66520f591ff5ccc79b05b9c592054a799858f17a",
    "pwSalt" : 8903445379660838681,
    "pwLogin" : true
  }, {
    "name" : "admin",
    "roles" : [ "ROLE_LIMITED" ],
    "pwHash" : "de6a0d5d0754cda351c2dfb9d3f85f00b9f38928102fe060a0e4e2516df97fbb",
    "pwSalt" : 1848753709156620765,
    "pwLogin" : true
  }, {
    "name" : "minotaur",
    "roles" : [ "ROLE_CONFIGURATOR" ],
    "pwHash" : "874bf89c350f9699f2f9e7ecb596c6c3e9ed166e91c722e19ba3e5efee99bc65",
    "pwSalt" : -2841871838676465325,
    "pwLogin" : true
  }, {
    "name" : "vtrhyno",
    "roles" : [ "ROLE_ADMIN" ],
    "pwHash" : "c2505fe01b95f43690e0588a1fc05a5e7472d4036a02434217cf04957b67aa82",
    "pwSalt" : 853835619582527066,
    "pwLogin" : true
  } ],
  "versionInfo" : {
    "version" : "5.8.1",
    "buildUser" : "jenkins",
    "buildTimestamp" : "20160722-1141",
    "gitHash" : "a0886a893750079a4dc7f902be22d6f6e63b85a1",
    "snapshot" : false
  },
  "managementService" : {
    "name" : "mgmt",
    "type" : "MGMT",
    "config" : {
      "roleTypeConfigs" : [ {
        "roleType" : "EVENTSERVER",
        "items" : [ {
          "name" : "event_server_heapsize",
          "value" : "612368384"
        } ]
      }, {
        "roleType" : "HOSTMONITOR",
        "items" : [ {
          "name" : "firehose_heapsize",
          "value" : "612368384"
        }, {
          "name" : "firehose_non_java_memory_bytes",
          "value" : "805306368"
        } ]
      }, {
        "roleType" : "REPORTSMANAGER",
        "items" : [ {
          "name" : "headlamp_database_host",
          "value" : "ip-10-0-1-121.ec2.internal"
        }, {
          "name" : "headlamp_database_name",
          "value" : "rman"
        }, {
          "name" : "headlamp_database_password",
          "value" : "rman_password"
        }, {
          "name" : "headlamp_database_user",
          "value" : "rman"
        }, {
          "name" : "headlamp_heapsize",
          "value" : "612368384"
        } ]
      }, {
        "roleType" : "SERVICEMONITOR",
        "items" : [ {
          "name" : "firehose_heapsize",
          "value" : "612368384"
        }, {
          "name" : "firehose_non_java_memory_bytes",
          "value" : "805306368"
        } ]
      } ],
      "items" : [ ]
    },
    "roles" : [ {
      "name" : "mgmt-ALERTPUBLISHER-e7516f7bb5c7b33da6966fbbaf8e0dbf",
      "type" : "ALERTPUBLISHER",
      "hostRef" : {
        "hostId" : "i-5c1b6f4a"
      },
      "config" : {
        "items" : [ {
          "name" : "role_jceks_password",
          "value" : "a3kffr3zwhul237u9ps0vtvse"
        } ]
      }
    }, {
      "name" : "mgmt-EVENTSERVER-e7516f7bb5c7b33da6966fbbaf8e0dbf",
      "type" : "EVENTSERVER",
      "hostRef" : {
        "hostId" : "i-5c1b6f4a"
      },
      "config" : {
        "items" : [ {
          "name" : "role_jceks_password",
          "value" : "m8mzdcf5udct0bd2dbu1zaip"
        } ]
      }
    }, {
      "name" : "mgmt-HOSTMONITOR-e7516f7bb5c7b33da6966fbbaf8e0dbf",
      "type" : "HOSTMONITOR",
      "hostRef" : {
        "hostId" : "i-5c1b6f4a"
      },
      "config" : {
        "items" : [ {
          "name" : "role_jceks_password",
          "value" : "dc9roj1k68etye92cbcewn6ue"
        } ]
      }
    }, {
      "name" : "mgmt-REPORTSMANAGER-e7516f7bb5c7b33da6966fbbaf8e0dbf",
      "type" : "REPORTSMANAGER",
      "hostRef" : {
        "hostId" : "i-5c1b6f4a"
      },
      "config" : {
        "items" : [ {
          "name" : "role_jceks_password",
          "value" : "452qbdq3c6ybaxrvg8p5ef19m"
        } ]
      }
    }, {
      "name" : "mgmt-SERVICEMONITOR-e7516f7bb5c7b33da6966fbbaf8e0dbf",
      "type" : "SERVICEMONITOR",
      "hostRef" : {
        "hostId" : "i-5c1b6f4a"
      },
      "config" : {
        "items" : [ {
          "name" : "role_jceks_password",
          "value" : "eb8yytm0n0618o1vt1e1x2imq"
        } ]
      }
    } ],
    "displayName" : "Cloudera Management Service"
  },
  "managerSettings" : {
    "items" : [ {
      "name" : "CLUSTER_STATS_START",
      "value" : "10/22/2012 13:50"
    }, {
      "name" : "PUBLIC_CLOUD_STATUS",
      "value" : "ON_PUBLIC_CLOUD"
    }, {
      "name" : "REMOTE_PARCEL_REPO_URLS",
      "value" : "https://archive.cloudera.com/cdh5/parcels/{latest_supported}/,https://archive.cloudera.com/cdh4/parcels/latest/,https://archive.cloudera.com/impala/parcels/latest/,https://archive.cloudera.com/search/parcels/latest/,https://archive.cloudera.com/accumulo/parcels/1.4/,https://archive.cloudera.com/accumulo-c5/parcels/latest/,https://archive.cloudera.com/kafka/parcels/latest/,https://archive.cloudera.com/navigator-keytrustee5/parcels/latest/,https://archive.cloudera.com/spark/parcels/latest/,https://archive.cloudera.com/sqoop-connectors/parcels/latest/"
    } ]
  }
}