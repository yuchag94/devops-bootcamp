#!/bin/bash

echo "📋 Mostrando los primeros 5 números:"
for i in {1..5}; do
  echo "Número: $i"
done

saludar() {
  echo "Hola, $1. ¡Bienvenida al mundo DevOps! 🚀"
}

echo ""
read -p "¿Cuál es tu nombre? " nombre
saludar "$nombre"

