# Webstack monitoring

**Background Context**
“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

Application monitoring: getting data about your running software and making sure it is behaving as expected
Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)
# Requirements
## General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
## Tasks :page_with_curl:

* **0. Monitor your Nginx traffic**
  * [0-monitor_your_nginx_traffic](./0-monitor_your_nginx_traffic): Text file containing
  my Sumo Logic access key.
    * First line: `Access ID`
    * Second line: `Access Key`

* **1. Monitor your server**
  * For this task, I configured Sumo Logic to monitor my server's memory, CPU, network
  and disk.

