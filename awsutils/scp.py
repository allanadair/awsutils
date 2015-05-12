"""
SCP utilities

"""
import json
from subprocess import call, check_output


def scp(names, *args):
    """
    Secure copies the Amazon ec2 instance(s) which match given ``Name`` tags.

    :param names: Ordered ``Name`` tags of instances involved in secure copy
    :type names: tuple

    """
    addrs = {}
    for i, name in enumerate(names):
        desc = check_output(['aws', 'ec2', 'describe-instances', '--filter',
                             'Name=tag:Name,Values={0}'.format(name),
                             '--output=json'])
        reservations = json.loads(desc).get('Reservations')
        if reservations:
            instances = reservations[0].get('Instances')
            if instances:
                addrs[names[i]] = instances[0]['PublicIpAddress']

    for name in names:
        if not addrs.get(name):
            raise Exception('No ec2 instance named "{0}".'.format(names[0]))

    new_args = []
    for arg in args:
        for name in names:
            if name in arg:
                arg = arg.replace(name, addrs[name])
            new_args.append(arg)

    if new_args:
        call(['scp'] + new_args)
