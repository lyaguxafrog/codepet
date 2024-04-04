# CodePET

## About
<!-- Yor description here -->

## Stack:
* Django
* DRF
* PostgreSQL
* Docker + Docker-compose
* Gunicorn
---
## Develop:

To work with the project, you need to install [vscode](https://code.visualstudio.com/) and [vscode-remote-containers](https://code.visualstudio.com/docs/remote/containers).

### Config
To generate a config:
```bash
./deploy.sh config
```

### Environment variables
 * `SECRET_KEY` - Django secret key. For generate new once, you can use service https://djecrety.ir/
 * `DEBUG` - Flag to tell django work on debug mode or not.
## Develop
Для разработки используются [Devcontainers](https://containers.dev).
* `DB_NAME` - PostgreSQL db name.
* `DB_USER` - PostgreSQL db user.
* `DB_PASSWORD` - PostgeSQL db password.


### Codding

For developing backend with django, open django project in vscode and reopen it in container.


```bash
code kernel
```

![reopen](https://github.com/lyaguxafrog/python-backend-devcontainers/blob/release/docs/pics/reopen.png?raw=true)

For migrate:
```bash
./manage.sh migrate
```

For create new django app:
```bash
./manage.sh app
```
./deploy.sh 
```

On local machine app will running on http://0.0.0.0/


&copy; Gen by [PBD](https://lyaguxafrog/python-backend-devcontainers) with 💚
