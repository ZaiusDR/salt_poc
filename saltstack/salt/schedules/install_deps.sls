install python pip:
  pkg.installed:
    - pkgs:
      - python-pip

install elasticsearch pip module:
  pip.installed:
    - name: elasticsearch

install systat package:
  pkg.installed:
    - pkgs:
      - sysstat
