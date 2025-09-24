CREATE PROCEDURE cancelarOrden(
    IN p_clienteID INT
)
BEGIN
    DECLARE v_ordenID INT;

    SELECT ordenID INTO v_ordenID
    FROM ordenes
    WHERE clienteID = p_clienteID AND enCurso = false
    LIMIT 1;
    
    if v_ordenID is not null then 
		update detalle_orden
		set quantity=0
		where ordenID=v_ordenID;
		UPDATE ordenes
		SET precioTotal = 0
		WHERE ordenID = v_ordenID;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No existe una orden en curso para este cliente';
    END IF;
end
