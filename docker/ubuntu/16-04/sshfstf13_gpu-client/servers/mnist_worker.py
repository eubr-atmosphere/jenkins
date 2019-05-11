# Distributed TENSORFLOW with Asyncronous Training.
# Copde for Worker Server
# PS: python3 /mnist_distrib.py --job_name=worker --task_index=<<<0..1>> --worker_hosts=clusterworker-1.tfcluster.default.svc.cluster.local:8000,clusterworker-2.tfcluster.default.svc.cluster.local:8000 --ps_hosts=clusterworker-0.tfcluster.default.svc.cluster.local:8000

import argparse
import sys
import os
os.environ['GRPC_POLL_STRATEGY'] = "poll"

import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
config.allow_soft_placement = True
config.log_device_placement = True

FLAGS = None

def train(_):
   ps_hosts = FLAGS.ps_hosts.split(",")
   worker_hosts = FLAGS.worker_hosts.split(",")

   cluster = tf.train.ClusterSpec({"ps":ps_hosts, "worker":worker_hosts})
   server = tf.train.Server(cluster, config=config, job_name=FLAGS.job_name, task_index=FLAGS.task_index)

   print(server.target)

   import time
   while True:
      time.sleep(5)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.register("type", "bool", lambda v: v.lower() == "true")
  # Flags for defining the tf.train.ClusterSpec
  parser.add_argument(
      "--ps_hosts",
      type=str,
      default="",
      help="Comma-separated list of hostname:port pairs"
  )
  parser.add_argument(
      "--worker_hosts",
      type=str,
      default="",
      help="Comma-separated list of hostname:port pairs"
  )
  parser.add_argument(
      "--job_name",
      type=str,
      default="",
      help="One of 'ps', 'worker'"
  )
  # Flags for defining the tf.train.Server
  parser.add_argument(
      "--task_index",
      type=int,
      default=0,
      help="Index of task within the job"
  )
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=train, argv=[sys.argv[0]] + unparsed)
