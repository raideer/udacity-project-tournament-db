#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2 as psql
import bleach

# a simple decorator to handle database connections
def requires_connection(f):
    def wrapper(*args, **kwargs):
        db = psql.connect("dbname=tournament")
        cursor = db.cursor()
        # pass the connection and cursor as arguments
        kwargs['db'] = db
        kwargs['cursor'] = cursor
        value = f(*args, **kwargs)
        # close the connection after the function has completed running
        db.close()

        return value
    return wrapper

@requires_connection
def deleteMatches(db, cursor):
    """Remove all the match records from the database."""
    cursor.execute('delete from matches')
    db.commit()

@requires_connection
def deletePlayers(db, cursor):
    """Remove all the player records from the database."""
    cursor.execute('delete from players')
    db.commit()

@requires_connection
def countPlayers(db, cursor):
    """Returns the number of players currently registered."""
    cursor.execute('select count(*) from players')
    results =  cursor.fetchone()
    return results[0]

@requires_connection
def registerPlayer(name, db, cursor):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    # sanitizing input with bleach
    cursor.execute('insert into players (name) values(%s)', (bleach.clean(name),))
    db.commit()

@requires_connection
def playerStandings(db, cursor):
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    cursor.execute('select * from standings')
    return cursor.fetchall()

@requires_connection
def reportMatch(winner, loser, db, cursor):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    cursor.execute('insert into matches (winner, loser) values (%s, %s)', (winner, loser,))
    db.commit()

@requires_connection
def swissPairings(db, cursor):
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    pairings = []

    # since playerStandings() returns list of players sorted by wins,
    # we can just consecutively group them by 2
    for x in range(0, len(standings) - 1, 2):
        player1 = standings[x]
        player2 = standings[x + 1]
        pairings.append( (player1[0], player1[1], player2[0], player2[1]) )

    return pairings
