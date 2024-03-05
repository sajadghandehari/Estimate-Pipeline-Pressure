from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
import turtle
import math
from sympy import symbols, solve

pipeline_length = ''
injection_points = 1
delivery_points = 1
nominal_pipe_size = ''
wall_thickness = ''
pipeline_propertice = {}

class Ui_Page1(object):

    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(600, 350)
        Form.setWindowIcon(QIcon('icon/python.png'))
        self.textBrowser = QtWidgets.QTextBrowser(self.Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 310, 600, 40))
        self.textBrowser.setStyleSheet("background-color: rgb(234, 234, 234);\n"
        "background-color: rgb(218, 218, 218);")
        self.textBrowser.setObjectName("textBrowser")
        
        self.lable()
        self.line_edit()
        self.button()
        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

    def next(self):
        global pipeline_length, injection_points, delivery_points, nominal_pipe_size, wall_thickness, pipeline_propertice
        
        pipeline_length = float(self.length_lineEdit.text())
        pipeline_propertice ['pipeline length'] = pipeline_length 
        injection_points = int(self.injection_lineEdit.text())
        delivery_points = int(self.deliveries_lineEdit.text())
        nominal_pipe_size = float(self.nominal_pipe_size_lineEdit.text())
        pipeline_propertice ['nominal pipe size'] = nominal_pipe_size 
        wall_thickness = float(self.wall_thickness_lineEdit.text())
        pipeline_propertice ['wall thickness'] = wall_thickness

        self.window_3 = QtWidgets.QMainWindow()
        self.ui = Ui_Page2()
        self.ui.setupUi(self.window_3)
        self.Form.hide()
        self.window_3.show()

    def lable(self):
        self.Pic_label = QtWidgets.QLabel(self.Form)
        self.Pic_label.setGeometry(QtCore.QRect(0, 0, 200, 310))
        self.Pic_label.setStyleSheet("background-image: url(icon/oil-and-gas.jpg);")
        self.Pic_label.setText("")
        self.Pic_label.setPixmap(QtGui.QPixmap("icon/oil-and-gas.jpg"))
        self.Pic_label.setScaledContents(True)
        self.Pic_label.setObjectName("label")

        self.pipeline_length_label = QtWidgets.QLabel(self.Form)
        self.pipeline_length_label.setGeometry(QtCore.QRect(215, 120, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pipeline_length_label.setFont(font)
        self.pipeline_length_label.setObjectName("label_2")

        self.nominal_pipe_size_label = QtWidgets.QLabel(self.Form)
        self.nominal_pipe_size_label.setGeometry(QtCore.QRect(215, 155, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nominal_pipe_size_label.setFont(font)
        self.nominal_pipe_size_label.setObjectName("label_3")

        self.wall_thickness_label = QtWidgets.QLabel(self.Form)
        self.wall_thickness_label.setGeometry(QtCore.QRect(215, 190, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wall_thickness_label.setFont(font)
        self.wall_thickness_label.setObjectName("label_3")        

        self.deliveries_label = QtWidgets.QLabel(self.Form)
        self.deliveries_label.setGeometry(QtCore.QRect(215, 225, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deliveries_label.setFont(font)
        self.deliveries_label.setObjectName("label_3")

        self.injection_label = QtWidgets.QLabel(self.Form)
        self.injection_label.setGeometry(QtCore.QRect(215, 260, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.injection_label.setFont(font)
        self.injection_label.setObjectName("label_6")

        self.discription_label = QtWidgets.QLabel(self.Form)
        self.discription_label.setGeometry(QtCore.QRect(210, -10, 361, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.discription_label.setFont(font)
        self.discription_label.setObjectName("label_4")

    def line_edit(self):
        self.length_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.length_lineEdit.setGeometry(QtCore.QRect(500, 120, 80, 20))
        self.length_lineEdit.setObjectName("lineEdit")
    
        self.nominal_pipe_size_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.nominal_pipe_size_lineEdit.setGeometry(QtCore.QRect(500, 155, 80, 20))
        self.nominal_pipe_size_lineEdit.setObjectName("lineEdit_2")

        self.wall_thickness_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.wall_thickness_lineEdit.setGeometry(QtCore.QRect(500, 190, 80, 20))
        self.wall_thickness_lineEdit.setObjectName("lineEdit_2")

        self.deliveries_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.deliveries_lineEdit.setGeometry(QtCore.QRect(500, 225, 80, 20))
        self.deliveries_lineEdit.setObjectName("lineEdit_2")

        self.injection_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.injection_lineEdit.setGeometry(QtCore.QRect(500, 260, 80, 20))
        self.injection_lineEdit.setObjectName("lineEdit_4")
        self.injection_lineEdit.returnPressed.connect(lambda: self.next())

    def button(self):
        self.Next_pushButton = QtWidgets.QPushButton(self.Form)
        self.Next_pushButton.setGeometry(QtCore.QRect(500, 320, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Next_pushButton.setFont(font)
        self.Next_pushButton.setObjectName("pushButton_2")
        self.Next_pushButton.clicked.connect(self.next)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Estimate pipeline pressure "))
        self.pipeline_length_label.setText(_translate("Form", "Your pipe line length :"))
        self.nominal_pipe_size_label.setText(_translate("Form", "nominal pipe size :"))
        self.wall_thickness_label.setText(_translate("Form", "wall thickness :"))

        self.deliveries_label.setText(_translate("Form", "Number of deliveries points in your pipe line :"))
        self.injection_label.setText(_translate("Form", "Number of Injection points in your pipe line :"))
        self.discription_label.setText(_translate("Form", "This aplication is made for claculaate pressure requaire\n\
along pipeline at several point of pipeline.\n\
This aplication can claculate required diameter for \n\
transmition in the Specified pressure."))
        self.Next_pushButton.setText(_translate("Form", "Next"))


class Ui_Page2(object):
    injections_dic = {}
    deliverely_dic = {}
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(600, 350)
        Form.setWindowIcon(QIcon('icon/python.png'))
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 310, 600, 40))
        self.textBrowser.setStyleSheet("background-color: rgb(234, 234, 234);\n"
"background-color: rgb(218, 218, 218);")
        self.textBrowser.setObjectName("textBrowser")

        self.lable()
        self.line_edit()
        self.button()
       
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def lable(self):
        self.pic_label = QtWidgets.QLabel(self.Form)
        self.pic_label.setGeometry(QtCore.QRect(0, 0, 200, 310))
        self.pic_label.setStyleSheet("background-image: url(icon/oil-and-gas.jpg);")
        self.pic_label.setText("")
        self.pic_label.setPixmap(QtGui.QPixmap("icon/oil-and-gas.jpg"))
        self.pic_label.setScaledContents(True)
        self.pic_label.setObjectName("label")

        self.deliveries_label = QtWidgets.QLabel(self.Form)
        self.deliveries_label.setGeometry(QtCore.QRect(215, 195, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deliveries_label.setFont(font)
        self.deliveries_label.setObjectName("label_2")

        self.deliveries_name_label = QtWidgets.QLabel(self.Form)
        self.deliveries_name_label.setGeometry(QtCore.QRect(215, 160, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deliveries_name_label.setFont(font)
        self.deliveries_name_label.setObjectName("label_3")
        
        self.injection_name_label = QtWidgets.QLabel(self.Form)
        self.injection_name_label.setGeometry(QtCore.QRect(215, 230, 250, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.injection_name_label.setFont(font)
        self.injection_name_label.setObjectName("label_6")

        self.discription_label = QtWidgets.QLabel(self.Form)
        self.discription_label.setGeometry(QtCore.QRect(210, -5, 380, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.discription_label.setFont(font)
        self.discription_label.setObjectName("label_4")

        self.message_label = QtWidgets.QLabel(self.Form)
        self.message_label.setGeometry(QtCore.QRect(215, 265, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.message_label.setFont(font)
        self.message_label.setObjectName("label_7")
        self.message_label.setStyleSheet("color: green;")

    def line_edit(self):

        self.comboBox_branch_type = QtWidgets.QComboBox(self.Form)
        self.comboBox_branch_type.setGeometry(QtCore.QRect(450, 160, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_branch_type.setFont(font) 
        self.comboBox_branch_type.setObjectName("comboBox")
        matter_list_by_SimulationName = ['Deliverie','Injection']
        self.comboBox_branch_type.addItems(matter_list_by_SimulationName)
        self.comboBox_branch_type.activated.connect(self.set_text)

        self.name_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.name_lineEdit.setGeometry(QtCore.QRect(450, 195, 80, 20))
        self.name_lineEdit.setObjectName("injection_name_lineEdit")
        self.name_lineEdit.returnPressed.connect(lambda: self.add())

        self.dictance_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.dictance_lineEdit.setGeometry(QtCore.QRect(450, 230, 80, 20))
        self.dictance_lineEdit.setObjectName("deliveries_dictance_lineEdit")
        self.dictance_lineEdit.returnPressed.connect(lambda: self.add())

    def button(self):
        self.next_pushButton = QtWidgets.QPushButton(self.Form)
        self.next_pushButton.setGeometry(QtCore.QRect(500, 320, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setObjectName("Next_pushButton")
        self.next_pushButton.clicked.connect(self.next)

        self.draw_pushButton = QtWidgets.QPushButton(self.Form)
        self.draw_pushButton.setGeometry(QtCore.QRect(300, 320, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.draw_pushButton.setFont(font)
        self.draw_pushButton.setObjectName("draw_pushButton")
        self.draw_pushButton.clicked.connect(self.figure)

        self.back_pushButton = QtWidgets.QPushButton(self.Form)
        self.back_pushButton.setGeometry(QtCore.QRect(400, 320, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.back_pushButton.setFont(font)
        self.back_pushButton.setObjectName("back_pushButton")
        self.back_pushButton.clicked.connect(self.back)

    def back(self):
        self.window_3 = QtWidgets.QMainWindow()
        self.ui = Ui_Page1()
        self.ui.setupUi(self.window_3)
        self.Form.hide()
        self.window_3.show()   

    def figure(self):
        injections_dic = self.injections_dic
        deliverely_dic = self.deliverely_dic

        ws=turtle.Screen()
        ws.setup(600, 350)
        turtle.TurtleScreen._RUNNING=True
        t=turtle.Turtle()
        t.color("teal")
        t.width("14")
        t.speed(100)
        t.shapesize(1.5)

        pipeline_length = 150

        def main_line(length ,color):
            t.color(f"{color}")
            t.width(f"{length}")
            t.hideturtle()           
            t.penup()              
            t.goto(-250, 0)     
            t.showturtle()          
            t.pendown()              
            t.forward(500) 
        
        def resize(length ,color ,Arrows ,branch_name ,position ,liquid):
            resize = (length * 500) / pipeline_length
            draw(resize, color, Arrows ,branch_name ,position ,liquid)

        def draw(length ,color ,Arrows ,branch_name, position ,liquid):

            if length >= 250 :
                t.color(color)
                length = length - 250
                t.hideturtle()           
                t.penup()              
                if position =='delivery':    
                    t.goto(length - 5, 5)  
                    t.write(f'{branch}',font =("Arial Narrow", 14, "bold")) 
                    t.goto(length, 0) 
                    t.showturtle()          
                    t.pendown() 
                    t.right(90)
                if position =='injection':    
                    t.goto(length - 5, -35)  
                    t.write(f'{branch}',font =("Arial Narrow", 14, "bold")) 
                    t.goto(length, 0) 
                    t.showturtle()          
                    t.pendown() 
                    t.left(90)
                t.forward(100)


                if Arrows == True and liquid == False:
                    if position =='delivery':          
                        t.width("3")
                        t.color("red")
                        t.hideturtle()           
                        t.penup()
                        t.goto(length, -150)
                        t.showturtle()          
                        t.pendown() 
                        t.right(180)
                        t.forward(30)
                        t.stamp()
                        t.right(180)
                        t.left(90)
                        t.width("14")
                        t.color(color)
                    if position =='injection':  
                        t.width("3")
                        t.color("red")
                        t.hideturtle()           
                        t.penup()
                        t.goto(length, 120)
                        t.showturtle()          
                        t.pendown() 
                        t.forward(30)
                        t.stamp()
                        t.right(90)
                        t.width("14")
                        t.color(color)
                else:
                    if position =='delivery':          
                        t.left(90)
                    if position =='injection':          
                        t.right(90)
                
            else:
                if position =='delivery': 
                    t.color(color)
                    length = length - 250
                    t.hideturtle()           
                    t.penup()              
                    t.goto(length - 5, 5)  
                    t.write(f'{branch_name}',font =("Arial Narrow", 14, "bold")) 
                    t.goto(length, 0)  
                    t.showturtle()          
                    t.pendown()              
                    t.right(90)
                    t.forward(100)
                    t.left(90)
                if position =='injection': 
                    t.color(color)
                    length = length - 250
                    t.hideturtle()           
                    t.penup()              
                    t.goto(length - 5, -35)  
                    t.write(f'{branch_name}',font =("Arial Narrow", 14, "bold")) 
                    t.goto(length, 0)  
                    t.showturtle()          
                    t.pendown()              
                    t.left(90)
                    t.forward(100)
                    t.right(90)
                if Arrows == True and liquid == False:
                    if position =='delivery':          
                        t.width("3")
                        t.color("red")
                        t.hideturtle()           
                        t.penup()
                        t.goto(length, -150)
                        t.showturtle()          
                        t.pendown() 
                        t.left(90)
                        t.forward(30)
                        t.stamp()
                        t.right(90)
                        t.width("14")
                        t.color(color)
                    if position =='injection':  
                        t.width("3")
                        t.color("red")
                        t.hideturtle()           
                        t.penup()
                        t.goto(length, 120)
                        t.showturtle()          
                        t.pendown() 
                        t.left(90)
                        t.forward(30)
                        t.stamp()
                        t.right(90)
                        t.width("14")
                        t.color(color)


        color ="teal"
        main_line(12, color)
        position = 'delivery'
        for branch in deliverely_dic:
            resize_branch = resize(deliverely_dic[branch] ,color ,True ,branch ,position ,False)
        position = 'injection'
        for branch in injections_dic:
            print(branch)
            resize_branch = resize(injections_dic[branch] ,color ,True ,branch ,position , False)

        color = "red"
        t.color(color)  
        t.speed(5)
        main_line(3, color)
        t.speed(5)
        position = 'delivery'
        for branch in deliverely_dic:
            t.width("3")
            resize_branch = resize(deliverely_dic[branch] ,color ,True ,branch ,position ,True)

        position = 'injection'
        t.speed(5)
        for branch in injections_dic:
            t.width("3")
            resize_branch = resize(injections_dic[branch] ,color ,True ,branch ,position , True)


        t.hideturtle()
        # turtle.getscreen()._root.mainloop()
        ws.exitonclick()
        print("OK")

    def next(self):
        self.window_3 = QtWidgets.QMainWindow()
        self.ui = Ui_Page3()
        self.ui.setupUi(self.window_3)
        self.Form.hide()
        self.window_3.show()

    def add(self):
        global pipeline_length, injection_points, delivery_points

        branch_type = self.comboBox_branch_type.currentText()
        
        
        # self.lable_result.setText(f'composition {self.count} added successfully!')

        if len(self.deliverely_dic) < delivery_points :
            if branch_type == 'Deliverie':
                deliveries_name = self.name_lineEdit.text()
                deliveries_dictance = self.dictance_lineEdit.text()
                if deliveries_dictance.replace('.','').isdigit() == True:
                    self.deliverely_dic [deliveries_name] = float(deliveries_dictance)
                    self.message_label.setText(f'{branch_type} branch with name {self.name_lineEdit.text()}\
 and distanse {self.dictance_lineEdit.text()} added \nsuccessfuly!')
        if len(self.injections_dic) < injection_points :
            if branch_type == 'Injection':
                injections_name = self.name_lineEdit.text()
                injections_dictance = self.dictance_lineEdit.text()
                if injections_dictance.replace('.','').isdigit() == True:
                    self.injections_dic [injections_name] = float(injections_dictance)
                    self.message_label.setText(f'{branch_type} branch with name {self.name_lineEdit.text()}\
 and distanse {self.dictance_lineEdit.text()} added \nsuccessfuly!')

        print(self.injections_dic)
        print(self.deliverely_dic)

    def set_text(self):
        branch_type = self.comboBox_branch_type.currentText()
        _translate = QtCore.QCoreApplication.translate
        self.deliveries_label.setText(_translate("Form", f"{branch_type} point name :"))
        self.injection_name_label.setText(_translate("Form", f"{branch_type} point distance from origin :"))

    def retranslateUi(self, Form):
        branch_type = self.comboBox_branch_type.currentText()
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Estimate pipeline pressure "))

        self.deliveries_name_label.setText(_translate("Form", "select branch type :"))
        self.deliveries_label.setText(_translate("Form", f"{branch_type} point name :"))
        self.injection_name_label.setText(_translate("Form", f"{branch_type} point distance from origin :"))
        # self.injection_distance_label.setText(_translate("Form", "Injection point distance from origin :"))

        self.discription_label.setText(_translate("Form", "in this part you must specify 2 delivery point and 3 \n\
injection point.\n\
when you enter points successfully Draw button will \n\
active and you can seen your pipeline figure."))
        self.next_pushButton.setText(_translate("Form", "Next"))
        self.draw_pushButton.setText(_translate("Form", "Figure"))
        self.back_pushButton.setText(_translate("Form", "Back"))


class Ui_Page3(object):

    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(600, 350)
        Form.setWindowIcon(QIcon('icon/python.png'))
        self.textBrowser = QtWidgets.QTextBrowser(self.Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 310, 600, 40))
        self.textBrowser.setStyleSheet("background-color: rgb(234, 234, 234);\n"
        "background-color: rgb(218, 218, 218);")
        self.textBrowser.setObjectName("textBrowser")
        
        self.lable()
        self.line_edit()
        self.button()
        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

    def next(self):
        global pipeline_length, injection_points, delivery_points ,pipeline_propertice
        specific_gravity = float(self.specific_gravity_lineEdit.text())
        pipeline_propertice ['specific gravity'] = specific_gravity
        viscosity = float(self.viscosity_lineEdit.text())
        pipeline_propertice ['viscosity'] = viscosity
        absolute_roughness = float(self.absolute_roughness_lineEdit.text())
        pipeline_propertice ['absolute roughness'] = absolute_roughness
        compressibility_factor = float(self.compressibility_factor_lineEdit.text())
        pipeline_propertice ['compressibility factor'] = compressibility_factor
        idrag_factor = float(self.idrag_factor_lineEdit.text())
        pipeline_propertice ['drag factor'] = idrag_factor
 
        self.window_3 = QtWidgets.QMainWindow()
        self.ui = Ui_Page4()
        self.ui.setupUi(self.window_3)
        self.Form.hide()
        self.window_3.show()

    def back(self):
        self.window_3 = QtWidgets.QMainWindow()
        self.ui = Ui_Page2()
        self.ui.setupUi(self.window_3)
        self.Form.hide()
        self.window_3.show()   

    def lable(self):
        self.Pic_label = QtWidgets.QLabel(self.Form)
        self.Pic_label.setGeometry(QtCore.QRect(0, 0, 200, 310))
        self.Pic_label.setStyleSheet("background-image: url(icon/oil-and-gas.jpg);")
        self.Pic_label.setText("")
        self.Pic_label.setPixmap(QtGui.QPixmap("icon/oil-and-gas.jpg"))
        self.Pic_label.setScaledContents(True)
        self.Pic_label.setObjectName("label")

        self.specific_gravity_label = QtWidgets.QLabel(self.Form)
        self.specific_gravity_label.setGeometry(QtCore.QRect(215, 120, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.specific_gravity_label.setFont(font)
        self.specific_gravity_label.setObjectName("label_2")

        self.viscosity_label = QtWidgets.QLabel(self.Form)
        self.viscosity_label.setGeometry(QtCore.QRect(215, 155, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.viscosity_label.setFont(font)
        self.viscosity_label.setObjectName("label_3")

        self.absolute_roughness_label = QtWidgets.QLabel(self.Form)
        self.absolute_roughness_label.setGeometry(QtCore.QRect(215, 190, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.absolute_roughness_label.setFont(font)
        self.absolute_roughness_label.setObjectName("label_3")        

        self.compressibility_factor_label = QtWidgets.QLabel(self.Form)
        self.compressibility_factor_label.setGeometry(QtCore.QRect(215, 225, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.compressibility_factor_label.setFont(font)
        self.compressibility_factor_label.setObjectName("label_3")

        self. drag_factor_label = QtWidgets.QLabel(self.Form)
        self.drag_factor_label.setGeometry(QtCore.QRect(215, 260, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.drag_factor_label.setFont(font)
        self.drag_factor_label.setObjectName("label_6")

        self.discription_label = QtWidgets.QLabel(self.Form)
        self.discription_label.setGeometry(QtCore.QRect(210, -10, 361, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.discription_label.setFont(font)
        self.discription_label.setObjectName("label_4")

    def line_edit(self):
        self.specific_gravity_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.specific_gravity_lineEdit.setGeometry(QtCore.QRect(350, 120, 80, 20))
        self.specific_gravity_lineEdit.setObjectName("lineEdit")
    
        self.viscosity_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.viscosity_lineEdit.setGeometry(QtCore.QRect(350, 155, 80, 20))
        self.viscosity_lineEdit.setObjectName("lineEdit_2")

        self.absolute_roughness_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.absolute_roughness_lineEdit.setGeometry(QtCore.QRect(350, 190, 80, 20))
        self.absolute_roughness_lineEdit.setObjectName("lineEdit_2")

        self.compressibility_factor_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.compressibility_factor_lineEdit.setGeometry(QtCore.QRect(350, 225, 80, 20))
        self.compressibility_factor_lineEdit.setObjectName("lineEdit_2")

        self.idrag_factor_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.idrag_factor_lineEdit.setGeometry(QtCore.QRect(350, 260, 80, 20))
        self.idrag_factor_lineEdit.setObjectName("lineEdit_4")
        self.idrag_factor_lineEdit.returnPressed.connect(lambda: self.next())

    def button(self):
        self.Next_pushButton = QtWidgets.QPushButton(self.Form)
        self.Next_pushButton.setGeometry(QtCore.QRect(500, 320, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Next_pushButton.setFont(font)
        self.Next_pushButton.setObjectName("pushButton_2")
        self.Next_pushButton.clicked.connect(self.next)

        self.back_pushButton = QtWidgets.QPushButton(self.Form)
        self.back_pushButton.setGeometry(QtCore.QRect(400, 320, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.back_pushButton.setFont(font)
        self.back_pushButton.setObjectName("back_pushButton")
        self.back_pushButton.clicked.connect(self.back)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Estimate pipeline pressure "))
        self.specific_gravity_label.setText(_translate("Form", "specific gravity :"))
        self.viscosity_label.setText(_translate("Form", "viscosity :"))
        self.absolute_roughness_label.setText(_translate("Form", "absolute roughness :"))

        self.compressibility_factor_label.setText(_translate("Form", "compressibility factor :"))
        self.drag_factor_label.setText(_translate("Form", "drag factor :"))
        self.discription_label.setText(_translate("Form", "In this page you have to enter the characteristics of\n\
the fluid flowing in the pipeline.\n\n"))
        self.Next_pushButton.setText(_translate("Form", "Next"))
        self.back_pushButton.setText(_translate("Form", "Back"))


class Ui_Page4(object):

    volume_point = {}
    reynolds_taransmition_factor = {}
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(600, 350)
        Form.setWindowIcon(QIcon('icon/python.png'))
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 310, 600, 40))
        self.textBrowser.setStyleSheet("background-color: rgb(234, 234, 234);\n"
"background-color: rgb(218, 218, 218);")
        self.textBrowser.setObjectName("textBrowser")
        self.point_name = ['inlet vol']
        for val in Ui_Page2.injections_dic :
            self.point_name.append(val)
        for val in Ui_Page2.deliverely_dic :
            self.point_name.append(val)

        self.lable()
        self.line_edit()
        self.button()
       
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def lable(self):
        self.pic_label = QtWidgets.QLabel(self.Form)
        self.pic_label.setGeometry(QtCore.QRect(0, 0, 200, 310))
        self.pic_label.setStyleSheet("background-image: url(icon/oil-and-gas.jpg);")
        self.pic_labelic_label.setText("")
        self.pic_labelic_label.setPixmap(QtGui.QPixmap("icon/oil-and-gas.jpg"))
        self.pic_label.setScaledContents(True)
        self.pic_label.setObjectName("label")

        self.base_pressure_label = QtWidgets.QLabel(self.Form)
        self.base_pressure_label.setGeometry(QtCore.QRect(215, 195, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.base_pressure_label.setFont(font)
        self.base_pressure_label.setObjectName("label_2")

        self. inlet_volume_label = QtWidgets.QLabel(self.Form)
        self.inlet_volume_label.setGeometry(QtCore.QRect(215, 160, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inlet_volume_label.setFont(font)
        self.inlet_volume_label.setObjectName("label_3")
        
        self.base_temperature_label = QtWidgets.QLabel(self.Form)
        self.base_temperature_label.setGeometry(QtCore.QRect(215, 230, 250, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.base_temperature_label.setFont(font)
        self.base_temperature_label.setObjectName("label_6")

        self.discription_label = QtWidgets.QLabel(self.Form)
        self.discription_label.setGeometry(QtCore.QRect(210, -5, 380, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.discription_label.setFont(font)
        self.discription_label.setObjectName("label_4")

    def line_edit(self):

        self.comboBox_branch_name = QtWidgets.QComboBox(self.Form)
        self.comboBox_branch_name.setGeometry(QtCore.QRect(460, 160, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_branch_name.setFont(font) 
        self.comboBox_branch_name.setObjectName("comboBox")
        self.comboBox_branch_name.addItems(self.point_name)
        self.comboBox_branch_name.activated.connect(self.add)

        self.inlet_volume_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.inlet_volume_lineEdit.setGeometry(QtCore.QRect(530, 160, 60, 20))
        self.inlet_volume_lineEdit.setObjectName("deliveries_dictance_lineEdit")
        self.inlet_volume_lineEdit.returnPressed.connect(lambda: self.add())

        self.base_pressure_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.base_pressure_lineEdit.setGeometry(QtCore.QRect(460, 195, 80, 20))
        self.base_pressure_lineEdit.setObjectName("deliveries_dictance_lineEdit")
        self.base_pressure_lineEdit.returnPressed.connect(lambda: self.add())

        self.base_temperature_lineEdit = QtWidgets.QLineEdit(self.Form)
        self.base_temperature_lineEdit.setGeometry(QtCore.QRect(460, 230, 80, 20))
        self.base_temperature_lineEdit.setObjectName("injection_name_lineEdit")
        self.base_temperature_lineEdit.returnPressed.connect(lambda: self.add())

    def button(self):
        self.next_pushButton = QtWidgets.QPushButton(self.Form)
        self.next_pushButton.setGeometry(QtCore.QRect(500, 320, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.next_pushButton.setFont(font)
        self.next_pushButton.setObjectName("Next_pushButton")
        self.next_pushButton.clicked.connect(self.calculate)

        self.draw_pushButton = QtWidgets.QPushButton(self.Form)
        self.draw_pushButton.setGeometry(QtCore.QRect(300, 320, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.draw_pushButton.setFont(font)
        self.draw_pushButton.setObjectName("draw_pushButton")
        self.draw_pushButton.clicked.connect(self.figure)

        self.back_pushButton = QtWidgets.QPushButton(self.Form)
        self.back_pushButton.setGeometry(QtCore.QRect(400, 320, 90, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.back_pushButton.setFont(font)
        self.back_pushButton.setObjectName("back_pushButton")
        self.back_pushButton.clicked.connect(self.back)

    def back(self):
        self.window_3 = QtWidgets.QMainWindow()
        self.ui = Ui_Page3()
        self.ui.setupUi(self.window_3)
        self.Form.hide()
        self.window_3.show()   

    def figure(self):
        global pipeline_propertice
        # injections_dic = Ui_Page2.injections_dic
        # deliverely_dic = Ui_Page2.deliverely_dic
        # volume_point = self.volume_point
        injections_dic = {'E' : 100}
        deliverely_dic = {'B' : 20, 'C' : 80}
        volume_point = {'inlet vol' : 250 , 'B' : 50, 'C' : 70, 'E' : 60}
        pipeline_propertice ={'pipeline length': 150.0, 'nominal pipe size': 20, 'wall thickness': 0.5, 'specific gravity': 0.65, 'viscosity': 8, 'absolute roughness': 150, 'compressibility factor': 0.85, 'drag factor': 0.96}

        # self.branch_pressure = {'E': 587.09, 'C': 625.03, 'B': 846.92, 'inlet': 942.01}
        self.branch_pressure = dict(reversed(list(self.branch_pressure.items())))
        self.branch_pressure.update(self.reynolds_taransmition_factor)

        ws=turtle.Screen()
        ws.setup(1090, 600)
        turtle.TurtleScreen._RUNNING=True
        t=turtle.Turtle()
        t.color("teal")
        t.width("14")
        t.speed(10)
        t.shapesize(1.5)

        pipeline_length = 150

        def main_line(length ,color):
            t.color(f"{color}")
            t.width(f"{length}")
            t.hideturtle()           
            t.penup()         
            if color == 'red':
                t.goto(-330, -30)
                t.write(f'{volume_point["inlet vol"]} \nMMSCFD',font =("Arial Narrow", 9, "bold"))  
                t.goto(-300, 0)
                t.showturtle()
                t.pendown()
                t.forward(40)
                t.stamp()
                t.hideturtle()           
                t.penup()    
            t.goto(-250, 0)     
            t.showturtle()          
            t.pendown()              
            t.forward(500) 
        
        def resize(length ,color ,Arrows ,branch_name ,position ,liquid):
            resize = (length * 500) / pipeline_length
            draw(resize, color, Arrows ,branch_name ,position ,liquid)

        def draw(length ,color ,Arrows ,branch_name, position ,liquid):

            if length >= 250 :
                t.color(color)
                length = length - 250
                t.hideturtle()           
                t.penup()      
                t.speed(3)        
                if position =='delivery':    
                    if liquid == False:
                        t.goto(length, -100)  
                        t.showturtle()          
                        t.pendown()              
                        t.left(90)
                        t.forward(100)
                        t.right(180)
                    else:
                        t.goto(length, 0)  
                        t.showturtle()          
                        t.pendown()              
                        t.right(90)
                        t.forward(100)
                if position =='injection':    
                    t.goto(length - 5, -35)  
                    t.write(f'{branch_name}',font =("Arial Narrow", 14, "bold")) 
                    t.goto(length, 0) 
                    t.showturtle()          
                    t.pendown() 
                    t.left(90)
                    t.forward(100)


                if Arrows == True and liquid == False:
                    if position =='delivery':          
                        t.width("3")
                        t.color("red")
                        t.hideturtle()           
                        t.penup()
                        t.goto(length-30, -180)
                        t.write(f'{volume_point[branch_name]} \nMMSCFD',font =("Arial Narrow", 9, "bold")) 
                        t.goto(length, -150)
                        t.showturtle()          
                        t.pendown() 
                        t.right(180)
                        t.forward(30)
                        t.stamp()
                        t.right(180)
                        t.left(90)
                        t.width("14")
                        t.color(color)
                    if position =='injection':  
                        t.width("3")
                        t.color("red")
                        t.hideturtle()           
                        t.penup()
                        t.goto(length - 30 , 150)
                        t.write(f'{volume_point[branch_name]} \nMMSCFD',font =("Arial Narrow", 9, "bold")) 
                        t.goto(length, 120)
                        t.showturtle()          
                        t.pendown() 
                        t.forward(30)
                        t.stamp()
                        t.right(90)
                        t.width("14")
                        t.color(color)
                else:
                    if position =='delivery':  
                        if liquid == False:
                            t.left(90)
                        else:
                            t.left(90)
                    if position =='injection':          
                        t.right(90)
                
            else:
                if position =='delivery': 
                    t.color(color)
                    length = length - 250
                    t.hideturtle()           
                    t.penup()              
                    t.goto(length - 5, 5)  
                    t.write(f'{branch_name}',font =("Arial Narrow", 14, "bold")) 
                    if liquid == False:
                        t.goto(length, -100)  
                        t.showturtle()          
                        t.pendown()              
                        t.right(-90)
                        t.forward(100)
                        t.left(-90)
                    else:
                        t.goto(length, 0)  
                        t.showturtle()          
                        t.pendown()              
                        t.right(90)
                        t.forward(100)
                        t.left(90)
                if position =='injection': 
                    t.color(color)
                    length = length - 250
                    t.hideturtle()           
                    t.penup()              
                    t.goto(length - 5, -35)  
                    t.write(f'{branch_name}',font =("Arial Narrow", 14, "bold")) 
                    t.goto(length, 0)  
                    t.showturtle()          
                    t.pendown()              
                    t.left(90)
                    t.forward(100)
                    t.right(90)
                if Arrows == True and liquid == False:
                    if position =='delivery':          
                        t.width("3")
                        t.color("red")
                        t.hideturtle()           
                        t.penup()
                        t.goto(length-30, -180)
                        t.write(f'{volume_point[branch_name]} \nMMSCFD',font =("Arial Narrow", 9, "bold"))
                        t.goto(length, -150)
                        t.showturtle()          
                        t.pendown() 
                        t.left(90)
                        t.forward(30)
                        t.stamp()
                        t.right(90)
                        t.width("14")
                        t.color(color)
                    if position =='injection':  
                        t.width("3")
                        t.color("red")
                        t.hideturtle()           
                        t.penup()
                        t.goto(length - 30 , 150)
                        t.write(f'{volume_point[branch_name]} \nMMSCFD',font =("Arial Narrow", 9, "bold")) 
                        t.goto(length, 120)
                        t.showturtle()          
                        t.pendown() 
                        t.left(90)
                        t.forward(30)
                        t.stamp()
                        t.right(90)
                        t.width("14")
                        t.color(color)

        def information(height, width, info ,data_type):
            if info == 'Input data' or info == 'Output data':
                t.width("3")
                t.hideturtle()           
                t.penup()
                t.goto(-width-20, height)
                t.write(f'{info}  ',font =("Arial Narrow", 14, "bold"))  
            else:
                if data_type == 'input':
                    t.width("3")
                    t.hideturtle()           
                    t.penup()  
                    t.goto(-width-17, height+10)
                    t.showturtle()          
                    t.pendown() 
                    t.forward(11)
                    t.hideturtle()           
                    t.penup() 
                    t.goto(-width, height)
                    t.write(f'{info} : {pipeline_propertice[info]}',font =("Arial Narrow", 11, "bold")) 
                if data_type == 'output':
                    t.width("3")
                    t.hideturtle()           
                    t.penup()  
                    t.goto(-width-17, height+10)
                    t.showturtle()          
                    t.pendown() 
                    t.forward(11)
                    t.hideturtle()           
                    t.penup() 
                    t.goto(-width, height)
                    t.write(f'{self.branch_pressure[info]}',font =("Arial Narrow", 10, "bold")) 

        color ="teal"
        t.color(color)  
        t.speed(10)
        information(240 ,505 ,'Input data','')
        height = 210
        width = 505
        for info in pipeline_propertice :
            print(height)
            information(height ,width ,info ,'input')
            if height == 60 :
                height -= 150
            else:
                height -= 30


        main_line(12, color)
        position = 'delivery'
        for branch in deliverely_dic:
            resize_branch = resize(deliverely_dic[branch] ,color ,True ,branch ,position ,True)
        position = 'injection'
        for branch in injections_dic:
            print(branch)
            resize_branch = resize(injections_dic[branch] ,color ,True ,branch ,position , True)


        # draw red line in pipe
        color = "red"
        t.color(color)  
        t.speed(20)
        main_line(3, color)
        t.speed(10)
        position = 'delivery'
        for branch in deliverely_dic:
            t.width("3")
            resize_branch = resize(deliverely_dic[branch] ,color ,True ,branch ,position ,False)

        # position = 'injection'
        # t.speed(20)
        # for branch in injections_dic:
        #     t.width("3")
        #     resize_branch = resize(injections_dic[branch] ,color ,True ,branch ,position , False)
        
        

        color ="teal"
        t.color(color)  
        information(240 ,-280 ,'Output data','')
        height = 210
        width = -280
        for info in self.branch_pressure :
            print(info)
            information( height ,width ,info ,'output')
            if height == 60 :
                height -= 150
            else:
                height -= 30
        print(self.branch_pressure)
        # for info in self.reynolds_taransmition_factor :
        #     print(info)
        #     information( height ,width ,info ,'output')
        #     if height == 60 :
        #         height -= 150
        #     else:
        #         height -= 30
        t.hideturtle()
        # turtle.getscreen()._root.mainloop()
        ws.exitonclick()
        print("OK")

    def next(self):
        self.window_3 = QtWidgets.QMainWindow()
        self.ui = Ui_Page3()
        self.ui.setupUi(self.window_3)
        self.Form.hide()
        self.window_3.show()

    def add(self):
        point_name = self.comboBox_branch_name.currentText()
        vol = self.inlet_volume_lineEdit.text()
        self.volume_point [point_name] = float(vol)

        self.base_pressure = float(self.base_pressure_lineEdit.text())
        self.base_temperature = float(self.base_temperature_lineEdit.text())
        print(self.volume_point)
        self.calculate()

    def calculate(self):
        global pipeline_propertice
        pipeline_propertice ={'pipeline length': 150.0, 'nominal pipe size': 20, 'wall thickness': 0.5, 'specific gravity': 0.65, 'viscosity': 8, 'absolute roughness': 150, 'compressibility factor': 0.85, 'drag factor': 0.96}
        
        F_factor = self.AGA_equation()
        print(F_factor)
        injections_dic = {'E' : 100}
        deliverely_dic = {'B' : 20, 'C' : 80}
        volume_point = {'inlet vol' : 250 , 'B' : 50, 'C' : 70, 'E' : 60}
        net_volume = {}
        main_dic = {}
        self.branch_pressure = {}
        G = pipeline_propertice['specific gravity']
        D = pipeline_propertice['nominal pipe size'] - 2 * pipeline_propertice['wall thickness']
        compressibility_factor = pipeline_propertice['compressibility factor']


        for val in injections_dic:
            main_dic[injections_dic[val]] = [val , 'inj']
        for val in deliverely_dic:
            main_dic[deliverely_dic[val]] = [val , 'del']

        sort = sorted(main_dic.items(), key = lambda x : x[0] )
        main_dic = {}
        for val in sort:
            main_dic [val[0]] = val[1]
        inlet_vol = volume_point['inlet vol']
        net_volume['inlet vol'] = [inlet_vol]

        x=0
        distance_list = []
        for val in main_dic :
            point = main_dic[val][0]
            branch_type = main_dic[val][1]
            distance = val - x
            x = val
            distance_list.append(distance)
            if branch_type == 'inj':
                inlet_vol = inlet_vol + volume_point[point]
                net_volume [point] = [inlet_vol]

            if branch_type == 'del':
                inlet_vol = inlet_vol - volume_point[point]
                net_volume [point] = [inlet_vol]

        f = main_dic.keys()
        distance_list.append(150-max(f))
        count = 0
        for val in net_volume.values() :
            val.append(distance_list[count])
            count+=1


        net_volume = dict(reversed(list(net_volume.items())))
        pressure = 314.7
        for val in net_volume :
            x = symbols('x')
            eq = 38.77 * F_factor * (self.base_temperature / self.base_pressure) * (((x**2 - pressure**2)/(G * self.base_temperature * net_volume[val][1] * compressibility_factor))**0.5) * D**(2.5) - net_volume[val][0] * (10**6)
            sol = solve(eq)
            P = sol[0]
            pressure = P
            self.branch_pressure [val] = f'Pressure at point {val} is {round(abs(P) ,2)} psig' 
            
    def reynolds(self) :
        global pipeline_propertice

        """
        Pb = base pressure, psia
        Tb = base temperature, R (460 + F)
        G = specific gravity of gas (Air = 1.0)
        Q = gas flow rate, standard ft3/day (SCFD)
        D = pipe inside diameter, in.
        viscosity = viscosity of gas, lb/ft-s
    """
        Pb = self.base_pressure
        Tb = self.base_temperature
        Q = 190 * (10**6)
        G = pipeline_propertice['specific gravity']
        D = pipeline_propertice['nominal pipe size'] - 2 * pipeline_propertice['wall thickness']
        visvosity = pipeline_propertice['viscosity'] * (10**-6)

        print(Pb, Tb, Q, G, D, visvosity)

        R = 0.0004778 * (Pb/Tb) * ((G * Q)/( visvosity * D))
        self.reynolds_taransmition_factor ['reynolds'] = f'Reynolds number is {round(R,3)}'
        return R

    def AGA_equation(self):
        global pipeline_propertice
        # for val in pipeline_propertice:
        #     print(val)
        # print(pipeline_propertice)
        pipeline_propertice ={'pipeline length': 150.0, 'nominal pipe size': 20, 'wall thickness': 0.5, 'specific gravity': 0.65, 'viscosity': 8, 'absolute roughness': 150, 'compressibility factor': 0.85, 'drag factor': 0.96}

        D = pipeline_propertice['nominal pipe size'] - 2 * pipeline_propertice['wall thickness']
        e = pipeline_propertice['absolute roughness'] * 10**(-6)
        # print(D,e)
        Re = self.reynolds()
        F1 = 4 * math.log10(3.7 * (D / e))
        print(Re)
        ft = 20
        for i in range(1000):
            Ft = 4 * math.log10(Re / ft) - 0.6

            if abs(Ft - ft) < 0.0001:
                break
            else:
                ft = Ft

        F2 = 4 * 0.96 * math.log10(Re / (1.4125 * Ft))

        print(F1 , F2)
        print(min(F1,F2))
        self.reynolds_taransmition_factor ['taransmition factor'] = f'taransmition factor is {round(min(F1,F2),3)}'
        # pipeline_propertice = pipeline_propertice + self.reynolds_taransmition_factor
        pipeline_propertice.update(self.reynolds_taransmition_factor)

        return round(min(F1,F2),3)




    def retranslateUi(self, Form):
        # branch_type = self.comboBox_branch_type.currentText()
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Estimate pipeline pressure "))
        self.inlet_volume_label.setText(_translate("Form", "select point and then enter inlet volume :"))
        self.base_pressure_label.setText(_translate("Form", "base pressure :"))
        self.base_temperature_label.setText(_translate("Form", "base temperature :"))

        self.discription_label.setText(_translate("Form", "in this part you must specify 2 delivery point and 3 \n\
injection point.\n\
when you enter points successfully Draw button will \n\
active and you can seen your pipeline figure."))
        self.next_pushButton.setText(_translate("Form", "Next"))
        self.draw_pushButton.setText(_translate("Form", "Draw"))
        self.back_pushButton.setText(_translate("Form", "Back"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Page1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())


