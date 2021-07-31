drop database if exists EDUCOEMOCIONES;
create database EDUCOEMOCIONES;
use EDUCOEMOCIONES;

create table if not exists administrador(
	usuario varchar(32) not null primary key,
    contrasenia varchar(32) not null
);

create table if not exists infante(
	nombre varchar(32) not null primary key,
    edad varchar(2) not null,
    genero varchar(16) not null,
    grado varchar(16) not null
);

create table if not exists preguntas(
	nombre_infante varchar(32) not null,
	modulo int(4) not null,
    sesion int(2) not null,
    submod int(2) not null,
    numPre int(2) not null,
    valor varchar(2) not null,
    fecha datetime default current_timestamp,
    foreign key (nombre_infante) references infante(nombre) on delete cascade on update cascade,
    primary key (modulo,sesion,submod,numPre)
);

create table if not exists ses_intervencion(
	nombre_infante varchar(32) not null,
	modulo int(4) not null,
    sesion int(2) not null,
    submod int(2) not null,
    numPre int(2) not null,
    valor varchar(64) not null,
    fecha datetime default current_timestamp,
    foreign key (nombre_infante) references infante(nombre) on delete cascade on update cascade,
    primary key (modulo,sesion,submod,numPre)
);

insert into administrador values('admin2','1234');
select * from administrador;