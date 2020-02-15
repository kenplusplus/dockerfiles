#!/bin/bash

sudo docker build --build-arg https_proxy=http://192.168.0.6:8118 -t 192.168.0.3:83/clearlinux/tensorflow-intel .
