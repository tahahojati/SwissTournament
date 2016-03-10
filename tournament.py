#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    myC = mydb.cursor(); 
    myC.execute("delete from Matches;");
    mydb.commit();
    del myC




def deletePlayers():
    """Remove all the player records from the database."""
    myC = mydb.cursor(); 
    myC.execute("delete from Players;");
    mydb.commit()
    del myC

def countPlayers():
    """Returns the number of players currently registered."""
    myC = mydb.cursor(); 
    myC.execute("select count(*) from Players;");
    mynum = myC.fetchone()[0]
    del myC
    return mynum
def registerPlayer(name):
    myC = mydb.cursor(); 
    myC.execute("insert into Players (name)  values (%s);", [name]);
    mydb.commit()
    del myC
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """



def playerStandings():
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
    myC = mydb.cursor(); 
    myC.execute(" select * from standings;");
    return myC.fetchall(); 


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    myC = mydb.cursor()
    myC.execute("insert into Matches (winner, loser) values (%s,%s) ; ", [winner, loser])
    mydb.commit()
    del myC
 
def swissPairings():
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
    myStanding = playerStandings()
    return [(myStanding[i][0],myStanding[i][1],myStanding[i+1][0],myStanding[i+1][1]) for i in range(0, len(myStanding), 2) ]
#create a connection to the database 
mydb = connect()
