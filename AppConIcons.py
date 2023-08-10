# Jesús David Benavides Chicaiza
# Cristian Yamith Salazar

from PySide6.QtWidgets import (
    QWidget, 
    QLabel, 
    QLineEdit, 
    QPushButton, 
    QComboBox,
    QFileDialog,
    QStyle,
    QApplication,
    QVBoxLayout,
    QHBoxLayout, 
    QMainWindow,
    QStyleFactory,
)
from PySide6.QtGui import QPalette, QColor, QIcon, QPixmap , QRegularExpressionValidator
from PySide6.QtCore import Qt, QRegularExpression, QRect


from datetime import date, time, datetime
import sys
import os


basedir = os.path.dirname(os.path.realpath(__file__))
indice_actual = 0
empleados = []

class MainWindow(QWidget):
    def __init__(self, style_name):
        super().__init__()
        self.setFixedSize(570,625)
        ##############################################
        iconMain = QIcon("./icons/iconoVentana.png")
        self.setWindowIcon(iconMain)
        ##############################################
        self.app = QApplication.instance()
        app.setStyle(QStyleFactory.create(""))
        self.setup()

    def setup(self):
        self.setWindowTitle("App de Gestión de Empleados")

        lb_banner = QLabel(self)
        pixmap = QPixmap(os.path.join(basedir, "img", "softpro.png"))
        pixmap = pixmap.scaled(570, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    
        lb_banner.setPixmap(pixmap)
        lb_banner.setGeometry(0,10,570,100)
        lb_banner.setAlignment(Qt.AlignCenter)
        lb_banner.setScaledContents(False)
        
        # Informacion de Empleados ---------------------------------------
        
        lb_textInformation = QLabel(text="Información del Empleado: -----------------------------------------------------------------------------", parent=self)
        lb_textInformation.setGeometry(30, 110, 550, 20)
        
        # Nombre
        lb_nombre = QLabel(text="Nombre:", parent=self)
        lb_input_nombre = QLineEdit(self) # Input

        ############################################################
        lb_input_nombre.setPlaceholderText("Nombre")
        lb_input_nombre.setStyleSheet("padding-left: 5px; font-weight: bold;")
        ############################################################

        lb_nombre.setGeometry(30, 150, 520, 25)
        lb_input_nombre.setGeometry(150, 150, 200, 25)
        
        # Apellido
        lb_apellido = QLabel(text="Apellido:", parent=self)
        lb_input_apellido = QLineEdit(self) # Input
        ############################################################
        lb_input_apellido.setPlaceholderText("Apellido")
        lb_input_apellido.setStyleSheet("padding-left: 5px; font-weight: bold;")
        ############################################################
        lb_apellido.setGeometry(30, 180, 520, 25)
        lb_input_apellido.setGeometry(150, 180, 200, 25)
        
        # Genero
        lb_genero = QLabel(text="Género:", parent=self)
        lb_input_genero = QComboBox(self) # Input
        ############################################################
        lb_input_genero.addItems(["Femenino", "Masculino", "otro"])
        lb_input_genero.setStyleSheet("padding-left: 5px; QApplication {style: macintosh;}")
        ############################################################

        lb_genero.setGeometry(30, 210, 520, 25)
        lb_input_genero.setGeometry(150, 210, 200, 25)

        # Fecha de Nacimiento
        lb_fechanac = QLabel(text="Fecha de Nacimiento:", parent=self)
        lb_input_fechanac = QLineEdit(self) # Input
        ############################################################
        lb_input_fechanac.setPlaceholderText("dd/mm/aaaa")
        lb_input_fechanac.setStyleSheet("padding-left: 5px;")
        ############################################################
        lb_fechanac.setGeometry(30, 240, 200, 25)
        lb_input_fechanac.setGeometry(150, 240, 200, 25)
        
        # Fecha de Ingreso
        lb_fechaing = QLabel(text="Fecha de Ingreso:", parent=self)
        lb_input_fechaing = QLineEdit(self)
        ##########################################################
        lb_input_fechaing.setPlaceholderText("dd/mm/aaaa")
        lb_input_fechaing.setStyleSheet("padding-left: 5px;")
        ##########################################################
        lb_fechaing.setGeometry(30, 270, 200, 25)
        lb_input_fechaing.setGeometry(150, 270, 200, 25)
        
        # Salario
        lb_salario = QLabel(text="Salario:", parent=self)
        lb_input_salario = QLineEdit(parent=self)
        validator = QRegularExpressionValidator(QRegularExpression("[0-9]*"))
        lb_input_salario.setValidator(validator)
        ##########################################################
        lb_input_salario.setPlaceholderText("$ Salario")
        lb_input_salario.setStyleSheet("padding-left: 5px;")
        ##########################################################
        lb_salario.setGeometry(30, 300, 220, 25)
        lb_input_salario.setGeometry(150, 300, 200, 25)

        # ERRORES (OCASIIONALES) ---------------------------------------

        lb_error = QLabel(text="", parent=self)
        lb_error.setGeometry(30, 335, 320, 40)
        lb_error.setStyleSheet("color: red;")
        lb_error.setWordWrap(True)


        # Foto / Imagen ---------------------------------------
        
        lb_imgPerfil = QLabel(self) # Imagen
        lb_imgPerfil.setPixmap(QPixmap(os.path.join(basedir, "img", "homero.jpg")))
        lb_imgPerfil.setGeometry(380,150,150,175)
        lb_imgPerfil.setScaledContents(True)
        
        lb_rutaImg = QLineEdit(self) # Ruta de la imagen
        lb_rutaImg.setPlaceholderText("/ruta/de/la/foto")
        lb_rutaImg.setGeometry(370, 330, 170, 25)
        lb_rutaImg.returnPressed.connect(lambda: self.actualizar_imagen(lb_rutaImg, 
                                                                        lb_imgPerfil))
        ############################################################
        iconoDir = self.style().standardIcon(QStyle.SP_DirIcon)
        btn_seleccionar = QPushButton(iconoDir, "Seleccionar Imagen", self)
        ############################################################
        btn_seleccionar.setGeometry(370, 362, 170, 30)
        btn_seleccionar.clicked.connect(lambda: self.seleccionar_imagen(lb_rutaImg))

        # actualizar_imagen(self, lb_rutaImg, lb_imgPerfil):
        
        
        # Botones de Guardar, Anterior y Siguiente -------------------------------------------
        
        ############################################################
        iconoGuardar = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        lb_btn_guardar = QPushButton(iconoGuardar, " Guardar",self)
        ############################################################
        lb_btn_guardar.setGeometry(30, 400, 130, 30)
        lb_btn_guardar.clicked.connect(lambda: self.agregar_empleado(
            lb_input_nombre,
            lb_input_apellido,
            lb_input_genero,
            lb_input_fechanac,
            lb_input_fechaing,
            lb_input_salario,
            lb_rutaImg,
            lb_error,
            ))
        #############################################
        iconoAnterior = self.style().standardIcon(QStyle.SP_ArrowBack)
        lb_btn_anterior = QPushButton(iconoAnterior, " Anterior",self)
        lb_btn_anterior.setGeometry(180, 400, 170, 30)
        lb_btn_anterior.clicked.connect(lambda: self.anterior_empleado(
            lb_input_nombre,
            lb_input_apellido,
            lb_input_genero,
            lb_input_fechanac,
            lb_input_fechaing,
            lb_input_salario,
            lb_rutaImg,
            lb_error,
        ))
        
        ###############################################################################
        iconoSiguiente = self.style().standardIcon(QStyle.SP_ArrowForward)
        lb_btn_siguiente = QPushButton("Siguiente ", self)
        lb_btn_siguiente.setIcon(iconoSiguiente)
        lb_btn_siguiente.setStyleSheet("text-align: center;")  # Ajustar estilo
        ###############################################################################

        lb_btn_siguiente.setGeometry(370, 400, 170, 30)
        lb_btn_siguiente.clicked.connect(lambda: self.siguiente_empleado(
            lb_input_nombre,
            lb_input_apellido,
            lb_input_genero,
            lb_input_fechanac,
            lb_input_fechaing,
            lb_input_salario,
            lb_rutaImg,
            lb_error,
        ))
        
        layout = QVBoxLayout()

        # Calculo de Empleados ---------------------------------------
        lb_textInformation2 = QLabel(text="Cálculos de Empleado: ---------------------------------------------------------------------------------", parent=self)
        lb_textInformation2.setGeometry(30, 450, 520, 20)
        layout.setGeometry(QRect(30, 450, 520, 20))
        layout.addWidget(lb_textInformation2)
        
        # Calcular Edad
        layoutEdad = QHBoxLayout()
        ###############################################################################
        iconoEdad = QIcon("./icons/iconEdad.png")
        lb_btn_calcularEdad = QPushButton(iconoEdad, " Calcular Edad",self) # Boton
        lb_btn_calcularEdad.setStyleSheet("text-align: left; padding-left: 10px;")
        ###############################################################################
        lb_btn_calcularEdad.setGeometry(30, 490, 150, 30)  # Ajustar el tamaño del icono al botón

        lb_btn_calcularEdad.clicked.connect(lambda: self.calcular_edad(lb_input_fechanac, lb_text_calcularEdad, lb_error))
        
        lb_text_calcularEdad = QLineEdit(parent=self)
        lb_text_calcularEdad.setPlaceholderText(" ejem: 58 años")
        lb_text_calcularEdad.setReadOnly(True)
        lb_text_calcularEdad.setGeometry(200, 490, 200, 30)
        
        layoutEdad.addWidget(lb_btn_calcularEdad)
        layoutEdad.addWidget(lb_text_calcularEdad)

        # Calcular Antiguedad
        
        ###############################################################################
        iconoAntiguedad = QIcon("./icons/iconoAntiguedad.png")
        lb_btn_calcularAntiguedad = QPushButton(iconoAntiguedad, " Calcular Antigüedad",self) # Boton
        lb_btn_calcularAntiguedad.setIcon(iconoAntiguedad)
        lb_btn_calcularAntiguedad.setStyleSheet("text-align: left; padding-left: 10px;")
        ###############################################################################

        lb_text_calcularAntiguedad = QLineEdit(parent=self)
        lb_text_calcularAntiguedad.setPlaceholderText(" ejem: 30 años, 7 meses, 25 dias")
        lb_text_calcularAntiguedad.setReadOnly(True)
        lb_btn_calcularAntiguedad.setGeometry(30, 530, 150, 30)
        lb_text_calcularAntiguedad.setGeometry(200, 530, 200, 30)
        lb_btn_calcularAntiguedad.clicked.connect(lambda: self.calcular_antiguedad(lb_input_fechaing, lb_text_calcularAntiguedad, lb_error))
        
        
        # Calcular Prestaciones

        ###############################################################################
        iconoPrestaciones = QIcon("./icons/iconoPrestaciones.png")
        lb_btn_calcularPrestaciones = QPushButton(iconoPrestaciones, " Calcular Prestaciones", self) # Boton
        lb_btn_calcularPrestaciones.setIcon(iconoPrestaciones)
        lb_btn_calcularPrestaciones.setStyleSheet("text-align: left; padding-left: 10px;")
        ###############################################################################
        
        lb_text_calcularPrestaciones = QLineEdit(parent=self)
        lb_text_calcularPrestaciones.setPlaceholderText(" ejem: $ 2500000.00")
        lb_text_calcularPrestaciones.setReadOnly(True)
        lb_btn_calcularPrestaciones.setGeometry(30, 570, 150, 30)
        lb_text_calcularPrestaciones.setGeometry(200, 570, 200, 30)
        lb_btn_calcularPrestaciones.clicked.connect(lambda: self.calcular_prestaciones(
            lb_input_fechaing,
            lb_input_salario,
            lb_text_calcularPrestaciones,
            lb_error,))
        
        ##########################################################
        dark_fusion = QPalette()
        dark_fusion.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_fusion.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_fusion.setColor(QPalette.Base, QColor(255,42,0))
        dark_fusion.setColor(QPalette.WindowText, Qt.white)
        dark_fusion.setColor(QPalette.ToolTipText, Qt.black)
        dark_fusion.setColor(QPalette.Text, Qt.white)
        dark_fusion.setColor(QPalette.ButtonText, Qt.black)
        dark_fusion.setColor(QPalette.BrightText, Qt.red)
        dark_fusion.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_fusion.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
        #activamos la paleta en la aplicación
        #app.setPalette(dark_fusion)
        ##########################################################    
        
    
    # Funciones ---------------------------------------------------------------------------------
    
    
    def agregar_empleado(self, nombre, apellido, genero, fechanac, fechaing, salario, rutaImg, error):
        error.setText("")

        if  (nombre.text() or apellido.text()) == "":  # Validar que el nombre no esté vacío
            error.setText("El nombre y/o apellido no puede estar vacío.")
            return

        for empleado in empleados:
            if empleado['nombre'] == nombre.text() and empleado['apellido'] == apellido.text():
                error.setText(f"El empleado {nombre.text()} {apellido.text()} ya existe en la lista.")
                return
            
        try:
            
            salario_numero = float(salario.text())  # Convertir el salario a número
            error.setText("")
        except ValueError:
            error.setText("El salario debe ser un número válido.")
            return
            
        empleado = {
            'nombre': nombre.text(),
            'apellido': apellido.text(),
            'genero': genero.currentText(),
            'fechanac': fechanac.text(),
            'fechaing': fechaing.text(),
            'salario': salario_numero,
            'rutaImg': rutaImg.text()
        }
        empleados.append(empleado)
            
            
    def anterior_empleado(self, nombre,apellido,genero,fechanac,fechaing, salario, rutaImg, error):
        global indice_actual
        error.setText("")
        if indice_actual > 0:
            indice_actual -= 1
            empleado_actual = empleados[indice_actual]
            
            # Actualizar los QLineEdit con los datos del empleado actual
            nombre.setText(empleado_actual['nombre'])
            apellido.setText(empleado_actual['apellido'])
            genero_texto = empleado_actual['genero']
            genero_index = genero.findText(genero_texto, Qt.MatchFixedString)
            if genero_index >= 0:
                genero.setCurrentIndex(genero_index)

            fechanac.setText(empleado_actual['fechanac'])
            fechaing.setText(empleado_actual['fechaing'])
            salario.setText(str(empleado_actual['salario']))
            rutaImg.setText(empleado_actual['rutaImg'])
        else:
            error.setText("No hay empleados anteriores.")
            
    
    def siguiente_empleado(self, nombre,apellido,genero,fechanac,fechaing, salario, rutaImg, error):
        global indice_actual
        error.setText("")
        if indice_actual < len(empleados) - 1:
            indice_actual += 1
            empleado_actual = empleados[indice_actual]
            
            # Actualizar los QLineEdit con los datos del empleado actual
            nombre.setText(empleado_actual['nombre'])
            apellido.setText(empleado_actual['apellido'])

            genero_texto = empleado_actual['genero']
            genero_index = genero.findText(genero_texto, Qt.MatchFixedString)
            if genero_index >= 0:
                genero.setCurrentIndex(genero_index)

            fechanac.setText(empleado_actual['fechanac'])
            fechaing.setText(empleado_actual['fechaing'])
            salario.setText(str(empleado_actual['salario']))
            rutaImg.setText(empleado_actual['rutaImg'])
        else:
            error.setText("No hay más empleados siguientes.")
    
    def seleccionar_imagen(self, line_edit):
        opciones = QFileDialog.Options()
        opciones |= QFileDialog.ReadOnly
        opciones |= QFileDialog.DontUseNativeDialog
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif);;Todos los archivos (*)", options=opciones)
        if archivo:
            line_edit.setText(archivo)

      
    
    def extraer_año(self, fecha):
        print(fecha)
        return str(fecha)[6:]

    def extraer_mes(self, fecha):
        print(str(fecha)[3:5])
        return str(fecha)[3:5]

    def extraer_dia(self, fecha):
        print(str(fecha)[0:2])
        return str(fecha)[0:2]
    
    def year(self, fecha):
        return self.extraer_año(fecha)

    def calcular_edad(self, fechanac, res, error): # input -> text
        fecha_actual = datetime.now()
        formato_fecha = "%d/%m/%Y"
        fechanac = fechanac.text()
        try:
            fecha_nacimiento = datetime.strptime(fechanac, formato_fecha)
            edad = fecha_actual.year - fecha_nacimiento.year
            
            # Verificar si todavía no ha pasado el cumpleaños este año
            if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
                edad -= 1
                res.setText(f" {edad} años")
                error.setText("")
            
        except ValueError:
            res.setText("Fecha Invalida")
            error.setText("La fecha de nacimiento no está en el formato correcto (DD/MM/YYYY).")
            
    def calcular_antiguedad(self, fechaing, res, error):
        fecha_actual = datetime.now()
        formato_fecha = "%d/%m/%Y"
        fechaing = fechaing.text()
        try:
            fecha_ingreso = datetime.strptime(fechaing, formato_fecha)
            tiempo_transcurrido = fecha_actual - fecha_ingreso
            
            # Obtener los componentes del tiempo transcurrido
            anios = tiempo_transcurrido.days // 365
            meses = (tiempo_transcurrido.days % 365) // 30
            dias = (tiempo_transcurrido.days % 365) % 30
            
            res.setText(f"{anios} años, {meses} meses, {dias} días")
            error.setText("")    
        except ValueError:
            res.setText("Fecha de ingreso invalida")   
            error.setText("La fecha de ingreso no está en el formato correcto (DD/MM/YYYY).")

            
    
    def calcular_prestaciones(self, fechaing, salario, res, error):
        dateNow = datetime.now()
        fecha = (fechaing.text()) 
        

        try:
            salarioNumero = (salario.text())
            salarioFloat = float(salarioNumero)
            salarioInt = int(round(salarioFloat))
            
            año = int(self.extraer_año(fecha))
            mes = int(self.extraer_mes(fecha))
            dia = int(self.extraer_dia(fecha))
            
            year = int(dateNow.year)
            month = int(dateNow.month)
            day = int(dateNow.day)
            meses=mes/12
            dias=(abs(day-dia))/365
            añot=(year-año)+meses+dias
            prestaciones = (añot*salarioInt)/12
            numero_formateado = "{:.2f}".format(prestaciones)
            res.setText(f" $ {numero_formateado} ")
            error.setText("")
        except ValueError:
            res.setText("Valor no digitado | Valor Invalido")   
            error.setText("Valor Incorrecto o Invalido")

    def actualizar_imagen(self, lb_rutaImg, lb_imgPerfil):
        ruta_imagen = lb_rutaImg.text()
        pixmap = QPixmap(os.path.join(basedir, ruta_imagen))
        lb_imgPerfil.setPixmap(pixmap)


    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    styles = "Windows7"

    window = MainWindow(styles)
    window.show()

    sys.exit(app.exec())

# Fusion -> Styles
# Palette -> Palette
# Icons -> Icons