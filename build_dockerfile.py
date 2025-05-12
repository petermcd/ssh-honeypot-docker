"""Build a dockerfile for a given container ID."""
from sys import argv, exit
from pathlib import Path

from docker_build.docker import Docker
from docker_build.models import ExposedPortDetails

if len(argv) != 3:
    exit('The number of arguments is incorrect, we need the container ID and the path for the temporary files.')

container_id = argv[1]
build_path = argv[2]

path = Path(build_path)
docker = Docker(base_path=path, container_id=container_id, base_image='scratch')
docker.run(
    config_files=[
        '/etc/pam.d/sshd',
        '/etc/passwd',
        '/usr/etc/sshd_config',
    ],
    binaries=[
        '/bin/bash',
        '/usr/bin/mkdir',
        '/usr/bin/ssh-keygen',
        '/bin/sh',
        '/usr/sbin/sshd',
        '/usr/bin/ssh',
        '/usr/bin/sqlite3',
        '/lib/security/ssh_honeypot.so',
        '/usr/libexec/sshd-session',
        '/usr/libexec/sshd-auth',
        '/usr/bin/tail',
    ],
    commands=[
        'ssh-keygen -A',
        'mkdir /var/',
        'mkdir /var/log/',
        'mkdir /var/empty',
        'mkdir /var/empty/sshd',
        'mkdir /var/empty/sshd/etc',
        'mkdir /root/',
        'mkdir /root/.ssh/',
    ],
    exposed_ports=[
        ExposedPortDetails(port=22, protocol='tcp'),
        ExposedPortDetails(port=22, protocol='udp'),
    ],
    entry_point='/usr/sbin/sshd && tail -f /dev/null',
)
