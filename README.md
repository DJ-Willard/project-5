# UOCIS322 - Project 5 #
Brevet time calculator with MongoDB!

## Overview

We add a storage to your previous project using MongoDB and `docker-compose`.
As we discussed, `docker-compose` makes it easier to create, manage and connect multiple container to create a single service comprised of different sub-services.

Presently, there's only a placeholder directory for your Flask app, and a `docker-compose` configuration file. You will copy over `brevets/` from your completed project 4, add a MongoDB service to docker-compose and your Flask app. You will also add two buttons named `Submit` and `Display` to the webpage. `Submit` must store the information (brevet distance, start time, checkpoints and their opening and closing times) in the database (overwriting existing ones). `Display` will fetch the information from the database and fill in the form with them.

Recommended: Review [MongoDB README](MONGODB.md) and[Docker Compose README](COMPOSE.md).

## Tasks

1. Add two buttons `Submit` and `Display` in the ACP calculator page.

	- Upon clicking the `Submit` button, the control times should be inserted into a MongoDB database, and the form should be cleared (reset) **without** refreshing the page.

	- Upon clicking the `Display` button, the entries from the database should be filled into the existing page.

	- Handle error cases appropriately. For example, Submit should return an error if no control times are input. One can imagine many such cases: you'll come up with as many cases as possible.

2. An automated `nose` test suite with at least 2 test cases: at least one for for DB insertion and one for retrieval.

3. Update README.md with brevet control time calculation rules (you were supposed to do this for Project 4), and additional information regarding this project.
	- This project will be peer-reviewed, so be thorough.

## Project Update and Description

* We used docker compose to create a database and a Flask API for the Code we edited in P4.
* We then updated calc.html to use AJAK the reverse of P3.
* We add submit and display buttons that we pass values though JSON passes
* Form there we added a doc 'brevetsmongo.py` that handles all the logic for mongo db and the interactions was added to the 'flask_brevet.py'
* We then implemented an automated test to ensure everything was working.
* please referance Helpful Examples below for implemention logic help:

DockerMongo
https://github.com/UO-CIS322/DockerMongo: Just a basic Flask app that talks to a MongoDB service through the network set up by docker compose.

TodoListApp
https://github.com/UO-CIS322/TodoListApp: A simple web-based to-do list based on Flask and MongoDB, with AJAX interactions!

## Authors

Daniel Willard
