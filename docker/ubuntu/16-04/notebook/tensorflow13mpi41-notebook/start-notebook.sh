#!/bin/bash
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

set -e

if [ "$SKIPMOUNT" != "true" ]; then
  mkdir -p /root/.ssh
  echo "SSH Directory created to"
  echo $SSHPRIVKEY | sed -e 's/\\n/\n/g' > /root/.ssh/id_rsa
  chmod 400 /root/.ssh/id_rsa
  echo $SSHPUBKEY > /root/.ssh/id_rsa.pub
  
  echo "PRIVKEY:"
  ls -l /root/.ssh/id_rsa
  cat /root/.ssh/id_rsa
  echo "PUBKEY:"
  ls -l /root/.ssh/id_rsa.pub
  cat /root/.ssh/id_rsa.pub

  echo "Remove host verification"

  echo "Host $SERVER" > /root/.ssh/config
  echo "   StrictHostKeyChecking no" >> /root/.ssh/config
  chmod 400 /root/.ssh/config

  PORT=${SSH_PORT:-22}

  echo "Connecting to root@$SERVER on port $PORT"

  HOMEUSER=$HOME
  sudo sshfs -o allow_other,nonempty -p $PORT -o IdentityFile=/root/.ssh/id_rsa -o StrictHostKeyChecking=no root@$SERVER:/ $MOUNTPOINT
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
