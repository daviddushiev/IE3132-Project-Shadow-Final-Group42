FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openssh-server \
        sudo \
        findutils \
        procps \
        iproute2 && \
    rm -rf /var/lib/apt/lists/*

# Create low-privilege challenge account
RUN useradd -m -s /bin/bash analyst && \
    echo 'analyst:student123' | chpasswd

# Configure SSH
RUN mkdir -p /run/sshd && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# Deliberate PS-07 sudo misconfiguration
RUN echo 'analyst ALL=(root) NOPASSWD: /usr/bin/find' \
    > /etc/sudoers.d/ps07-challenge && \
    chmod 440 /etc/sudoers.d/ps07-challenge

# Final challenge flag
RUN echo 'SHADOW{sudo_misconfiguration_grants_root}' > /root/flag.txt && \
    chmod 600 /root/flag.txt

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
