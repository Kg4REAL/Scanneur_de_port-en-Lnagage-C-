# Scanneur_de_port-en-Lnagage-C-

# 🔍 Scanneur de Ports en Langage C

Ce projet est un outil simple de **scan de ports TCP**, écrit en **langage C**, permettant de détecter les ports ouverts sur une machine cible.

## 🚀 Fonctionnalités

- Scanner les ports d'une adresse IP spécifiée
- Détection des ports ouverts
- Affichage clair des résultats dans le terminal
- Rapide et léger

## 🛠️ Technologies utilisées

- Langage : C
- Librairies : `stdio.h`, `stdlib.h`, `string.h`, `unistd.h`, `arpa/inet.h`, `sys/socket.h`

## 📦 Installation

### 1. Cloner le dépôt :
```bash
git clone git@github.com:Kg4REAL/Scanneur_de_port-en-Lnagage-C-.git
cd Scanneur_de_port-en-Lnagage-C-
gcc -o scanneur scanneur.c
