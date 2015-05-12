#!/usr/bin/env python
"""
Utiliy for secure copying by using an Amazon ec2 instance Name tags

"""
from awsutils.scp import scp
from sys import argv

if __name__ == '__main__':

    names = []

    for arg in argv[1:]:
        if '@' in arg:
            name = arg.split('@')[-1]
            name = name.split(':')[0]
            names.append(name)

    if names:
        scp(names, *argv[1:])
    else:
        raise Exception('Must provide user@name argument(s).')
