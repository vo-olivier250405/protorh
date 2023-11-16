#!/bin/bash

# Vérification des paramètres
developer_mode=0
while [[ "$#" -gt 0 ]]; do
    case "$1" in
        --dev)
            developer_mode=1
            ;;
        *)
            echo -e '\e[31mUnknown option\e[0m'
            exit 1
            ;;
    esac
    shift
done

# Installation des linters destinés aux développeurs
if [ "$developer_mode" -eq 1 ]; then
    echo -e '\e[34mInstallation des linters destinés aux développeurs\e[0m'
    sudo apt-get install -y pycodestyle pylint
fi

# Installation de python
echo -e '\e[34mInstallation de python\e[0m'
sudo apt-get install -y python3 python3-pip