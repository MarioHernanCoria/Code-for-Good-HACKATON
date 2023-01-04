create database hackaton2;
use hackaton2;

CREATE TABLE USUARIO(
UsuarioID int auto_increment primary KEY,
NombreApellido VARCHAR(25) NOT NULL,
Pais VARCHAR(15) NOT NULL,
Pronombres VARCHAR(10) NOT NULL,
UsuarioEmail VARCHAR(30) NOT NULL,
Contrasena VARCHAR(40) NOT NULL,
Username VARCHAR (30) NOT NULL,
Edad int NOT NULL
);

CREATE TABLE ORGANIZACION(
OrgID int auto_increment primary key,
RazonSocial VARCHAR(25) NOT NULL,
Pais VARCHAR(15) NOT NULL,
Ciudad varchar(15) NOT NULL,
OrgEmail VARCHAR(30) NOT NULL,
Contrasena VARCHAR(40) NOT NULL
Telefono int,
Etiquetas VARCHAR(40)
);

CREATE TABLE SUSCRIPCION(
Tier int NOT NULL,
FechaInicio DATE NOT NULL,
FechaFinal DATE NOT NULL,
SuscripcionUsuarioID VARCHAR(20) NOT NULL
);

CREATE TABLE ConsultasUser(
ConsultaUserID int auto_increment primary KEY,
AutorID int NOT NULL,
Contenido VARCHAR(150) NOT NULL,
Tipo VARCHAR(30) NOT NULL,
Respondido VARCHAR(10) NOT NULL,
Fecha date not null
);

CREATE TABLE ConsultasOrg(
ConsultaOrgID int auto_increment primary KEY,
AutorID int NOT NULL,
Contenido VARCHAR(150) NOT NULL,
Tipo VARCHAR(30) NOT NULL,
Respondido VARCHAR(10) NOT NULL,
Fecha date not null
);

CREATE TABLE EVENTOS(
EventoID int auto_increment primary KEY,
EventosOrgID int NOT NULL,
Fecha date NOT NULL,
Ubicacion VARCHAR(20) NOT NULL,
EventoNombre VARCHAR(30) NOT NULL,
EventoDescripcion VARCHAR(150) NOT NULL
);

/*ALTER TABLES*/

/*USUARIO*/
	alter table USUARIO
		add constraint checkNombreUsuario
		check(NombreApellido not like '%[0-9]%');

	alter table USUARIO
		add constraint checkPronombres
		check(Pronombres in ('el', 'ella', 'elle'));
	
	alter table USUARIO
		add constraint checkEmailUser
		check(UsuarioEmail like '%@%');

	alter table USUARIO
		add constraint checkEdad
		check(Edad > 0);

/*ORGANIZACION*/
	alter table ORGANIZACION
		add constraint checkEmailOrg
		check(OrgEmail like '%@%');


/*SUSCRIPCION*/
	alter table SUSCRIPCION
		add constraint checkTier
		check(Tier BETWEEN 0 AND 3);

	alter table SUSCRIPCION
		add constraint fkSuscripcion
		foreign key (SuscripcionUsuarioID) references USUARIO(UsuarioID);
	
/*CONSULTAS USUARIOS*/
	alter table ConsultasUser
		add constraint checkTipoUser
		check(Tipo in ('Evento', 'Promocion/Subir Contenido', 'Consulta', 'Otros'));

	alter table ConsultasUser
		add constraint checkRespondidoConsultasUser
		check(Respondido like 'True' OR Respondido LIKE 'False');

	alter table ConsultasUser
		add constraint fkConsultasUser
		foreign key (AutorID) references USUARIO(UsuarioID);

/*CONSULTAS ORGS*/
	alter table ConsultasOrg
		add constraint checkTipoOrg
		check(Tipo in ('Evento', 'Promocion/Subir Contenido', 'Consulta', 'Otros'));

	alter table ConsultasOrg
		add constraint checkRespondidoConsultasOrg
		check(Respondido like 'True' OR Respondido LIKE 'False');

	alter table ConsultasOrg
		add constraint fkConsultasOrg
		foreign key (AutorID) references ORGANIZACION(OrgID);

/*EVENTOS*/
	alter table EVENTOS
		add constraint fkEventos
		foreign key (EventosOrgID) references ORGANIZACION(OrgID);