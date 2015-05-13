"""
SSH utilities

"""
import json
from subprocess import call, check_output


def ssh(name, *args):
    """
    Opens a SSH session to the first Amazon ec2 instance which matches a given
    ``Name`` tag.

    :param name: The value of the ``Name`` tag of the instance
    :type name: string

    """
    addr = None
    desc = check_output(['aws', 'ec2', 'describe-instances', '--filter',
                         'Name=tag:Name,Values={0}'.format(name),
                         '--output=json'])
    reservations = json.loads(desc).get('Reservations')
    if reservations:
        instances = reservations[0].get('Instances')
        if instances:

            # prefer public IP over private IP
            addr = instances[0]['PublicIpAddress'] or \
                instances[0]['PrivateIpAddress']

    if not addr:
        raise Exception('No ec2 instance named "{0}".'.format(name))

    new_args = []
    for arg in args:
        if name in arg:
            arg = arg.replace(name, addr)
        new_args.append(arg)

    if new_args:
        call(['ssh', '-F', '/dev/null'] + new_args)
