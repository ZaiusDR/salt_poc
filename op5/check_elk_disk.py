import argparse
import sys

import elasticsearch
import elasticsearch_dsl


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-E', '--elasticsearch',
                        help='Elasticserach Server IP')
    parser.add_argument('-H', '--hostname', help='Hostname')
    parser.add_argument('-P', '--partition',
                        help='Partition Mountpoint')
    parser.add_argument('-C', '--critical', type=int)
    args = parser.parse_args()

    client = elasticsearch.Elasticsearch([args.elasticsearch])

    s = elasticsearch_dsl.Search(using=client,
                                 index="metricbeat-*") \
        .query('match', beat__name=args.hostname) \
        .query('match', metricset__module='system') \
        .query('match', system__filesystem__mount_point=args.partition) \
        .sort('-@timestamp') \
        .extra(size=1)

    response = s.execute().to_dict()
    if not response['hits']['hits']:
        print('Error! Host not found')
        sys.exit(3)
    partition_data = response['hits']['hits'][0]['_source']['system']['filesystem']
    space_used = partition_data['used']['pct'] * 100
    if space_used > args.critical:
        print('Error! Disk space over threshold (used: {0})'.format(space_used))
        sys.exit(2)
    print('Disk usage: {0}%'.format(space_used))


if __name__ == '__main__':
    main()
