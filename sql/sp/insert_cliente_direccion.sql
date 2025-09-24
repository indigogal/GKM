CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertarCliente_Direccion`(

IN p_nombre VARCHAR(100),
-- IN p_direccionDeEntregas INT, 
IN p_email VARCHAR(100),
IN p_telefono VARCHAR(100),
IN p_calle VARCHAR(100),
IN p_numero VARCHAR(100),
IN p_numeroInt VARCHAR(100),
IN p_codigoPost VARCHAR(100),
IN p_referenciasExtra VARCHAR(100)
)
BEGIN
INSERT INTO direcciones(calle,numero,numeroInt,codigoPost,referenciasExtra)
VALUES (p_calle,p_numero,p_numeroInt,p_codigoPost,p_referenciasExtra);
 
 SET @ultimaDireccionID = LAST_INSERT_ID();

INSERT INTO clientes (nombre,direccionDeEntregas,email,telefono)
VALUES (p_nombre,@ultimaDireccionID,p_email,p_telefono);

 
END