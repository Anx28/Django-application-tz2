

Structure:
```
├── files
│   └── my_healthcheck
│       ├── urls.py
│       └── views.py
├── inventory.ini
├── readme.md
├── site.yml
└── templates
    ├── gunicorn.service.j2
    └── nginx.conf.j2

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


