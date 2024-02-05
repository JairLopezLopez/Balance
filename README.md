Como ejecutar el codigo balance

1- En la funcion "send_email" se deben llenar los parametros para que se envie el mensaje:

    smtp_server = 'Your server'                           //// En esta seccion se pondra el servidor de preferencia para enviar el email
        smtp_port = 587                                   /// Se selecciona por que puerto se requiere enviar el email
        sender_email = 'your email'                       /// Se coloca el email el cual sera el emisor del mensaje
        sender_password = 'your password'                 /// Se coloca la contraseña del email para ser usado (esta contraseña debe de ser de las generadas para ser usadas por aplicaciones, no es la contraseña del usuario)
        receiver_email = 'receiving email'                /// Se coloca el email que recibira el mensaje


En la seccion de la linea 61 del codigo se puede colocar el mensaje que querramos que nuestro correo lleve como titulo:

    message['Subject'] = 'Resumen de transacciones'         // Presisamente en esta sección se coloca, por defecto esta como "Resumen de transacciones"

Por ultimo se debe de indicar la ruta en la cual se encuentra el archivo, esto se hace indicando la ruta en la linea 74 del código:

    file_path = 'Your CSV file'                  /// Precisamente en esta seccion

Una vez se hayan llenado estos campos se puede proceder a ejecutar el código en el IDE o editor de texto de preferencia.
