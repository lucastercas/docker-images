FROM alpine:latest AS base

ARG helm_version
ARG helm_url="https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-${helm_version}"

LABEL lucastercas.helm.author="lucastercas <lucasmtercas@gmail.com>" \
  lucastercas.helm.version=${helm_vesion}

WORKDIR /app
RUN apk add --no-cache curl bash openssl
RUN  curl -fsSL -o get_helm.sh "${helm_url}" \
  && chmod +x get_helm.sh \
  && ./get_helm.sh

ENTRYPOINT [ "helm" ]
CMD [ "version" ]