# Simple Web Stack

![Image of a simple web stack](https://imgur.com/eBSa3Wi.jpg)

## Description

This basic web infrastructure hosts a website accessible via `www.foobar.com`. No firewalls or SSL certificates are implemented. Each component (database, application server) shares server resources (CPU, RAM, SSD).

## Specifics About This Infrastructure

+ **Server:** A computer providing services to other computers (clients).

+ **Domain Name:** Provides a human-friendly alias for an IP Address, mapped in DNS.

+ **DNS record for `www` in `www.foobar.com`:** Uses an **A record** for address mapping.

+ **Web Server:** Responds to HTTP/HTTPS requests with requested content.

+ **Application Server:** Installs, operates, and hosts applications for end users or organizations.

+ **Database:** Organizes and maintains accessible information.

+ **Client-Server Communication:** Occurs over the internet through the TCP/IP protocol suite.

## Issues With This Infrastructure

+ **SPOF (Single Point Of Failure):** Multiple points of failure, e.g., MySQL server downtime leads to entire site downtime.

+ **Downtime for Maintenance:** Maintenance requires component or server downtime, affecting the website.

+ **Limited Scalability:** Difficult to scale with increasing traffic, risking resource exhaustion and performance degradation.
