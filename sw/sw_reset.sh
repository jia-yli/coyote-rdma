#!/bin/bash
set -o xtrace
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
BUILD_DIR="${SCRIPT_DIR}/build"
rm -rf ${BUILD_DIR}
mkdir ${BUILD_DIR} && cd ${BUILD_DIR}
# /usr/bin/cmake ${SCRIPT_DIR} -DTARGET_DIR=${SCRIPT_DIR}/examples/dedup_sys_test1
# /usr/bin/cmake ${SCRIPT_DIR} -DTARGET_DIR=${SCRIPT_DIR}/examples/dedup_sys_test2
# /usr/bin/cmake ${SCRIPT_DIR} -DTARGET_DIR=${SCRIPT_DIR}/examples/dedup_sys_test3
/usr/bin/cmake ${SCRIPT_DIR} -DTARGET_DIR=${SCRIPT_DIR}/examples/dedup_sys_test$1
make