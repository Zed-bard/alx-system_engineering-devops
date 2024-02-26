# Secured and Monitored Web Infrastructure

![https://imgur.com/atbVKWR]( 
![https://imgur.com/atbVKWR])

## Description

This web infrastructure consists of three servers designed to ensure security, monitoring, and encrypted traffic transmission.

## Key Features of the Infrastructure

### Firewalls
The firewalls play a crucial role in safeguarding the web servers from unwanted and unauthorized access. They serve as intermediaries between the internal and external networks, actively blocking incoming traffic that doesn't meet specified criteria. This proactive measure enhances network security by preventing potential threats from reaching the web servers.

### SSL Certificate
The SSL certificate serves the purpose of encrypting traffic between the web servers and the external network. This encryption is vital in thwarting man-in-the-middle attacks (MITM) and preventing network sniffers from intercepting sensitive information. The SSL certificates contribute to ensuring privacy, data integrity, and proper server identification.

### Monitoring Clients
The monitoring clients are dedicated to overseeing the servers and external network. They analyze server performance, assess overall health, and promptly alert administrators if any deviations from expected performance are detected. The monitoring tools provide valuable metrics on server operations, conducting automatic tests on server accessibility and response time. Additionally, they raise alerts for issues such as corrupt or missing files, security vulnerabilities, and other potential concerns.

## Identified Issues with the Infrastructure

### SSL Termination at Load Balancer
Terminating SSL at the load balancer level may leave the communication between the load balancer and the web servers unencrypted. Ensuring end-to-end encryption is crucial for maintaining the confidentiality and security of transmitted data.

### Single MySQL Server
The presence of a single MySQL server poses scalability challenges and introduces a single point of failure in the web infrastructure. Implementing a more scalable database solution can enhance reliability and support future growth.

### Uniform Server Components
Utilizing servers with identical components may lead to resource contention issues, such as competition for CPU, memory, and I/O. This contention can result in poor performance and difficulty in pinpointing the source of problems. A more scalable and efficient setup involves diversified components and resource allocation, ensuring optimal server performance and easier scalability.
