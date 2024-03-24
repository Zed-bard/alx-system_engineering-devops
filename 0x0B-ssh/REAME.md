# 0x0B. SSH

SSH (Secure Shell) is a secure network protocol used for remote access and management of network devices, servers, and computers over an unsecured network, such as the Internet.

## Resources

### A Simple SSH Illustration
![SSH Illustration](https://assets.website-files.com/5ff66329429d880392f6cba2/61c1b963247368113bbeef17_Secure%20Shell%20work.png)

## Learning Objectives

### General
- Understand what a server is
- Know where servers usually reside
- Learn about SSH and its significance
- Discover how to create an SSH RSA key pair
- Learn how to connect to a remote host using an SSH RSA key pair
- Understand the advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## General
- **What is a server:** 
  - A server is a computer or a system that provides resources, data, services, or programs to other computers, known as clients, over a network.
- **Where servers usually live:** 
  - Servers can physically reside in data centers, server rooms, or in the cloud.
- **What is SSH (Secure Shell):** 
  - SSH is a secure network protocol that allows for secure remote access and management of network devices, servers, and computers over an unsecured network, such as the Internet.
- **How to create an SSH RSA key pair:**
  - To create an SSH RSA key pair, you can use the `ssh-keygen` command on your local machine. This command generates a public and private key pair. The public key can be shared with servers or other users, while the private key should be kept secure on your local machine.
- **How to connect to a remote host using an SSH RSA key pair:**
  - To connect to a remote host using an SSH RSA key pair, you can use the `ssh` command followed by the username and hostname of the remote host. For example:
    ```
    ssh username@hostname
    ```
  - If you have an SSH RSA key pair configured, SSH will attempt to authenticate using your private key.
- **The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`:**
  - Using `#!/usr/bin/env bash` as the shebang line allows the script to find the Bash interpreter regardless of its location in the file system. This provides more flexibility and portability to the script, especially when it's being executed on different systems where the Bash interpreter might be located in different directories.


