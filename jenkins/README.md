# Quick reference

- **Maintained by**: []()
- **Where to get help**:
  [Jenkins Oficial Image](https://github.com/jenkinsci/docker)

# Supported tags and respective `Dockerfile` links

- [`latest`]()

# What is `Jenkins`?

# How to use this image

Custom Jenkins docker image, with plugins, packages and python modules I use.

```console
$ docker run --rm \
  -p 8080:8080 \
  -v jenkins_home:/var/jenkins_home \
  lucastercas/jenkins
```

## Modifications:

1. Jenkins Plugins
   1. gitlab-plugins
   2. sonar
2. Packages
   1. make
   2. maven
   3. sshpass
   4. python3-pip
   5. python3-setuptools
3. Python Modules
   1. docker
   2. ansible
