#!/usr/bin/env python
"""
Utiliy for opening a SSH session by using an Amazon ec2 instance Name tag

"""
from awsutils.ssh import ssh
from sys import argv

if __name__ == '__main__':

    name_value = None

    for arg in argv[1:]:
        if '@' in arg:
            name_value = arg.split('@')[-1]

    if name_value:
        ssh(name_value, *argv[1:])
    else:
        raise Exception("Must provide a user@TagName argument.")
