#!/usr/bin/env bash

case $1 in
api)
  fastapi run main.py
  ;;
*)
  exec $@
esac