# Quick reference

- **Maintained by**: []()
- **Where to get help**: []()

# Supported tags and respective `Dockerfile` links

- [`3`, `latest`]()

# What is `helm`?

[Helm](https://helm.sh/) is a package manager for kubernetes,
which provides an easy way to find and share software
to be installed on a k8s cluster.

# How to use this image

The default workdir is `/app`, so any command will execute there, unless
you specify another working directory.

Updating local repositories:

```console
$ docker run --rm -ti \
  lucastercas/helm repo add jetstack https://charts.jetstack.io
```

Installing a package to the cluster:

```console
$ docker run --rm -ti \
  -v $(pwd)/cluster-config.yml:/app/cluster-config.yml \
  lucastercas/helm  --kubeconfig=./cluster_config.yml install cert-manager
```
