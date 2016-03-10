#Swiss Tournament
This project was conceptualized by the Udacity staff as a practice project for the students of its _Relational Databases_ course.
##Overview
This project simulates a swiss tournament and in that context demonstrates the principles of database design and one complex query against a database. A swiss system tournament is a tournament without eliminations. Competitor face each other in lg(N) rounds. In each round the players are paired such that each players competes with another player that is closest to him/her in ranking.  In this project, the ranking is determined using the match history in the tournament. For more information about Swiss system tournament, please refer to [Wikipedia](https://en.wikipedia.org/wiki/Swiss-system_tournament). 

##Files
###tournament.sql
This is the main document in this project. It sets up the tournament database and its tables. The database has two tables and a view: 
- Players table: with an id and a name field. 
- Matches table: contains id, winner, loser, and draw fields (draw field is never used in the program and is reserved for future)
- Standings view: this view is created using a complex SQL statement explained below. It contains the number of wins and total matches for each player. 

#### Standings SQL statement: 
Here's the SQL statement used to create the Standings view: 
```SQL 
create view standings as (
	select Players.id, name, wins, nummatches from 
		Players join (
		select t1.id, t1.nummatches, t2.wins from (
				select Players.id, count(Matches.winner) as nummatches from 
				Players left join Matches on (Players.id = Matches.loser or Players.id = Matches.winner) group by Players.id
			) as t1 join (
				select Players.id, count(Matches.winner) as wins 
				from Players left join Matches on Players.id = Matches.winner group by Players.id
			)as t2 on t1.id = t2.id
		) t3 on Players.id = t3.id 
	order by t3.wins desc);
```
This statement first creates t1 and t2 tables using sub-statements. Table t1 contains the total number of matches for each player and table t2 contains the number of matches the player has won. Table t3 is then created by joining t1 and t2 and the view is created by joing Players with t3. There are a total of four join operations in this statement and that is why it is complex. 

###tournament.py 
This file provides methods to interact with our PostgreSQL database using Python's psycopg2 library. 

###tournament_test.py 
This file tests the methods in tournament.py. Most of the code in this file was provided by the Udacity.com staff. 

##Deployment
In order to test the code in this project you must first install the PostgreSQL server on your computer followed by Python2. After that you can run the code by typing `psql -f tournament.sql && python tournament_test.py` into your terminal. Alternatively, you can substitute PostgreSQL with your database system to deploy the project. 
