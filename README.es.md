# Cuestionario Interactivo con Tkinter
Este proyecto es una aplicación de escritorio desarrollada en Python utilizando la biblioteca Tkinter. Este programa presenta una serie de preguntas a los usuarios y les permite seleccionar la respuesta correcta. Los usuarios también tienen la opción de personalizar las preguntas, las opciones de respuesta y las imágenes utilizadas en el cuestionario.

## Uso
- Ejecute el código Python en un entorno de desarrollo compatible.

- Aparecerá una ventana principal titulada "Cuestionario" con un mensaje de bienvenida.

- Haga clic en el botón "Empecemos!" para iniciar el cuestionario.

- Se abrirá una nueva ventana con la primera pregunta y las opciones de respuesta.

- Seleccione la opción de respuesta que considere correcta haciendo clic en el botón correspondiente.

- Si la respuesta es correcta, se mostrará un mensaje informativo. De lo contrario, se mostrará un mensaje de error.

- Haga clic en el botón "Siguiente" para avanzar a la siguiente pregunta.

- El proceso de presentación de preguntas, selección de respuestas y avance continúa hasta que se haya completado el cuestionario.

- Cuando se haya respondido la última pregunta, se cerrarán las ventanas del cuestionario y la ventana principal.

## Personalización
- Para personalizar las preguntas, las opciones de respuesta y las imágenes utilizadas en el cuestionario, puede modificar las listas en el código.

- Las preguntas se almacenan en la lista "questions". Puede cambiar el texto de las preguntas agregando o modificando elementos de esta lista.

- Las opciones de respuesta se almacenan en las listas "answer1", "answer2" y "answer3". Puede cambiar el texto de las opciones de respuesta agregando o modificando elementos de estas listas.

- Las imágenes utilizadas en el cuestionario se almacenan en la lista "questions_images". Puede reemplazar las imágenes existentes con sus propias imágenes agregando o modificando elementos de esta lista. Asegúrese de que las imágenes estén ubicadas en la carpeta "images" o especifique la ruta de la carpeta de imágenes según sea necesario.

- Por defecto, la respuesta correcta se considera como la segunda opción de respuesta. Si desea cambiar la respuesta correcta a otra opción, puede modificar el código para reflejar su preferencia.

## Requisitos del sistema
- Python 3.x
- Biblioteca Tkinter
- Biblioteca PIL (Python Imaging Library)
