#!/bin/bash

set -euo pipefail

testing_regex() {
version=12.0.41

[[ $version =~ ([0-9]*)\.([0-9]*)\.([0-9]*) ]]
echo ${BASH_REMATCH}
echo "version | $version"
echo "Whole match | ${BASH_REMATCH[0]}"
echo "Major       | ${BASH_REMATCH[1]}"
echo "Release     | ${BASH_REMATCH[2]}"
echo "Patch       | ${BASH_REMATCH[3]}"
echo "What is the in parenthases is what you get in the array"
}

# Release gets bumped when you branch main to start on a new release Epic
# If it is an Epic Epic!! And you know you are doing major changes then maybe you bump the major too

# TODO: Add support for release versions bumping https://kodekeith.atlassian.net/browse/GEN-40

version=$(toml get --toml-path pyproject.toml project.version)
[[ $(toml get --toml-path pyproject.toml project.version) =~ \
([0-9]*)\.([0-9]*)\.([0-9]*) ]]
i=${BASH_REMATCH[3]}
new_version="${BASH_REMATCH[1]}.${BASH_REMATCH[2]}.$((++i))"
toml set --toml-path pyproject.toml project.version $new_version
git add pyproject.toml
git commit -m "$0"
git pull # might need to pull if another parralle build 
# has done the same thing for a different platform!
# Do the pull after the bump so we should end up with all platforms having the same version?
git push

# $((++i))
#  0.2.0
# toml set --toml-path pyproject.toml tool.poetry.version 0.2.0
