# RHCE

## Vault

```
---
- name: Deploy DBA password file
  hosts: dbservers
  become: yes

  tasks:
   - name: Create and pgapass file
     lineinfile:
      line: 'LinuxAcad'
      create: yes
      owner: dba
      group: dba
      mode: 0600
      path: /home/dba/.pgpass

ansible-vault encrypt dba-pass.yml

ansible-playbook --ask-vault-pass dba-pass.yml
```

## Templates

```
<Directory />
   AllowOverride none
   Require all denied
</Directory>

DocumentRoot "{{ webdir }}html"

<Directory "{{ webdir }}">
   AllowOverride None
   Require all granted
</Directory>

---
- name: Template playbook
  hosts: webservers
  become: yes
  vars:
   webdir: '/opt/'

  tasks:
   - name: Deploy the web template
     template:
      src: /root/httpd.template
      dest: /etc/httpd/conf/httpd.conf

ansible-playbook template.yml
```

## Modules

### Scheduled tasks

```
- name: Cron jobs
     hosts: all
     become: yes

     tasks:
     - cron:
        name: "Weekly YUM Update"
        special_time: weekly
        job: "/usr/bin/yum update -y"

     - cron:
        name: "Reboot Status"
        special_time: reboot
        job: "/usr/bin/status"

     - cron:
        name: "Faillock Report"
        job: /usr/bin/faillock_report
        weekday: "1,3,5"
        minute: "30"
        hour: "7"

ansible-playbook cron.yml
```


