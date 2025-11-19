#!/bin/bash

echo "cual es la dieccion ip"
read ip_ades
echo "cual es el puerto"
read $port
echo "cual es el archivo que quieres descargar"
read file
ncat $ip_adres $port $file
