install python-apt:
  pkg.installed:
    - pkgs:
      - python-apt

install elasticsearch repo key:
  pkgrepo.managed:
    - name: 'deb https://artifacts.elastic.co/packages/6.x/apt stable main'
    - human_name: 'Elastic Beats'
    - file: /etc/apt/sources.list.d/elastic-6.x.list
    - key_url: 'https://artifacts.elastic.co/GPG-KEY-elasticsearch'

install beats:
  pkg.installed:
    - pkgs:
      - metricbeat

copy beats configuration:
  file.managed:
    - name: /etc/metricbeat/metricbeat.yml
    - source: salt://beats/files/metricbeats.yml

start beats:
  service.running:
    - name: metricbeat
    - watch:
      - file: /etc/metricbeat/metricbeat.yml
