docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t petermcd/ssh_honeypot:0.0.1 --push -f ssh_honeypot.dockerfile . --no-cache
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t petermcd/ssh_honeypot:latest --push -f ssh_honeypot.dockerfile .
