FROM alpine:3.20

RUN apk add --no-cache dnsmasq

COPY dnsmasq.conf /etc/dnsmasq.conf

EXPOSE 53/udp
EXPOSE 53/tcp

CMD ["dnsmasq", "--no-daemon", "--conf-file=/etc/dnsmasq.conf"]
