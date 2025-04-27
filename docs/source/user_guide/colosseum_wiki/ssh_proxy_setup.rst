SSH Proxy Setup
==============

Using the SSH Config File
------------------------

Using the ssh config file, it is possible to ssh through an intermediate machine(s) in order to arrive at a destination only through that path. Since sftp and scp both operate over ssh, this configuration applies to those commands also.

The ssh config file allows the user to specify default settings that the client is to use for connections to specific hosts. By specifying default user names, key files, or proxy commands, it is possible to greatly reduce the number of arguments that need to be entered on the command line. This in turn simplifies access to Colosseum resources.

**Note: this procedure will apply only to your current user account on your machine.**

Procedure
--------

1. On your local machine, create an ssh config file if one does not already exist, or open the existing config file within the .ssh/ directory, which is typically found in the user home directory. The example below shows a terminal command to open/create the file in the vi editor, but any terminal or graphical text editor can be used.

   .. code-block:: bash
   
       vim ~/.ssh/config

2. Within the SSH config file, add the following lines and save the changes.

   .. code-block:: bash
   
    # SSH Gateway
    Host colosseum-gw
       Hostname gw.colosseum.net
       User username
       IdentityFile ~/.ssh/id_rsa
       
    # File Proxy Server
    Host file-proxy
       Hostname file-proxy
       User username
       ProxyCommand ssh -W %h:%p colosseum-gw 
       
    # SRNs (User Container)
    Host teamname-srn???
       User root
       StrictHostKeyChecking no
       UserKnownHostsFile=/dev/null
       ProxyCommand ssh -W %h:%p colosseum-gw

   .. note::

    If you are not sure of your team name, just log into the Colosseum portal and open the "Reservations" page:

    .. figure:: /_static/images/user_guide/wiki/ssh_proxy_setup/team_name.png


   .. note::

     * The entry for the SSH Gateway may have already been created during the procedure to :doc:`Upload SSH Public Keys <upload_ssh_keys>`

     * The three question marks in the last entry are single-character wildcards. These will automatically match all of the SRN container hostnames. "teamname" is to be replaced by the corresponding team name.

     * The SRN hostnames and the file-proxy hostname listed above are only routable within the Colosseum network and are effectively "nicknames" used by the ssh command.

     * The default path for the private key for Linux systems is: ``/home/username/.ssh/id_rsa``

3. Now it should be possible to ssh directly to one of the end destination hosts specified in the config file. For example, it should be possible to ssh to the File Proxy server using the following: ``ssh file-proxy``. You will be prompted for a password for each intermediate host as well as the destination host.

Details
------

The ssh config file specifies parameters to use for specific hosts. This is a convenient way to instruct ssh to use a specific user name for specific hosts, or other similar parameters.

In particular, the "ProxyCommand" parameter indicates a command to be run in order to connect to the specified host. In the example here, this instructs ssh that, for these hosts, it should first connect to the ssh gateway by ssh.

References
---------

This article was based primarily on the following reference:

`https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Proxies_and_Jump_Hosts <https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Proxies_and_Jump_Hosts>`_ (Look for: Recursively Chaining Gateways Using stdio Forwarding)

For more information on the ssh config file, see the man page:

.. code-block:: bash

    man ssh_config
