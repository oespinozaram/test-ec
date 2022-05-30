# test-ec
Test de EC 



#### Sección B

- archivo test_ec.dbs (DBSchema)

  ![esquema_db](C:\Users\Usuario\Downloads\esquema_db.png)

- Desde mi prespectiva, es la primera vez que busco algo respecto a una aplicación para flotillas, no tengo mucho que agregar, 



#### Sección C

- Pruebas para Historia de usuario de suscripción 

  | Prueba                                                     | Estatus      |
  | ---------------------------------------------------------- | ------------ |
  | Crear cuenta de usuario, usando email y password           | No ejecutada |
  | Verificar cuenta de usuario vía correo electrónico         | No ejecutada |
  | Logear cuenta ya verificada                                | No ejecutada |
  | Ir a configuraciones y localizar la sección de Suscripción | No ejecutada |
  | Seleccionar tipo de suscripción                            | No Ejecutada |
  | Agregar tipo de pago Tarjeta de Crédito                    | No ejecutada |
  | Agregar tipo de pago Tarjeta de Regalo                     | No ejecutada |
  | Seleccionar periodo de suscripción (1 mes)                 | No ejecutada |
  | Guardar preferencias                                       | No ejecutada |
  | Volver a inicio y verificar estado de suscripción          | No ejecutada |



- de los Ejercicios de la Sección A

  - Con mejoras entiendo dos cosas. una mejora al código implementado o una mejora al problema planteado. respondiendo, pienso que un contador extra para el número de apariciones de cada vocal, lo digo porque me parece que puede ser un buen ejercicio para complementar 
    Para la ejercicio A2, tiene buen reto, por algo no lo terminé, creo que tiene lo que necesita.

  - Ejecutando Flake8, tenemos que:

  - C:\Source\Python\test_ec\env\Scripts/python -m flake8 --max-line-length=130 --exclude env,migrations C:\Source\Python\test_ec
    C:\Source\Python\test_ec\test_orm.py:23:1: E303 too many blank lines (3)
    C:\Source\Python\test_ec\test_orm.py:35:1: E303 too many blank lines (3)
    C:\Source\Python\test_ec\test_orm.py:53:28: E231 missing whitespace after ','

    Process finished with exit code 1

    El analizador no mostró ningún detalle para el programa del conteo de vocales, el estandar es el **PEP8**

    Las mejoras posibles, al código, sería quitar las líneas en blanco y dar el espacio después de la coma que me indica el mensaje, no tengo más propuestas, dado a que es la primera vez que uso Flake8, no conocía la herramienta.

