#!/bin/sh -e

exec s6-applyuidgid -u $PUID -g $PGID -G "" /daemon.py
