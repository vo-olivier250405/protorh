#!/bin/bash

# Lancer le fichier suivi du nom du dossier ou du fichier à vérifier
pylama $1; pylint $1; pycodestyle $1