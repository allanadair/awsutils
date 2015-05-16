========
awsutils
========

``awsutils`` represents a grab bag of utilities that make life easier when
working with amazon web services.

+------------------+-------------------------------------------------------+
| script           | Description                                           |
+==================+=======================================================+
| ``awssh.py``     | Establishes SSH connections based on the value of ec2 |
|                  | ``Name`` tags instead of network addresses.           |
+------------------+-------------------------------------------------------+
| ``awscp.py``     | Facilitates SCP operations based on the values of ec2 |
|                  | ``Name`` tags instead of network addresses.           |
+------------------+-------------------------------------------------------+
| ``awslookup.py`` | Returns IP addresses of instances by ``Name``.        |
+------------------+-------------------------------------------------------+

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

These scripts are added to the Python *Scripts* directy and should be on the
system path. ``awssh.py`` and ``awscp.py`` are used just as a user would
normally use ssh and scp. If a named instance contains spaces, enclose the
instance-name in quotations.

Examples:

.. code-block:: bash

        $ awssh.py user@myserver1

.. code-block:: bash

        $ awssh.py user@"my server 1"

.. code-block:: bash
        
        $ awscp.py /path/to/local/file user@myserver1:/path/to/remote/file

.. code-block:: bash

        $ awslookup.py myserver1
