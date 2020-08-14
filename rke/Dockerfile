FROM alpine:latest

WORKDIR /app

ARG VERSION=v1.1.3
RUN apk --no-cache add curl && \
    curl -L "https://github.com/rancher/rke/releases/download/${VERSION}/rke_linux-amd64" --output rke && \
    chmod +x rke && \
    /app/rke --version

ENTRYPOINT [ "/app/rke" ]
