#!/bin/bash
#  mvn-install-jar.sh
#    install jar into local maven repository
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


function install_jar() {
    echo "---- install jar into local maven repository:"

    local jarfile="$1"
    local groupId="$2"
    local artifactId="$3"
    local version="$4"

    echo "jarfile: "$jarfile
    echo "groupId: "$groupId
    echo "artifactId: "$artifactId
    echo "version: "$version

    local cmd='mvn install:install-file -Dfile='"$jarfile"' -DgroupId='"$groupId"' -DartifactId='"$artifactId"' -Dversion='"$version"' -Dpackaging=jar'

    $cmd
}


xstream_lib="$libprefix/xstream-1.4.7/lib"

# xstream-1.4.7.jar
install_jar "$xstream_lib/xstream-1.4.7.jar" "com.thoughtworks.xstream" "xstream" "1.4.7"

# xmlpull-1.1.3.1.jar
#   depedency of xstream
install_jar "$xstream_lib/xstream/xmlpull-1.1.3.1.jar" \
    "org.xmlpull" \
    "xmlpull" \
    "1.1.3.1"

# xpp3_min-1.1.4c.jar
#   depedency of xstream
install_jar "$xstream_lib/xstream/xpp3_min-1.1.4c.jar" \
    "org.xmlpull" \
    "xpp3_min" \
    "1.1.4c"
