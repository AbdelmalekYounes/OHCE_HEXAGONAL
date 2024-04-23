# Projet OHCE PROTOTYPE

Le projet OHCE est une application Python qui offre une interface console ainsi qu'une API web pour interagir avec l'utilisateur de manière ludique en renvoyant les entrées textuelles en miroir. Si l'entrée est un palindrome, l'application répond "Bien dit !" ou "Well said!" selon la langue configurée.

## Fonctionnalités

- Salutations personnalisées selon l'heure de la journée.
- Réponse en miroir des entrées de l'utilisateur.
- Détection des palindromes.
- Adieux personnalisés selon l'heure de la journée.
- Support multilingue (Français, Anglais).

## Prérequis

- Python 3.6 ou plus récent.
- Flask pour l'API web.

## Installation

Clonez ce dépôt et installez les dépendances nécessaires :

```bash
git clone https://your-repository-url/ohce_project.git
cd ohce_project
pip install flask

```

## Utilisation

### Mode Console

Pour démarrer l'application en mode console, exécutez la commande suivante :
```bash
python main.py
```
Suivez les instructions affichées pour interagir avec l'application via la console.

## Mode API Web

Pour démarrer l'application en mode API, utilisez la commande suivante :
```bash
python main.py api
```
L'API sera alors accessible via http://localhost:5000.

#### Intéragir avec l'API

Utilisez curl pour envoyer des requêtes à l'API comme suit :
```bash
curl -X POST http://localhost:5000/echo -H "Content-Type: application/json" -H "Accept-Language: {Langue}" -d "{\"input\":\"votre texte ici\"}"
```
Pour terminer la session via l'API, envoyez "exit" comme entrée :
```bash
curl -X POST http://localhost:5000/echo -H "Content-Type: application/json" -d "{\"input\":\"exit\"}"
```


