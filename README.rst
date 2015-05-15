========
awsutils
========

awsutils represents a grab bag of utilities that make life easier when working
with amazon web services.

+--------------+-------------------------------------------------------+
| script       | Description                                           |
+==============+=======================================================+
| awssh.py     | Establishes SSH connections based on the value of ec2 |
|              | ``Name`` tags instead of network addresses.           |
+--------------+-------------------------------------------------------+
| awscp.py     | Facilitates SCP operations based on the values of ec2 |
|              | ``Name`` tags instead of network addresses.           |
+--------------+-------------------------------------------------------+
| awslookup.py | Returns IP addresses of instances.                    |
+--------------+-------------------------------------------------------+

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

Currently there are only two scripts, ``awssh.py`` and ``awscp.py``. These
scripts are added to the Python *Scripts* directy and should be on the system
path. ``awssh.py`` and ``awscp.py`` are used just as you would use ssh and scp.

Examples:

.. code-block::

        $ awssh.py user@TagName

.. code-block::
        
        $ awscp.py /path/to/local/file user@TagName:/path/to/remote/file

Except instead of having to remember IP addresses or weird domain names, the
value of a ``Name`` tag is used instead.
