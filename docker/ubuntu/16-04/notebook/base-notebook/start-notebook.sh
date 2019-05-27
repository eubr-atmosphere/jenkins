#!/bin/bash
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

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

  echo "Host $SERVER" > ~/.ssh/config
  echo "   StrictHostKeyChecking no" >> ~/.ssh/config
  chmod 400 ~/.ssh/config

  PORT=${SSH_PORT:-22}

  echo "Connecting to root@$SERVER on port $PORT"

  HOMEUSER=$HOME
  sudo sshfs -o allow_other,nonempty -p $PORT -o IdentityFile=$HOMEUSER/.ssh/id_rsa -o StrictHostKeyChecking=no root@$SERVER:/ $MOUNTPOINT
fi


if [ "$STARTCLUSTER" == "true" ]; then
  MYIP=$(hostname -i)
  ipcontroller --ip=$MYIP --ipython-dir=$MOUNTPOINT/.ipython &
fi

if [[ ! -z "${JUPYTERHUB_API_TOKEN}" ]]; then
  # launched by JupyterHub, use single-user entrypoint
  exec /usr/local/bin/start-singleuser.sh $*
else
  if [[ ! -z "${JUPYTER_ENABLE_LAB}" ]]; then
    . /usr/local/bin/start.sh jupyter lab $*
  else
    . /usr/local/bin/start.sh jupyter notebook $*
  fi
fi
