"""
SSH utilities

"""
import json
from subprocess import check_call, check_output


def ssh(name, *args):
    """
    Opens a SSH session.

    :param name: The value of the ``Name`` tag of the instance

    """
    desc = check_output(['aws', 'ec2', 'describe-instances', '--filter',
                         'Name=tag:Name,Values={0}'.format(name),
                         '--output=json'])
    reservations = json.loads(desc).get('Reservations')
    if reservations:
        instances = reservations[0].get('Instances')
        if instances:
            addr = instances[0]['PublicIpAddress']

    assert(addr)

    new_args = []
    for arg in args:
        if name in arg:
            arg = arg.replace(name, addr)
        new_args.append(arg)

    check_call(['ssh'] + new_args)
