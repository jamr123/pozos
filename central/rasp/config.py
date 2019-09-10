#Ubidots Log
"""
UBIDOTS_TOKEN = 'BBFF-HHmBlj5C4CVgIrlBjgakdtyeFsYx1p' 
UBIDOTS_API_KEY='BBFF-7bacbcf068b323745bbdb16423f195797bb'
UBIDOTS_NAME_DEVICE ='Prueba' 
"""

UBIDOTS_TOKEN = 'BBFF-IH5I4OcjNkdFY6IAcKjnBhbdEThV8j' 
UBIDOTS_API_KEY='BBFF-e95568780d8217c718fac68bf30c60c2c30'
REPORT_TIMER=60
#DEVICES
UBIDOTS_POZOS='POZOS'
UBIDOTS_TEMPERATURAS='TEMPERATURAS'
UBIDOTS_ESTANQUES='ESTANQUES_AGUA'

#POZO 1
UBIDOTS_POZO_1_NiVEL_1="POZO_1_nivel_1"
UBIDOTS_POZO_1_NiVEL_2="POZO_1_nivel_1"
UBIDOTS_POZO_1_PRESION_1="POZO_1_presion_1"
UBIDOTS_POZO_1_PRESION_2="POZO_1_presion_2"
UBIDOTS_POZO_1_CAUDAL_1="POZO_1_caudal_1"
UBIDOTS_POZO_1_CAUDAL_2="POZO_1_caudal_2"
POZO_1_MEDIDA_NIVEL_1=50
POZO_1_INSTALACION_NIVEL_1=50
POZO_1_MEDIDA_NIVEL_2=50
POZO_1_INSTALACION_NIVEL_2=50
POZO_1_PRESION_1=10
POZO_1_PRESION_2=10



#POZO2
UBIDOTS_POZO_2_NiVEL_1="POZO_2_nivel_1"
UBIDOTS_POZO_2_NiVEL_2="POZO_2_nivel_2"
UBIDOTS_POZO_2_PRESION_1="POZO_2_presion_1"
UBIDOTS_POZO_2_PRESION_2="POZO_2_presion_2"
UBIDOTS_POZO_2_CAUDAL_1="POZO_2_caudal_1"
UBIDOTS_POZO_2_CAUDAL_2="POZO_2_caudal_2"
POZO_2_MEDIDA_NIVEL_1=50
POZO_2_INSTALACION_NIVEL_1=50
POZO_2_MEDIDA_NIVEL_2=50
POZO_2_INSTALACION_NIVEL_2=50
POZO_2_PRESION_1=10
POZO_2_PRESION_2=10

#POZO3
UBIDOTS_POZO_3_NiVEL_1="POZO_3_nivel_1"
UBIDOTS_POZO_3_NiVEL_2="POZO_3_nivel_1"
UBIDOTS_POZO_3_PRESION_1="POZO_3_presion_1"
UBIDOTS_POZO_3_PRESION_2="POZO_3_presion_2"
UBIDOTS_POZO_3_CAUDAL_1="POZO_3_caudal_1"
UBIDOTS_POZO_3_CAUDAL_2="POZO_3_caudal_2"
POZO_3_MEDIDA_NIVEL_1=50
POZO_3_INSTALACION_NIVEL_1=50
POZO_3_MEDIDA_NIVEL_2=50
POZO_3_INSTALACION_NIVEL_2=50
POZO_3_PRESION_1=10
POZO_3_PRESION_2=10

#ESTANQU1
UBIDOTS_ESTANQUE_1_NiVEL_1="ESTANQUE_1_nivel_1"
UBIDOTS_ESTANQUE_1_NiVEL_2="ESTANQUE_1_nivel_1"
UBIDOTS_ESTANQUE_1_PRESION_1="ESTANQUE_1_presion_1"
UBIDOTS_ESTANQUE_1_PRESION_2="ESTANQUE_1_presion_2"
UBIDOTS_ESTANQUE_1_CAUDAL_1="ESTANQUE_1_caudal_1"
UBIDOTS_ESTANQUE_1_CAUDAL_2="ESTANQUE_1_caudal_2"
ESTANQUE_1_MEDIDA_NIVEL_1=50
ESTANQUE_1_INSTALACION_NIVEL_1=50
ESTANQUE_1_MEDIDA_NIVEL_2=50
ESTANQUE_1_INSTALACION_NIVEL_2=50
ESTANQUE_1_PRESION_1=10
ESTANQUE_1_PRESION_2=10


POZO_1_S1=[4,20,0,POZO_1_MEDIDA_NIVEL_1] #nivel1
POZO_1_S2=[4,20,0,POZO_1_MEDIDA_NIVEL_2] #nivel2
POZO_1_S3=[4,20,0,POZO_1_PRESION_1] #presion1
POZO_1_S4=[4,20,0,POZO_1_PRESION_2] #presion2

POZO_2_S1=[4,20,0,POZO_2_MEDIDA_NIVEL_1] #nivel1
POZO_2_S2=[4,20,0,POZO_2_MEDIDA_NIVEL_2] #nivel2
POZO_2_S3=[4,20,0,POZO_2_PRESION_1] #presion1
POZO_2_S4=[4,20,0,POZO_2_PRESION_2] #presion2

POZO_3_S1=[4,20,0,POZO_3_MEDIDA_NIVEL_1] #nivel1
POZO_3_S2=[4,20,0,POZO_3_MEDIDA_NIVEL_2] #nivel2
POZO_3_S3=[4,20,0,POZO_3_PRESION_1] #presion1
POZO_3_S4=[4,20,0,POZO_3_PRESION_2] #presion2

ESTANQUE_1_S1=[4,20,0,POZO_3_MEDIDA_NIVEL_1] #nivel1
ESTANQUE_1_S2=[4,20,0,POZO_3_MEDIDA_NIVEL_2] #nivel2
ESTANQUE_1_S3=[4,20,0,POZO_3_PRESION_1] #presion1
ESTANQUE_1_S4=[4,20,0,POZO_3_PRESION_2] #presion2


#TEMPERATURAS
UBIDOTS_TEMPERATURA_1="temperatura_1"
UBIDOTS_TEMPERATURA_2="temperatura_2"
UBIDOTS_TEMPERATURA_3="temperatura_3"

#URIS
URI_CREAR_TOKEN='https://industrial.api.ubidots.com/api/v1.6/auth/token/'
URI_DEVICE='https://industrial.api.ubidots.com/api/v1.6/devices/'




VARS_POZOS={
            UBIDOTS_POZO_1_NiVEL_1,
            UBIDOTS_POZO_1_NiVEL_2,
            UBIDOTS_POZO_1_PRESION_1,
            UBIDOTS_POZO_1_PRESION_2,
            UBIDOTS_POZO_1_CAUDAL_1,
            UBIDOTS_POZO_1_CAUDAL_2,
            UBIDOTS_POZO_2_NiVEL_1,
            UBIDOTS_POZO_2_NiVEL_2,
            UBIDOTS_POZO_2_PRESION_1,
            UBIDOTS_POZO_2_PRESION_2,
            UBIDOTS_POZO_2_CAUDAL_1,
            UBIDOTS_POZO_2_CAUDAL_2,
            UBIDOTS_POZO_3_NiVEL_1,
            UBIDOTS_POZO_3_NiVEL_2,
            UBIDOTS_POZO_3_PRESION_1,
            UBIDOTS_POZO_3_PRESION_2,
            UBIDOTS_POZO_3_CAUDAL_1,
            UBIDOTS_POZO_3_CAUDAL_2,
            }
VARS_TEMPERATURAS={
                    UBIDOTS_TEMPERATURA_1,
                    UBIDOTS_TEMPERATURA_2,
                    UBIDOTS_TEMPERATURA_3,

                    }

VARS_ESTANQUES={
                UBIDOTS_ESTANQUE_1_NiVEL_1,
                UBIDOTS_ESTANQUE_1_NiVEL_2,
                UBIDOTS_ESTANQUE_1_PRESION_1,
                UBIDOTS_ESTANQUE_1_PRESION_2,
                UBIDOTS_ESTANQUE_1_CAUDAL_1,
                UBIDOTS_ESTANQUE_1_CAUDAL_2,

                    }

VARS_DEVICES={
             UBIDOTS_POZOS,
             UBIDOTS_TEMPERATURAS,
             UBIDOTS_ESTANQUES,
             }
