# 0x13. Firewall
## Firewall Setup with UFW (Uncomplicated Firewall)

In this project, we'll be setting up a firewall using UFW on `web-01` to restrict incoming traffic while allowing specific TCP ports.

## What is a Firewall?

A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It acts as a barrier between a trusted internal network and untrusted external networks, such as the internet.

## UFW (Uncomplicated Firewall)

UFW is a user-friendly interface to manage iptables, the built-in firewall for Linux systems. It simplifies the process of configuring a firewall by managing the iptables rules.

### Installation

UFW is typically installed by default on many Linux distributions. However, if it's not installed, you can install it using the following command:

```bash
sudo apt-get install ufw
```

### Configuration

We'll configure UFW on `web-01` to block all incoming traffic except for SSH (port 22), HTTPS (port 443), and HTTP (port 80). Here's how to do it:

1. **Allow SSH (port 22):**
    ```bash
    sudo ufw allow 22/tcp
    ```

2. **Allow HTTPS (port 443):**
    ```bash
    sudo ufw allow 443/tcp
    ```

3. **Allow HTTP (port 80):**
    ```bash
    sudo ufw allow 80/tcp
    ```

4. **Enable UFW:**
    ```bash
    sudo ufw enable
    ```

5. **Verify the rules:**
    ```bash
    sudo ufw status
    ```

After applying these rules, UFW will block all incoming traffic on other ports except for SSH, HTTPS, and HTTP.

### Testing

You can test the firewall rules using tools like telnet to verify that connections are only allowed on the specified ports. For example:

```bash
telnet web-01 22
telnet web-01 443
telnet web-01 80
```

## Additional Notes

- Be cautious when configuring firewall rules, especially when blocking SSH (port 22), as it can lock you out of your server if done incorrectly.
- Always test your firewall rules thoroughly to ensure they are functioning as expected.
- Remember that network-based firewalls outside of your control, such as those in the school network, may impact your ability to test certain ports from specific locations.

By following these steps, you can effectively configure a firewall using UFW on your Linux server.
