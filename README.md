# ssh-honeypot-docker

A couple of years ago I created a project to have an SSH Honey Pot. Originally this was made from a few
repos that would require building. This repository packages this into a docker container.

## Disclaimer

THis has had no testing so far, use this at your own risk.

## Build Yourself

If you would like to build the docker image yourself simply run:

```shell
docker build --tag petermcd/ssh_honeypot -f ssh_honeypot.dockerfile .
```

### Using the Honeypot

You can start the honeypot by running the following command:

```shell
docker run -p 22222:22 -P petermcd/ssh_honeypot
```

This will begin the honeypot, you will also be required to enable port forwarding on your router from port 22 -> 22222
on the host hosting the honeypot.

### TODO

At present the honeypot stores the attempts in a file within the container, this will be tasken out and placed somewhere
it can be easily retrieved

The image is quite large due to it being based on Ubuntu, I intend to make a brand new custom container in the future.
