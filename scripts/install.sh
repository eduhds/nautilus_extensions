#!/bin/bash

if command -v apt &> /dev/null; then pkg_cmd='apt install -y python3-nautilus'
elif command -v dnf &> /dev/null; then pkg_cmd='dnf install -y nautilus-python'
else echo 'Unsupported, try install manually'; exit 1; fi

sudo $pkg_cmd git

mkdir -p ~/.local/share/nautilus-python
mkdir -p ~/.local/share/nautilus-python/extensions

git clone https://github.com/eduhds/nautilus_extensions.git \
    /tmp/nautilus_extensions

cp /tmp/nautilus_extensions/nautilus_*.py \
    ~/.local/share/nautilus-python/extensions

if [ "$?" -ne 0 ]; then
    echo 'Failed install'
else
    echo 'Install complete'
fi
