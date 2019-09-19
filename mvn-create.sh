#!/bin/bash
#
echo "create java project using mvn:"

groupId="com.pepstack.code"
artifactId="outputlib"


mvn archetype:generate \
    -DgroupId="$groupId" \
    -DartifactId="$artifactId" \
    -DarchetypeArtifactId=maven-archetype-quickstart \
    -DinteractiveMode=false

