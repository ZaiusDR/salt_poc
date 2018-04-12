install postgresql:
  pkg.installed:
    - pkgs:
      - postgresql

start postgresql:
  service.running:
    - name: postgresql

copy beats postgres configuration file:
  file.managed:
    - name: /etc/metricbeat/postgresql.yml
    - source: salt://beats/files/postgresql.yml

set postgresql user:
  postgres_user.present:
    - name: poc_user
    - password: poc_pass

restart beats service for postgres changes:
  service.running:
    - name: metricbeat
    - watch:
      - file: /etc/metricbeat/postgresql.yml
