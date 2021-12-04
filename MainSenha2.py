from PySide2 import QtCore, QtGui, QtWidgets
from ui_Gera_SenhaF import Ui_MainWindow
from random import shuffle, choice
import string as st
import numpy as np

class main(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(main,self).__init__()
        self.setupUi(self)

        self.senha = ''
        self.verif = np.zeros(5)

        self.btnGeraSen.clicked.connect(self.BtnGeraSen)
        self.inpTamSen.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(r'[0-9]{,5}')))

    
    def caixa1(self):
        if(self.cbMaius.isChecked()):
            self.senha += st.ascii_uppercase
            self.verif[0] = 1
        else:
            self.senha += ''
    
    def caixa2(self):
        if(self.cbMinus.isChecked()):
            self.senha += st.ascii_lowercase
            self.verif[1] = 1
        else:
            self.senha += ''

    def caixa3(self):
        if(self.cbNum.isChecked()):
            self.senha += st.digits
            self.verif[2] = 1
        else:
            self.senha += ''
    
    def caixa4(self):
        if(self.cbSimb.isChecked()):
            self.senha += st.punctuation
            self.verif[3] = 1
        else:
            self.senha += ''
            

    def caixa5(self):
        if(self.cbEspec.isChecked()):
            texto = self.lblEspec.text()
            self.verif[4] = 1
        else:
            texto = ''
          

        return texto

    def BtnGeraSen(self):
        senha = ''
        Auxsenha = ''
        verifi = 0
        self.caixa1()
        self.caixa2()
        self.caixa3()
        self.caixa4()
        texto = self.caixa5()
        TamSen = self.inpTamSen.text()
        
        if(TamSen == ""):
            self.label.setText("INFORME TAMANHO DA SENHA")
            self.inpTamSen.setFocus()
        
        if(TamSen != ""):
            self.label.setText("")
            tam = int(TamSen)

            for i in range(5):
                verifi += self.verif[i]
            
            if(verifi == 0):
                self.label.setText("SELECIONE UM CAMPO")
            
            else:
                if (self.verif[4] == 1):
                    if(len(texto) < tam):
                        aux = tam - len(texto)
                        for i in range(aux):
                            Auxsenha+=choice(self.senha)
                        Auxsenha+=texto
                        senha = ''.join(Auxsenha.split(' '))
                        self.label.setText("")
                    
                    elif(len(texto) == tam):
                        senha = ''.join(texto.split(' '))
                        self.label.setText("")
                    
                    else:
                        self.label.setText("TEXTO MAIOR QUE A SENHA")
                else:
                    for i in range(tam):
                        Auxsenha +=choice(self.senha)
                    senha = ''.join(Auxsenha.split(' '))

        if(self.checkBox.isChecked()):
            lisSen = list(senha)
            shuffle(lisSen)
            senha = ''.join(lisSen)
            self.leSenha.setText(senha)
        else:
            self.leSenha.setText(senha)

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela = main()
    tela.show()
    sys.exit(app.exec_())