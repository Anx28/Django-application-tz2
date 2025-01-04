

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


