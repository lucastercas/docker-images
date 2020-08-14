FROM alpine:latest

WORKDIR /app

RUN apk add --no-cache curl bash openssl && \
  curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
  chmod +x get_helm.sh && \
  ./get_helm.sh

ENTRYPOINT [ "helm" ]
