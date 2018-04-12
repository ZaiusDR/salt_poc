import elasticsearch
import elasticsearch_dsl

client = elasticsearch.Elasticsearch(['localhost'])

s = elasticsearch_dsl.Search(using=client, index="salt-status_diskusage-v1") \
    .query('match', minion='minion1') \
    .source(['@timestamp',
             'data./etc/hosts.available',
             'data./etc/hosts.total']) \
    .sort("-@timestamp") \
    .extra(size=1)

response = s.execute().to_dict()
source = response['hits']['hits'][0]['_source']
data = source['data']
print('Raw /etc/hosts Disk data from returner:', data)

#############################
# Get Disk Usage
s = elasticsearch_dsl.Search(using=client, index="salt-disk_percent-v1") \
    .query('match', minion='minion2') \
    .source(['@timestamp', 'data./']) \
    .sort("-@timestamp") \
    .extra(size=1)

response = s.execute().to_dict()
source = response['hits']['hits'][0]['_source']
data = source['data']
print('/ Disk data from returner: ', data)

############################
# Get Beats metric
s = elasticsearch_dsl.Search(using=client,
                             index="metricbeat-*") \
    .query('match', beat__name='minion1') \
    .query('match', metricset__name='cpu') \
    .source(['@timestamp', 'system.cpu.iowait']) \
    .sort('-@timestamp') \
    .extra(size=1)
response = s.execute().to_dict()
source = response['hits']['hits'][0]['_source']
data = source['system']['cpu']['iowait']
print('IOWait percentage: ', data)
