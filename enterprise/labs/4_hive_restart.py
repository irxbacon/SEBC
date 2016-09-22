import json
import pycurl
from pprint import pprint
from StringIO import StringIO

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.USERPWD, 'vtrhyno:cloudera')
c.setopt(c.URL, 'http://ec2-54-196-123-147.compute-1.amazonaws.com:7180/api/v1/clusters/vtrhyno/services/hive/commands/stop')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

#body = buffer.getvalue()
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
#print(body)

#with open('data.json') as data_file:    
#    data = json.load(data_file)

#pprint(data)

#data["serviceState"]
#data["masks"]["id"]
#data["om_points"]
