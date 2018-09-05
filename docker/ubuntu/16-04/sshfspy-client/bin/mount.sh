#!/bin/bash
set -e
mkdir ~/.ssh
echo "SSH Directory created to"
echo $SSHPRIVKEY | sed -e 's/\\n/\n/g' > ~/.ssh/id_rsa
chmod 400 ~/.ssh/id_rsa
echo $SSHPUBKEY > ~/.ssh/id_rsa.pub

echo "PRIVKEY:"
ls -l ~/.ssh/id_rsa
cat ~/.ssh/id_rsa
echo "PUBKEY:"
ls -l ~/.ssh/id_rsa.pub
cat ~/.ssh/id_rsa.pub

echo "Remove host verification"

echo "Host $SERVER" > ~/.ssh/config
echo "   StrictHostKeyChecking no" >> ~/.ssh/config
chmod 400 ~/.ssh/config

echo "Connecting to root@$SERVER"
sshfs -o allow_other root@$SERVER:/ $MOUNTPOINT
$@
