#!/bin/bash
set -e

CONTAINER="ps07-backdoor"
IMAGE="project-shadow-ps07"

echo "[1/7] Stopping existing PS-07 container if present..."
docker stop "$CONTAINER" 2>/dev/null || true

echo "[2/7] Removing existing PS-07 container if present..."
docker rm "$CONTAINER" 2>/dev/null || true

echo "[3/7] Recreating PS-07 container..."
docker run -d \
  --name "$CONTAINER" \
  --network ps07-internal \
  --memory 512m \
  --cpus 0.5 \
  --restart unless-stopped \
  -p 127.0.0.1:2227:22 \
  "$IMAGE"

echo "[4/7] Connecting PS-07 access network..."
docker network connect ps07-access "$CONTAINER"

echo "[5/7] Waiting for SSH service..."
sleep 5

echo "Removing previous PS-07 SSH host key..."
ssh-keygen -f "/home/student/.ssh/known_hosts" \
  -R "[127.0.0.1]:2227" >/dev/null 2>&1 || true

echo "[6/7] Reapplying PS-07 firewall isolation..."
sudo /usr/local/sbin/ps07-firewall.sh

echo "[7/7] Verification..."

echo
echo "Container status:"
docker ps --filter "name=$CONTAINER" \
  --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo
echo "Networks:"
docker inspect "$CONTAINER" \
  -f '{{range $name,$net := .NetworkSettings.Networks}}{{$name}} -> {{$net.IPAddress}}{{println}}{{end}}'

echo
echo "Restart policy:"
docker inspect "$CONTAINER" \
  -f '{{.HostConfig.RestartPolicy.Name}}'

echo
echo "Flag permissions:"
docker exec "$CONTAINER" ls -l /root/flag.txt

echo
echo "PS-07 reset complete."
echo "Test SSH with:"
echo "ssh -p 2227 analyst@127.0.0.1"
