"""
SCP utilities

"""
from . import lookup
from subprocess import call


def scp(names, *args):
    """
    Secure copies the Amazon ec2 instance(s) which match given ``Name`` tags.

    :param names: Ordered ``Name`` tags of instances involved in secure copy
    :type names: tuple

    """
    addrs = {}
    for i, name in enumerate(names):
        addrs[names[i]] = lookup(name)

    new_args = []
    for arg in args:
        for name in names:
            if name in arg:
                arg = arg.replace(name, addrs[name])
            new_args.append(arg)

    if new_args:
        call(['scp', '-F', '/dev/null'] + new_args)
