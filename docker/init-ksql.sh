#!/bin/sh

set -e

KSQL_SERVER="$1"

until ksql "$KSQL_SERVER"; do
  >&2 echo "Wating for KSQL Server"
  sleep 1
done

>&2 echo "KSQL Server Ready"
ksql -f /tmp/test.sql $KSQL_SERVER