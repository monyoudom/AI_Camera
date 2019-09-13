# AI_Camera

## How to install

```bash
$ django-admin.py startproject \
  --template=https://github.com/jpadilla/django-project-template/archive/master.zip \
  --name=Procfile \
  --extension=py,md,env \
  project_name
$ mv example.env .env
$ pipenv install --dev
```

## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```
ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY='dont-tell-eve'
DJANGO_DEBUG='yes'
```

These settings(and their default values) are only used on staging and production environments.

```
DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=''
DJANGO_SECURE_SSL_HOST=''
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'
```

## Deployment

It is possible to deploy to Heroku or to your own server.

### Heroku

```bash
$ heroku create
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
$ heroku config:set DJANGO_SECRET_KEY=`./manage.py generate_secret_key`
```
