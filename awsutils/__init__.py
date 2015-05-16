"""
awsutils

"""
import json
from subprocess import check_output

__version__ = '1.0.7'


def lookup(name):
    """
    Returns the network address of an Amazon ec2 instance.

    :param name: value of a ``Name`` tag
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
            addr = instances[0].get('PublicIpAddress') or \
                instances[0].get('PrivateIpAddress')

    if not addr:
        raise Exception('No ec2 instance named "{0}".'.format(name))

    return addr
