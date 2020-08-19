FROM alpine:latest

ARG helm_version
ARG helm_url="https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-${helm_version}"

WORKDIR /opt/app
RUN apk add --no-cache curl bash openssl
RUN  curl -fsSL -o get_helm.sh "${helm_url}" \
  && chmod +x get_helm.sh \
  && ./get_helm.sh

LABEL \
  org.lucastercas.helm.image.authors="Lucas de Macedo Terças <lucasmtercas@gmail.com>" \
  org.lucastercas.helm.image.maintainers="Lucas de Macedo Terças <lucasmtercas@gmail.com>" \
  org.lucastercas.helm.image.version=${helm_vesion} \
  org.lucastercas.helm.image.title="lucastercas/helm" \
  org.lucastercas.helm.image.description="Helm application" \
  org.lucastercas.helm.image.licenses="" \
  org.lucastercas.helm.image.source="" \
  org.lucastercas.helm.image.url="" \
  org.lucastercas.helm.image.documentation=""

ENTRYPOINT [ "helm" ]
CMD [ "version" ]