CREATE PROCEDURE `crearOrden`(

    IN p_clienteID INT,
    IN p_qtyMenuSaludable INT,
    IN p_qtyMenuEcon INT
)
BEGIN
    DECLARE v_precioTotal INT;
    DECLARE v_numSemana INT;
    DECLARE v_year INT;
    DECLARE v_ordenID INT;

 IF (p_qtyMenuSaludable = 0 AND p_qtyMenuEcon = 0) THEN
 signal sqlstate '45000'
   SET MESSAGE_TEXT = 'Debe ordenar al menos un menú';
    END IF;

 SET v_precioTotal = (p_qtyMenuEcon * 200) + (p_qtyMenuSaludable * 300);
SET v_numSemana = WEEK(CURRENT_DATE()) + 1;
SET v_year = YEAR(CURRENT_DATE());

INSERT INTO ordenes(clienteID, precioTotal, enCurso, fechaApartado, numSemana, year)
VALUES(p_clienteID, v_precioTotal, FALSE, CURRENT_DATE(), v_numSemana, v_year);

 SET v_ordenID = LAST_INSERT_ID();
 
 if(p_qtyMenuSaludable>0)then 
	 insert into detalle_orden(ordenID, menuSemanalID, cantidad)
	 SELECT v_ordenID, m.menuSemanalID, p_qtyMenuSaludable 
	 FROM menuSemanal m 
	 WHERE m.numSemana = v_numSemana AND m.anio=v_year and m.tipo='Saludable'
	 limit 1;
END IF;

    IF (p_qtyMenuEcon > 0) THEN
        INSERT INTO detalle_orden(ordenID, menuSemanalID, cantidad)
        SELECT v_ordenID, m.menuSemanalID, p_qtyMenuEcon
        FROM menuSemanal m
        WHERE m.numSemana = v_numSemana AND m.year = v_year AND m.tipo = 'Económico'
        LIMIT 1;
    END IF;


END
