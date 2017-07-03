# Udacity Tournament database project
This project is for for Udacity's **Full Stack nanodegree program**. 
The project implements a simple swiss-system game tournament to demonstrate both simple and complex SQL queries using PostgreSQL.

## Table of contents
* [Setting up](#setting-up)
  * [Setting up the development environment](#1-setting-up-the-development-environment)
  * [Downloading the repository](#2-downloading-the-repository)
  * [Setting up the database](#3-setting-up-the-database)
  * [Running the project](#4-running-the-project)
* [Included functions](#functions)

## Setting up
Follow these steps to successfully run the application.

### 1. Setting up the development environment
To make sure you have all the required dependicies to run this project, you should set up [Udacity's fullstack-nanodegree virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)
using [Vagrant](https://www.vagrantup.com/).
1. Install Vagrant
2. Pick a location to store this VM and run `git clone https://github.com/udacity/fullstack-nanodegree-vm`
3. Navigate to the `fullstack-nanodegree-vm/vagrant` directory
4. Run the VM with `vagrant up`
5. After the setup is done, connect to the VM with `vagrant ssh`

### 2. Downloading the repository
Now it's time to obtain the project files. 
1. Navigate to vagrant's shared folder (`fullstack-nanodegree-vm/vagrant`)
2. Clone this repository `git clone https://github.com/raideer/udacity-project-tournament-db`

### 3. Setting up the database
1. Go to your VM (after running vagrant ssh) and navigate to this repo's location `cd /vagrant/udacity-project-tournament-db`
2. Run PostgreSQL interactive terminal using the command `psql`
3. And now to make the database and create the tables, run `\i tournament.sql`

### 4. Running the project
Now that we have obtained all the required files and set up the database, we can start using the project files.

* **tournament.py** file contains all the functions necessary for running a swiss-system tournament.
* **tournament_test.py** file unit tests the `tournament.py` file to make sure everything is working.
* **tournament.sql** contains all the table definitions for our database

## Functions
These are the functions that are included in the **tournament.py** file

#### deleteMatches()
Remove all the match records from the database

#### deletePlayers()
Remove all the player records from the database

#### countPlayers()
Returns the number of players currently registered

#### registerPlayer(name)
Adds a player to the tournament database  
Args:  
* **name**: the player's full name (need not be unique).
      
#### playerStandings()
Returns a list of the players and their win records, sorted by wins

#### reportMatch(winner, loser)
Records the outcome of a single match between two players.  
Args:  
* **winner**:  the id number of the player who won
* **loser**:  the id number of the player who lost

#### swissPairings()
Returns a list of pairs of players for the next round of a match
