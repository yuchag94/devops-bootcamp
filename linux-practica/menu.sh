#!/bin/bash

echo "Hola Yuliet, elige una opcion:"
echo "1. Mostrar fecha actual"
echo "2. Mostrar contenido de la carpeta actual"
echo "3. Salir"

read opcion

case $opcion in
	1) date ;;
	2) ls -la ;;
	3) echo "Adios .." ;;
	*) echo "Opcion invalida" ;;
esac

