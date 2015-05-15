"""
SSH utilities

"""
from . import lookup
from subprocess import call


def ssh(name, *args):
    """
    Opens a SSH session to the first Amazon ec2 instance which matches a given
    ``Name`` tag.

    :param name: The value of the ``Name`` tag of the instance
    :type name: string

    """
    addr = lookup(name)

    new_args = []
    for arg in args:
        if name in arg:
            arg = arg.replace(name, addr)
        new_args.append(arg)

    if new_args:
        call(['ssh', '-F', '/dev/null'] + new_args)
