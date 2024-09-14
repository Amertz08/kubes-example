#!/usr/bin/env bash

case $1 in
api)
  fastapi run main.py
  ;;
cron)
  python cron_main.py
  ;;
*)
  exec $@
esac