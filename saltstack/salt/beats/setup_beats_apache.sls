install apache:
  pkg.installed:
    - pkgs:
      - apache2

start apache:
  service.running:
    - name: apache2

activate metricbeat apache module:
  file.copy:
    - name: /etc/metricbeat/modules.d/apache.yml
    - source: /etc/metricbeat/modules.d/apache.yml.disabled

restart beats service:
  cmd.run:
    - name: /etc/init.d/metricbeat restart
