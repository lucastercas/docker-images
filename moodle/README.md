![Docker Image CI](https://github.com/lucastercas/docker-moodle/workflows/Docker%20Deploy/badge.svg)

# Quick reference

- **Where to get help**:
  [GitHub Issues Page](https://github.com/lucastercas/docker-moodle/issues)
  [Oficial Moodle Documentaion]()

- **Maintained by**:
  [lucastercas](https://github.com/lucastercas)

# Supported tags and respective `Dockerfile` links

- [ `v3.8.3`, `latest` ](https://github.com/lucastercas/docker-moodle)
- [ `v3.7.6` ](https://github.com/lucastercas/docker-moodle)

# What is Moodle?

<img src="https://raw.githubusercontent.com/lucastercas/docker-moodle/master/moodle-logo.png" width="70%">

[Moodle oficial site](https://moodle.org/?lang=pt_br)

# How to use this image

## Using `docker run`

```bash
$ docker run --rm -it -p 80:80 lucastercas/moodle:latest
```

This will start an instance of Moodle on port `80` of the host. However, as there is no database,
it will crash

## Using `docker-compose.yml`

```yaml
version: "3.7"
services:
  moodle:
    image: lucastercas/moodle:v3.8.3
    ports:
      - "80:80"
    environments:
      DB_USER: db_user
      DB_PASS: db_pass
      DB_HOST: db
      DB_DRIVER: pgsql
      MOODLE_ADMINPASS: admin_pass

  db:
    image: postgres:13-alpine
    environment:
      POSTGRES_USER: db_pass
      POSTGRES_PASSWORD: db_user
      POSTGRES_DB: moodle
```

```bash
$ docker-compose up
```

# Environment Variables

When you start this `moodle` image, you have to provide certain environment variables, so it knows where the database is located, as well as certain Moodle parameters.

## Moodle configuration variables

1. `MOODLE_ADMINUSER`: Optional variable, sets the login to use for the `administrator` account, default is _admin_user_.
2. `MOODLE_ADMINPASS`: Password for the administrator account, there is no default.
3. `MOODLE_ADMINMAIL`: Optional variable, sets the email of the administrator user, default is `mail@email.com`.
4. `MOODLE_NAME`: Optional variable, sets the name of the Moodle instance, default is `moodle`.
5. `MOODLE_WWWROOT`: Optional variable, location of the web site, default is `http://localhost`.
6. `MOODLE_DIR`: Optional variable, location of Moodle, default is `/var/www/html`.
7. `MOODLE_DATADIR`: Optional variables, location of moodledata, default is `/var/www/moodledata`.

## Database configuration variables

1. `DB_HOST`: Host of the database.
2. `DB_USER`: User of database.
3. `DB_PASS`: Password of `DB_USER`.
4. `DB_NAME`: Optional variable, name of database that this instance of Moodle will use, default is _moodle_.
5. `DB_DRIVER`: Type of driver, it can be _pgsql_, _mariadb_, _mysqli_, _sqlsrv_ or _oci_, according to the [Moodle documentation](). Depends on the type of the database on `DB_HOST`

# Extending this image
