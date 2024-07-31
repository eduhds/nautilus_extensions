#!/bin/bash

if command -v apt &> /dev/null; then pkg_cmd='apt install -y'
elif command -v dnf &> /dev/null; then pkg_cmd='dnf install -y'
else echo 'Unsupported, try install manually'; exit 1; fi

sudo $pkg_cmd nautilus-python git

mkdir -p ~/.local/share/nautilus-python
mkdir -p ~/.local/share/nautilus-python/extensions

git clone ... /tmp/nautilus_extensions

cp /tmp/nautilus_extensions/nautilus_*.py ~/.local/share/nautilus-python/extensions

echo 'Install complete'
