#!/bin/bash
set -e
echo "MOUNTING"
mount -v $SERVER:/ $MOUNTPOINT
echo "RUNNING: $@"
$@
