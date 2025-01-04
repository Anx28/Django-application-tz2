

Structure:
```
.
├── site.yml
├── inventory.ini
└── templates/
    ├── nginx.conf.j2
    └── gunicorn.service.j2
```

Running the playbook:
```
ansible-playbook -i inventory.ini site.yml 

```

Verifying the deployment:
```
# Check component status
curl http://your_server_ip/app_healthcheck/
```

Expected response:
```
{
    "status": "healthy",
    "components": {
        "postgresql": "up",
        "nginx": "up",
        "django": "up"
    }
}
```
![image](https://github.com/user-attachments/assets/1c78de58-b746-4ce9-9527-22ab35c18918)

