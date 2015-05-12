========
awsutils
========

awsutils represents a grab bag of utilities that make life easier when working
with amazon web services.

Currently there is only a utility that allows a user to open a SSH connection
to an instance based on its ``Name`` tag.

This package depends on the ``awscli`` package and a proper configuration. To
configure the Amazon CLI, please see the official documentation:
http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

Installation
------------

To install using pip:

.. code-block:: bash
        
        $ pip install awsutils

Or from a source distribution:

.. code-block:: bash

        $ python setup.py install

Scripts
-------

Currently there is only one script, ``awssh.py``. This script is added to the
Python *Scripts* directy and should be on the system path. ``awssh.py`` is
used just as you would use ssh.

.. code-block::

        $ awssh.py user@TagName

Except instead of having to remember IP addresses or weird domain names, a
``Name`` tag is be used instead.
