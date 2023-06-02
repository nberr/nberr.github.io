#!/bin/bash

read -p 'Hostname: ' hostname
read -p 'Username: ' username
read -sp 'Password: ' password

sshpass -p $password scp index.html $username@$hostname:public_html/
