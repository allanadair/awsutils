#!/usr/bin/env python
"""
Utiliy for looking up the network address of an Amazon ec2 instance

"""
from argparse import ArgumentParser
from awsutils import lookup

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('name',
                        help='Value of the Name tag of an ec2 instance',)
    args = parser.parse_args()

    print(lookup(name=args.name))
