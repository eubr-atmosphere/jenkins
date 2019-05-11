#!/bin/bash
set -e

if [ "$SKIPMOUNT" != "true" ]; then
  mkdir -p ~/.ssh
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

  echo 'Host *' > ~/.ssh/config
  echo "   StrictHostKeyChecking no" >> ~/.ssh/config
  chmod 400 ~/.ssh/config
#  UID=$(id -u)
#  chown -R $UID.$UID ~/.ssh
  chown -R 1000.1000 /home/jovyan/.ssh
  touch /tmp/pepe
  ls -lR ~/.ssh

fi

# This solution does not work if the argument is a set of bash commands
# $@

# Using this instead
echo "$@" >.runcmd
source .runcmd
