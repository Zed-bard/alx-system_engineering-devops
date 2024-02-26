# Scaled Up Web Infrastructure

![Scaled Up Web Infrastructure](https://i.imgur.com/WxUQwuz.jpg)

## Description

This enhanced web infrastructure represents a scaled-up version of the architecture detailed [here](https://i.imgur.com/WxUQwuz.jpg). In this iteration, all Single Points of Failure (SPOFs) have been eliminated. The major components, including the web server, application server, and database servers, have been relocated to separate GNU/Linux servers. SSL protection is not terminated at the load balancer, and each server's network is fortified with a firewall while being actively monitored.

## Specifics About This Infrastructure

+ **Firewall Implementation:** A firewall has been introduced between each server, enhancing security by protecting individual servers from unwanted and unauthorized access.

## Issues With This Infrastructure

+ **High Maintenance Costs:** The transition of each major component to its dedicated server results in increased maintenance costs. The procurement of additional servers and the accompanying rise in electricity consumption amplify operational expenses. Allocating company funds becomes necessary for server acquisition and covering the heightened electricity consumption to sustain both existing and new servers.
