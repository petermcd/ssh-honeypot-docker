"""Example file."""
from sys import argv, exit
from pathlib import Path

from docker_build.docker import Docker
from docker_build.models import ExposedPortDetails

if len(argv) == 1:
    exit('The image ID was not passed to this script')

container_id = argv[1]

path = Path('/tmp/')
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
    ]
)
