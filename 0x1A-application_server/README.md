# 0x1A. Application server

This `project` is a practical guide for setting up an application server in conjunction with Nginx to serve a Flask-based web application, such as the Airbnb clone project mentioned in the project Instruction

Steps you follow to work the project
**Update and Install**: The script begins by updating the package manager and installing necessary components like Nginx, pip, Flask, and Gunicorn.
**Repository Cloning**: It includes commands to remove any current Airbnb repositories and clone new versions for the application.
**Nginx Configuration:** The script defines the path to the Nginx configuration file and provides a detailed configuration setup that includes server listening ports, root directory, server name, and proxy pass directives for different applications.
**Service Restart:** After configuring Nginx, the script restarts the service to apply the changes.
Tmux Session Setup: Finally, it sets up Tmux sessions for running the application server with Gunicorn binding to the specified port.

## Requirements
### General
- A README.md file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using python3
- All config files must have comments
- Bash Scripts
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Description
The goal of this project is to install an application server (gunicorn) on our own servers and serve dynamic content with it.

## Table of contents
File | Description
---- | -----------
[2-app_server-nginx_config](./2-app_server-nginx_config) | Nginx config file setup to serve our page from the route /airbnb-onepage/
[3-app_server-nginx_config](./3-app_server-nginx_config) | Nginx config file setup to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001
[4-app_server-nginx_config](./4-app_server-nginx_config) | Nginx config file setup so that the route /api/ points to a Gunicorn instance listening on port 5002
[5-app_server-nginx_config](./5-app_server-nginx_config) | Nginx config file  so that it properly serves the static assets found in web_dynamic/static/ and so that the route / points to your Gunicorn instance

