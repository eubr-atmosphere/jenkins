#!/bin/bash
set -e

if [ "$SKIPMOUNT" != "true" ]; then
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

  echo 'Host *' > ~/.ssh/config
  echo "   StrictHostKeyChecking no" >> ~/.ssh/config
  chmod 400 ~/.ssh/config

  # Same directory for user atmosphere
  cp -r /root/.ssh /home/atmosphere
  chown -R atmosphere.atmosphere /home/atmosphere/.ssh  

  PORT=${SSH_PORT:-22}

  echo "Connecting to root@$SERVER on port $PORT"
  sshfs -o allow_other,nonempty -p $PORT root@$SERVER:/ $MOUNTPOINT
fi

# This solution does not work if the argument is a set of bash commands
# $@

# Using this instead
echo "$@" >.runcmd
/usr/local/bin/entrypoint.sh .runcmd
#source .runcmd
