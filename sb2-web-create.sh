#!/bin/bash
#  sb2-web-create.sh
#    create springboot2 web artifact
#
###########################################################
# will cause error on macosx
_file=$(readlink -f $0)

_cdir=$(dirname $_file)
_name=$(basename $_file)

###########################################################
# Treat unset variables as an error
set -o nounset

# Treat any error as exit
set -o errexit


# where you put local jar
libprefix="$_cdir/lib"
if [ "${libprefix:0:10}" = "/cygdrive/" ]; then
    libprefix="${libprefix:10:1}:${libprefix:11}"
fi

###########################################################
# save with: https://start.spring.io/
#
SpringBoot="2.1.8"

# Project Metadata:
Group="com.pepstack"
Artifact="sb2-demo"

# Options
Name="sb2-demo"
Description="Demo project for Spring Boot2"
PackageName="com.pepstack.sb2demo"
Packaging="Jar"
Java="8"

