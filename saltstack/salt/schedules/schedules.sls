create system disk report schedule:
  schedule.present:
    - name: raw_disk_info
    - function: status.diskusage
    - job_args:
      - ext?
    - seconds: 30
    - returner: elasticsearch

create system disk human report schedule:
  schedule.present:
    - name: human_disk_info
    - function: disk.percent
    - seconds: 30
    - returner: elasticsearch

create system memory report schedule:
  schedule.present:
    - name: memory_report
    - function: status.meminfo
    - seconds: 30
    - returner: elasticsearch
