CREATE TABLE Turbine_1 (
   Time datetime,
   [HW supply temperature] float,
   [HW release temperature] float,
   [HW supply pressure] float,
   [HW release pressure] float,
   [Fuel supply temperaure] float,
   [Fuel supply pressure] float,
   [Steam volume] float,
   [Steam pressure] float,
   [Gas consumption] float,
   [Water consumption] float,
   [Power consumption] float,
   [Total capacity] float,
);

DECLARE @i int = 0;

WHILE @i < 1000
BEGIN
   INSERT INTO Turbine_1 (Time, [HW supply temperature], [HW release temperature], [HW supply pressure], [HW release pressure], [Fuel supply temperaure], [Fuel supply pressure], 
		[Steam volume], [Steam pressure], [Gas consumption], [Water consumption], [Power consumption], [Total capacity])
   VALUES (DATEADD(minute, 5*@i, CAST('2022-12-12 00:00:00' AS datetime)), RAND(), RAND(), RAND(), RAND(), RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND());
   SET @i = @i + 1;
END;

CREATE TABLE Turbine_2 (
   Time datetime,
   [HW supply temperature] float,
   [HW release temperature] float,
   [HW supply pressure] float,
   [HW release pressure] float,
   [Fuel supply temperaure] float,
   [Fuel supply pressure] float,
   [Steam volume] float,
   [Steam pressure] float,
   [Gas consumption] float,
   [Water consumption] float,
   [Power consumption] float,
   [Total capacity] float,
);

SET @i = 0;

WHILE @i < 1000
BEGIN
   INSERT INTO Turbine_2 (Time, [HW supply temperature], [HW release temperature], [HW supply pressure], [HW release pressure], [Fuel supply temperaure], [Fuel supply pressure], 
		[Steam volume], [Steam pressure], [Gas consumption], [Water consumption], [Power consumption], [Total capacity])
   VALUES (DATEADD(minute, 5*@i, CAST('2022-12-12 00:00:00' AS datetime)), RAND(), RAND(), RAND(), RAND(), RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND());
   SET @i = @i + 1;
END;

CREATE TABLE [Boiler_Room_1] (
   Time datetime,
   [HW supply temperature] float,
   [HW release temperature] float,
   [HW supply pressure] float,
   [HW release pressure] float,
   [Fuel supply temperaure] float,
   [Fuel supply pressure] float,
   [Steam volume] float,
   [Steam pressure] float,
   [Gas consumption] float,
   [Water consumption] float,
   [Power consumption] float,
   [Total capacity] float,
);

SET @i = 0;

WHILE @i < 1000
BEGIN
   INSERT INTO [Boiler_Room_1] (Time, [HW supply temperature], [HW release temperature], [HW supply pressure], [HW release pressure], [Fuel supply temperaure], [Fuel supply pressure], 
		[Steam volume], [Steam pressure], [Gas consumption], [Water consumption], [Power consumption], [Total capacity])
   VALUES (DATEADD(minute, 5*@i, CAST('2022-12-12 00:00:00' AS datetime)), RAND(), RAND(), RAND(), RAND(), RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND());
   SET @i = @i + 1;
END;

CREATE TABLE [Cooling_Tower_1] (
   Time datetime,
   [HW supply temperature] float,
   [HW release temperature] float,
   [HW supply pressure] float,
   [HW release pressure] float,
   [Fuel supply temperaure] float,
   [Fuel supply pressure] float,
   [Steam volume] float,
   [Steam pressure] float,
   [Gas consumption] float,
   [Water consumption] float,
   [Power consumption] float,
   [Total capacity] float,
);

SET @i = 0;

WHILE @i < 1000
BEGIN
   INSERT INTO [Cooling_Tower_1] (Time, [HW supply temperature], [HW release temperature], [HW supply pressure], [HW release pressure], [Fuel supply temperaure], [Fuel supply pressure], 
		[Steam volume], [Steam pressure], [Gas consumption], [Water consumption], [Power consumption], [Total capacity])
   VALUES (DATEADD(minute, 5*@i, CAST('2022-12-12 00:00:00' AS datetime)), RAND(), RAND(), RAND(), RAND(), RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND(),  RAND());
   SET @i = @i + 1;
END;