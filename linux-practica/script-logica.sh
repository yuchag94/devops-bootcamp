#!/bin/bash

echo "Cual es tu nombre?"
read nombre

if [ "$nombre" = "Yuliet" ]; then
  echo "¡Hola profe DevOps!"
else
  echo "Hola $nombre"
fi

