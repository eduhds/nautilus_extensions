#!/bin/bash

icons_directory=/usr/share/icons/hicolor/scalable/apps

sudo mkdir -p $icons_directory
sudo cp assets/*.svg $icons_directory

sudo gtk-update-icon-cache /usr/share/icons/hicolor

cp nautilus_*.py ~/.local/share/nautilus-python/extensions

nautilus -q
