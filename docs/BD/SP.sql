use EDUCOEMOCIONES;

drop procedure if exists sp_Login;
delimiter **
create procedure sp_Login(in usr varchar(32), in psw varchar(32))
begin
declare existe int;
declare msj varchar(32);
set existe = (select count(*) from administrador where administrador.usuario=usr);
	if existe = 0 then
		set msj = "El usuario no existe";
	else
		set existe = (select count(*) from administrador where administrador.contrasenia=psw);
        if existe = 0 then
			set msj = "Contraseña invalida";
        else
			set existe = (select count(*) from administrador where administrador.usuario=usr and administrador.contrasenia=psw);
            if existe = 0 then
				set msj = "Credenciales invalidas";
            else
				set msj = "Bienvenid@ al sistema";
            end if;
        end if;
    end if;
	select msj as Respuesta;
end **
delimiter ;


drop procedure if exists sp_insertar_usuario;
delimiter **
create procedure sp_insertar_usuario(in nom varchar(32), in eda varchar(2), in gener varchar(16), grad varchar(16))
begin
declare existe int;
declare msj varchar(32);
set existe = (select count(*) from infante where infante.nombre=nom);
	if existe = 0 then
		set msj = "Infante registrado";
        insert into infante values(nom,eda,gener,grad);
	else
		set msj = "Infante existente";
    end if;
    select msj as Respuesta;
end **
delimiter ;

# call sp_Login('admin','1234');
call sp_insertar_usuario('Juan','10','Femenino','4to primaria');
select * from infante;