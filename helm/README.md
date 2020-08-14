# Helm Docker Image

The default workdir is `/app`, so any command will execute there, unless
you specify another working directory.

## Example Usage

Updating local repositories:

```bash
docker run --rm -ti \
  lucastercas/helm repo add jetstack https://charts.jetstack.io
```

Installing a package to the cluster:

```bash
docker run --rm -ti \
  -v $(pwd)/cluster-config.yml:/app/cluster-config.yml \
  lucastercas/helm  --kubeconfig=./cluster_config.yml install cert-manager
```
