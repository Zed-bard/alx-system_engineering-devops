# Web Stack Debugging #3

In this project, we are tasked with debugging a Wordpress website running on a LAMP stack. When traditional debugging methods such as logs are not providing enough information, we need to delve deeper into the stack to identify and resolve issues.

## Requirements
- All files will be interpreted on Ubuntu 14.04 LTS.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Puppet manifests must run without error.
- Puppet manifest files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

## General Information
Wordpress is a widely used tool for various purposes such as blogs, portfolios, e-commerce, and company websites. It powers a significant portion of the web, approximately 26%. It is typically run on a LAMP stack, consisting of Linux, Apache, MySQL, and PHP.

## More Info
To install `puppet-lint`, use the following commands:
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

Let's dive into debugging this web stack and ensure smooth operation of the Wordpress website.
