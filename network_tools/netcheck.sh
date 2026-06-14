#!/bin/bash
# netcheck.sh - quick network overview

echo "================================"
echo "       NETWORK RECONNAISSANCE"
echo "================================"

echo ""
echo "==== YOUR IP ===="
ip a | grep "inet " | grep -v "127.0.0.1"

echo ""
echo "==== GATEWAY ===="
ip route | grep default

echo "" 
echo "==== DEVICES ON NETWORK ===="
SUBNET=$(ip a | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n1)
nmap -sn "$SUBNET" -oG /tmp/live_hosts.txt > /dev/null
grep "Up" /tmp/live_hosts.txt | awk '{print $2}'

echo ""
echo "==== DETAILED SCAN OF LIVE HOSTS ===="
grep "Up" /tmp/live_hosts.txt | awk '{print $2}' > /tmp/live_ips.txt
nmap -A -iL /tmp/live_ips.txt

echo ""
echo "==== OPEN PORTS ON THIS MACHINE ===="
ss -tulpn

echo "================================="
echo "             DONE"
echo "================================="

