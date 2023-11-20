-- Inserciones
-- PRODUCT_TYPES
INSERT INTO PRODUCT_TYPES VALUES(NULL, 'EMERGENCIA');
INSERT INTO PRODUCT_TYPES VALUES(NULL, 'REFRIGERADOS');
INSERT INTO PRODUCT_TYPES VALUES(NULL, 'CRONICOS');
INSERT INTO PRODUCT_TYPES VALUES(NULL, 'COMUN');

-- PRODUCTS
INSERT INTO PRODUCTS VALUES(NULL, 'EPINEFRINA', 'Trata reacciones alérgicas graves, como anafilaxia, revertiendo síntomas peligrosos como dificultad respiratoria y shock', 1);
INSERT INTO PRODUCTS VALUES(NULL, 'NITROGLICERINA', 'Alivia el dolor en el pecho durante emergencias cardíacas, mejorando el flujo sanguíneo al corazón', 1);
INSERT INTO PRODUCTS VALUES(NULL, 'ALBUTEROL', 'Broncodilatador que abre las vías respiratorias en emergencias, como ataques agudos de asma', 1);
INSERT INTO PRODUCTS VALUES(NULL, 'GLUCAGON', ' Eleva los niveles de glucosa en sangre en emergencias hipoglucémicas, contrarrestando la falta de azúcar', 1);

INSERT INTO PRODUCTS VALUES(NULL, 'INSULINA', 'Medicamento crucial para personas con diabetes, requiere refrigeración para mantener su eficacia en el control del azúcar en sangre', 2);
INSERT INTO PRODUCTS VALUES(NULL, 'VACUNA CONTRA LA GRIPE', 'Vacuna anual para prevenir la gripe, se almacena en condiciones refrigeradas para preservar su potencia', 2);
INSERT INTO PRODUCTS VALUES(NULL, 'AMOXICILINA', 'Antibiótico común, la versión líquida puede requerir refrigeración para mantener su estabilidad y eficacia', 2);
INSERT INTO PRODUCTS VALUES(NULL, 'SPR', 'Vacuna esencial para la inmunización infantil, debe mantenerse refrigerada para garantizar su eficacia', 2);

INSERT INTO PRODUCTS VALUES(NULL, 'ATORVASTATINA', 'Medicamento para reducir el colesterol en pacientes con enfermedades cardíacas crónicas', 3);
INSERT INTO PRODUCTS VALUES(NULL, 'METFORMINA', 'Tratamiento para la diabetes tipo 2, utilizado de manera crónica para controlar los niveles de azúcar en sangre', 3);
INSERT INTO PRODUCTS VALUES(NULL, 'WARFARINA', 'Anticoagulante oral usado crónicamente para prevenir la formación de coágulos sanguíneos', 3);
INSERT INTO PRODUCTS VALUES(NULL, 'ENALAPRIL', 'Medicamento para la hipertensión arterial, tomado de forma crónica para controlar la presión arterial', 3);

INSERT INTO PRODUCTS VALUES(NULL, 'PARACETAMOL', 'Analgésico y antipirético utilizado comúnmente para aliviar el dolor y reducir la fiebre', 4);
INSERT INTO PRODUCTS VALUES(NULL, 'IBUPROFENO', 'Antiinflamatorio no esteroideo (AINE) que alivia el dolor y reduce la inflamación', 4);
INSERT INTO PRODUCTS VALUES(NULL, 'RANITIDINA', 'Antagonista de los receptores H2 utilizado para reducir la producción de ácido en el estómago', 4);
INSERT INTO PRODUCTS VALUES(NULL, 'LORATADINA', 'Antihistamínico utilizado para tratar alergias y sus síntomas, como la congestión nasal y el picor', 4);

-- PHARMACIES
INSERT INTO PHARMACIES VALUES(NULL, 'SALUDEXPRESS', '901234567-1', 5.545254, -73.360222);
INSERT INTO PHARMACIES VALUES(NULL, 'VIDAFARMACIAS', '902345678-2', 5.537939, -73.368949);
INSERT INTO PHARMACIES VALUES(NULL, 'BIENESTARFARMA', '903456789-3', 5.532341, -73.364480);
INSERT INTO PHARMACIES VALUES(NULL, 'FARMARAPIDA', '904567890-4', 5.536932, -73.358593);
INSERT INTO PHARMACIES VALUES(NULL, 'FARMAPLUS', '905678901-5', 5.549799, -73.352038);
INSERT INTO PHARMACIES VALUES(NULL, 'SALUDTOTAL', '906789012-6', 5.546548, -73.353442);
INSERT INTO PHARMACIES VALUES(NULL, 'VITALFARMA', '907890123-7', 5.533520, -73.359649);
INSERT INTO PHARMACIES VALUES(NULL, 'MEGAFARMACIAS', '908901234-8', 5.535543, -73.348472);
INSERT INTO PHARMACIES VALUES(NULL, 'ECOFARMA', '909012345-9', 5.548542, -73.363880);
INSERT INTO PHARMACIES VALUES(NULL, 'LA REBAJA', '905678232-1', 5.528048, -73.348237);
INSERT INTO PHARMACIES VALUES(NULL, 'DISTRIBUIDORA FARMASEC', '954829174-2', 5.552584, -73.350291);

-- PHARMACY_CONECTIONS
INSERT INTO PHARMACY_CONECTIONS VALUES(1,9);
INSERT INTO PHARMACY_CONECTIONS VALUES(9,2);
INSERT INTO PHARMACY_CONECTIONS VALUES(2,9);
INSERT INTO PHARMACY_CONECTIONS VALUES(2,6);
INSERT INTO PHARMACY_CONECTIONS VALUES(6,2);
INSERT INTO PHARMACY_CONECTIONS VALUES(5,1);
INSERT INTO PHARMACY_CONECTIONS VALUES(5,8);
INSERT INTO PHARMACY_CONECTIONS VALUES(8,5);
INSERT INTO PHARMACY_CONECTIONS VALUES(8,10);
INSERT INTO PHARMACY_CONECTIONS VALUES(10,7);
INSERT INTO PHARMACY_CONECTIONS VALUES(7,3);
INSERT INTO PHARMACY_CONECTIONS VALUES(7,4);
INSERT INTO PHARMACY_CONECTIONS VALUES(4,8);
INSERT INTO PHARMACY_CONECTIONS VALUES(3,1);
INSERT INTO PHARMACY_CONECTIONS VALUES(3,2);
INSERT INTO PHARMACY_CONECTIONS VALUES(8,3);
INSERT INTO PHARMACY_CONECTIONS VALUES(3,8);
INSERT INTO PHARMACY_CONECTIONS VALUES(6,9);
INSERT INTO PHARMACY_CONECTIONS VALUES(3,5);
INSERT INTO PHARMACY_CONECTIONS VALUES(11,6);
INSERT INTO PHARMACY_CONECTIONS VALUES(11,9);
INSERT INTO PHARMACY_CONECTIONS VALUES(6,11);
INSERT INTO PHARMACY_CONECTIONS VALUES(5,11);


DROP TABLE PHARMACY_CONECTIONS;
DROP TABLE PHARMACIES;
DROP TABLE PRODUCTS;
DROP TABLE PRODUCT_TYPES;

SELECT * FROM PRODUCT_TYPES;

UPDATE SQLITE_SEQUENCE SET SEQ = 0 WHERE NAME = 'PHARMACIES';

SELECT * FROM PHARMACIES;
SELECT * FROM PRODUCT_TYPES;