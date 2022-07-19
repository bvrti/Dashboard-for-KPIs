#!/bin/bash

SERVER=blo-ve2.delphidrive.com
IMAGE=jj00sp_dashboard
VERSION=$(date +%Y%m%d%H%M)
BUILD_DIR="/var/tmp/dockerbuild/$IMAGE/$VERSION"

ssh ${SERVER} mkdir -p ${BUILD_DIR}
rsync -zrvh ssh . ${SERVER}:${BUILD_DIR}
# ssh ${SERVER} docker build -t ${IMAGE} -t ${IMAGE}:${VERSION}