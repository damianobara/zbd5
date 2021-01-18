begin;

create schema zad5;

create table zad5.person (
  id               text primary key,
  gender           char(1),
  birth            date,
  income           integer,
  longitude        float,
  latitude         float,
  interests        text []
);

create table zad5.ad (
    id             text primary key,
    hight          integer,
    width          integer,
    texts          text [],
    color          text
);

create table zad5.view (
    person_id      text not null references zad5.person(id),
    ad_id          text not null references zad5.ad(id),
    view_time      timestamp
);

commit;