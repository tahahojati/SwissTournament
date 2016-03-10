-- Table definitions for the tournament project.
--This file is used to set up the database. 

drop database if exists tournament;
create database tournament;
\c tournament;
create table Players (id serial primary key, name text, score int default 0);
create table Matches (id serial, winner int references Players(id), 
	loser int references Players(id), draw boolean default false);
insert into Players (name) values ('joe'),('mike'),('jose'),('julie'),('Quinten'),('Sarah'), ('LL'), ('kmi');
insert into Matches (winner, loser) values (1,2), (3,4), (5,6), (8,7), (8,1), (6,3), (5,7); 
-- the code below creates a view that contains the number of wins and total number of matches for each team. 
create view standings as (select Players.id, name, wins, nummatches from Players join 
	(select t1.id, t1.nummatches, t2.wins from (select Players.id, count(Matches.winner) as nummatches from Players left join Matches on 
	(Players.id = Matches.loser or Players.id = Matches.winner) group by Players.id) as t1 join ( select Players.id, count(Matches.winner) as 
	wins from Players left join Matches on Players.id = Matches.winner group by Players.id)as t2 on t1.id = t2.id) t3 on Players.id = t3.id 
	order by t3.wins desc);