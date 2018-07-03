# Containers used in jenkins jobs

## Alpine
* im: Container to run the IM service.
* node-npm: Alpine container with node and npm packages
* tosca-parser: Container to launch tosca-parser tests

## Ubuntu

### 16.04
* ansible: Base image for Ansible
* base: Base container with the jenkins user configured
* git: Container with the latest version of Git
* python: Container with python 2.7 and python test libraries
* im: Container to run the IM service.
* tosca: Container with the python libraries needed to test tosca templates
* ec3: Container with the [ec3](http://servproject.i3m.upv.es/ec3/) software for cluster deployment and testing

#### Container inheritance
* base
  * git
    * python
      * im
      * tosca
    * java8
      * maven
        * vnc
    * ec3
