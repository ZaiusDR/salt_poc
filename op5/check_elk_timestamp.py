import argparse
import datetime
import sys

import elasticsearch
import elasticsearch_dsl


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-E', '--elasticsearch',
                        help='Elasticserach Server IP')
    parser.add_argument('-H', '--hostname', help='Hostname')
    parser.add_argument('-T', '--maxtime', type=int,
                        help='Max time since last received metric')
    args = parser.parse_args()

    client = elasticsearch.Elasticsearch([args.elasticsearch])

    s = elasticsearch_dsl.Search(using=client,
                                 index="metricbeat-*") \
        .query('match', beat__name=args.hostname) \
        .query('match', metricset__module='system') \
        .source(['@timestamp']) \
        .sort('-@timestamp') \
        .extra(size=1)

    response = s.execute().to_dict()
    if not response['hits']['hits']:
        print('Error! Host not found')
        sys.exit(3)
    timestamp = response['hits']['hits'][0]['_source']['@timestamp']
    last_write = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
    if last_write < datetime.datetime.now() - datetime.timedelta(seconds=args.maxtime):
        print('Error! No data received in last {0} seconds!'.format(args.maxtime))
        sys.exit(2)
    print('OK - Last data received at {0}'.format(last_write))


if __name__ == '__main__':
    main()
