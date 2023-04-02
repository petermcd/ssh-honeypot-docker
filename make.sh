VERSION="V_9_0_P1"

docker build --tag full -f ssh_honeypot.dockerfile .;
IMAGE_ID=$(docker run -d full);

python3 -m venv venv;
./venv/bin/python -m pip install --upgrade pip;
./venv/bin/pip install git+https://github.com/petermcd/docker-build.git;
./venv/bin/python build_dockerfile.py "$IMAGE_ID";

docker stop "$IMAGE_ID";
cd /tmp || exit ;
docker build --tag petermcd/ssh_honeypot:$VERSION .;
docker tag petermcd/ssh_honeypot:$VERSION petermcd/ssh_honeypot:latest;
