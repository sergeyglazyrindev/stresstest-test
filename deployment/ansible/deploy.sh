#! /usr/bin/env bash

/home/ubuntu/gitrepos/reddplus_deployment/.env/bin/ansible-playbook --ask-vault-pass -i 127.0.0.1 -e @secret-vars.vault --extra-vars "env=${2}" --extra-vars "service=${1}" --extra-vars "force_redeploy=yes" build-image-and-deploy.yml
