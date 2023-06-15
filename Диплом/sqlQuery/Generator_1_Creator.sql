CREATE TABLE [CHP_generator_1] (
   Time datetime NOT NULL PRIMARY KEY,
   [Temperature] float NOT NULL,
   [Fuel consumption] float NOT NULL,
   [Power] float NOT NULL,
   [Amperage] float NOT NULL,
   [Voltage] float NOT NULL
);

DECLARE @prev_temperature FLOAT = 30;
DECLARE @prev_fuel_cons FLOAT = 30;
DECLARE @prev_power FLOAT = 50;
DECLARE @prev_voltage FLOAT = 220;
DECLARE @prev_amperage FLOAT = 45;

DECLARE @i INT = 0;

WHILE @i < 1000
BEGIN
   SET @prev_temperature = @prev_temperature + (RAND() * 10 - 5);
   SET @prev_fuel_cons = @prev_fuel_cons + (RAND() * 10 - 5);
   SET @prev_power = @prev_voltage + (RAND() * 10 - 5);
   SET @prev_voltage = @prev_voltage + (RAND() * 10 - 5);
   SET @prev_amperage = @prev_amperage + (RAND() * 10 - 5);

   INSERT INTO [CHP_generator_1] (Time, [Temperature], [Fuel consumption], [Power], [Amperage], [Voltage])
   VALUES (DATEADD(minute, 5*@i, CAST('2022-12-12 00:00:00' AS datetime)), @prev_temperature, @prev_fuel_cons, @prev_power, @prev_voltage, @prev_amperage);
   SET @i = @i + 1;
END;

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE [CHP_transformer_1] (
   Time datetime,
   [Temperature] float,
   [Primary winding voltage] float,
   [Secondary  winding voltage] float,
   [Primary winding amperage] float,
   [Secondary  winding amperage] float
);

SET @prev_temperature = 30;
DECLARE @prev_pw_voltage FLOAT = 110;
DECLARE @prev_sw_voltage FLOAT = 220;
DECLARE @prev_pw_amperage FLOAT = 60;
DECLARE @prev_sw_amperage FLOAT = 45;

SET @i = 0;

WHILE @i < 1000
BEGIN
   SET @prev_temperature = @prev_temperature + (RAND() * 10 - 5);
   SET @prev_pw_voltage = @prev_pw_voltage + (RAND() * 10 - 5);
   SET @prev_sw_voltage = @prev_sw_voltage + (RAND() * 10 - 5);
   SET @prev_pw_amperage = @prev_pw_amperage + (RAND() * 10 - 5);
   SET @prev_sw_amperage = @prev_sw_amperage + (RAND() * 10 - 5);

   INSERT INTO [CHP_transformer_1] (Time, [Temperature], [Primary winding voltage], [Secondary  winding voltage], [Primary winding amperage], [Secondary  winding amperage])
   VALUES (DATEADD(minute, 5*@i, CAST('2022-12-12 00:00:00' AS datetime)), @prev_temperature, @prev_pw_voltage, @prev_sw_voltage, @prev_pw_amperage, @prev_sw_amperage);
   SET @i = @i + 1;
END;

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE [Cooling_tower_1] (
   Time datetime,
   [Temperature] float,
   [Water consumption] float,
   [Inlet pressure] float,
   [Outlet pressure] float,
);

SET @prev_temperature = 30;
DECLARE @prev_consumption FLOAT = 50;
DECLARE @prev_in_pressure FLOAT = 20;
DECLARE @prev_out_pressuree FLOAT = 15;

SET @i = 0;

WHILE @i < 1000
BEGIN
   SET @prev_temperature = @prev_temperature + (RAND() * 10 - 5);
   SET @prev_consumption = @prev_consumption + (RAND() * 10 - 5);
   SET @prev_in_pressure = @prev_in_pressure + (RAND() * 10 - 5);
   SET @prev_out_pressuree = @prev_out_pressuree + (RAND() * 10 - 5);

   INSERT INTO [Cooling_tower_1] (Time, [Temperature], [Water consumption], [Inlet pressure], [Outlet pressure])
   VALUES (DATEADD(minute, 5*@i, CAST('2022-12-12 00:00:00' AS datetime)), @prev_temperature, @prev_consumption, @prev_in_pressure, @prev_out_pressuree);
   SET @i = @i + 1;
END;

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

