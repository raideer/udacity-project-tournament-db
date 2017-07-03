-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- create table tournaments (
--   id serial primary key,
--   name text
-- );

create database tournament;
\c tournament

create table players (
  id serial primary key,
  name text
);

create table matches (
  id serial primary key,
  loser integer references players(id),
  winner integer references players(id)
);

create view matches_won as select players.id, count(matches.winner) as count from players
left join matches on players.id = matches.winner
group by players.id;

create view matches_played as select players.id, count(matches.id) as count from players
left join matches on players.id = matches.loser or players.id = matches.winner
group by players.id;

create view standings as select players.id, players.name, matches_won.count as matches_won, matches_played.count as matches_played
from players, matches_won, matches_played
where players.id = matches_won.id
and players.id = matches_played.id
order by matches_won.count desc;
