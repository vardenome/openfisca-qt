# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/page08.ui'
#
# Created: Thu May 24 14:03:04 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Page08(object):
    def setupUi(self, Page08):
        Page08.setObjectName(_fromUtf8("Page08"))
        Page08.resize(730, 372)
        Page08.setMinimumSize(QtCore.QSize(730, 0))
        Page08.setMaximumSize(QtCore.QSize(730, 16777215))
        Page08.setWindowTitle(QtGui.QApplication.translate("Page08", "Form", None, QtGui.QApplication.UnicodeUTF8))
        Page08.setStyleSheet(_fromUtf8(""))
        self.gridLayout_2 = QtGui.QGridLayout(Page08)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(Page08)
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setText(QtGui.QApplication.translate("Page08", "8| DIVERS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setProperty("class", QtGui.QApplication.translate("Page08", "titreA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_60 = QtGui.QLabel(Page08)
        self.label_60.setStyleSheet(_fromUtf8(""))
        self.label_60.setText(QtGui.QApplication.translate("Page08", "Élus locaux indemnités de fonction soumises à la retenue à la source", None, QtGui.QApplication.UnicodeUTF8))
        self.label_60.setProperty("class", QtGui.QApplication.translate("Page08", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.gridLayout.addWidget(self.label_60, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label_61 = QtGui.QLabel(Page08)
        self.label_61.setMinimumSize(QtCore.QSize(30, 20))
        self.label_61.setMaximumSize(QtCore.QSize(30, 20))
        self.label_61.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_61.setStyleSheet(_fromUtf8(""))
        self.label_61.setText(QtGui.QApplication.translate("Page08", "8BY", None, QtGui.QApplication.UnicodeUTF8))
        self.label_61.setProperty("class", QtGui.QApplication.translate("Page08", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.gridLayout.addWidget(self.label_61, 0, 2, 1, 1)
        self.f8by = QtGui.QSpinBox(Page08)
        self.f8by.setEnabled(True)
        self.f8by.setMinimumSize(QtCore.QSize(60, 20))
        self.f8by.setMaximumSize(QtCore.QSize(60, 20))
        self.f8by.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f8by.setWrapping(False)
        self.f8by.setFrame(True)
        self.f8by.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f8by.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f8by.setAccelerated(False)
        self.f8by.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f8by.setKeyboardTracking(True)
        self.f8by.setSuffix(_fromUtf8(""))
        self.f8by.setPrefix(_fromUtf8(""))
        self.f8by.setMinimum(0)
        self.f8by.setMaximum(999999)
        self.f8by.setSingleStep(1000)
        self.f8by.setProperty("value", 0)
        self.f8by.setObjectName(_fromUtf8("f8by"))
        self.gridLayout.addWidget(self.f8by, 0, 3, 1, 1)
        self.label_59 = QtGui.QLabel(Page08)
        self.label_59.setMinimumSize(QtCore.QSize(30, 20))
        self.label_59.setMaximumSize(QtCore.QSize(30, 20))
        self.label_59.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_59.setStyleSheet(_fromUtf8(""))
        self.label_59.setText(QtGui.QApplication.translate("Page08", "8CY", None, QtGui.QApplication.UnicodeUTF8))
        self.label_59.setProperty("class", QtGui.QApplication.translate("Page08", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.gridLayout.addWidget(self.label_59, 0, 4, 1, 1)
        self.f8cy = QtGui.QSpinBox(Page08)
        self.f8cy.setEnabled(True)
        self.f8cy.setMinimumSize(QtCore.QSize(60, 20))
        self.f8cy.setMaximumSize(QtCore.QSize(60, 20))
        self.f8cy.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f8cy.setWrapping(False)
        self.f8cy.setFrame(True)
        self.f8cy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f8cy.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f8cy.setAccelerated(False)
        self.f8cy.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f8cy.setKeyboardTracking(True)
        self.f8cy.setSuffix(_fromUtf8(""))
        self.f8cy.setPrefix(_fromUtf8(""))
        self.f8cy.setMinimum(0)
        self.f8cy.setMaximum(999999)
        self.f8cy.setSingleStep(1000)
        self.f8cy.setProperty("value", 0)
        self.f8cy.setObjectName(_fromUtf8("f8cy"))
        self.gridLayout.addWidget(self.f8cy, 0, 5, 1, 2)
        self.label_63 = QtGui.QLabel(Page08)
        self.label_63.setStyleSheet(_fromUtf8(""))
        self.label_63.setText(QtGui.QApplication.translate("Page08", "Plus-values en report d’imposition non expiré", None, QtGui.QApplication.UnicodeUTF8))
        self.label_63.setProperty("class", QtGui.QApplication.translate("Page08", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.gridLayout.addWidget(self.label_63, 1, 0, 1, 1)
        self.label_62 = QtGui.QLabel(Page08)
        self.label_62.setMinimumSize(QtCore.QSize(30, 20))
        self.label_62.setMaximumSize(QtCore.QSize(30, 20))
        self.label_62.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_62.setStyleSheet(_fromUtf8(""))
        self.label_62.setText(QtGui.QApplication.translate("Page08", "8UT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_62.setProperty("class", QtGui.QApplication.translate("Page08", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.gridLayout.addWidget(self.label_62, 1, 4, 1, 1)
        self.f8ut = QtGui.QSpinBox(Page08)
        self.f8ut.setEnabled(True)
        self.f8ut.setMinimumSize(QtCore.QSize(60, 20))
        self.f8ut.setMaximumSize(QtCore.QSize(60, 20))
        self.f8ut.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f8ut.setWrapping(False)
        self.f8ut.setFrame(True)
        self.f8ut.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f8ut.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f8ut.setAccelerated(False)
        self.f8ut.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f8ut.setKeyboardTracking(True)
        self.f8ut.setSuffix(_fromUtf8(""))
        self.f8ut.setPrefix(_fromUtf8(""))
        self.f8ut.setMinimum(0)
        self.f8ut.setMaximum(999999)
        self.f8ut.setSingleStep(1000)
        self.f8ut.setProperty("value", 0)
        self.f8ut.setObjectName(_fromUtf8("f8ut"))
        self.gridLayout.addWidget(self.f8ut, 1, 5, 1, 2)
        self.label_66 = QtGui.QLabel(Page08)
        self.label_66.setStyleSheet(_fromUtf8(""))
        self.label_66.setText(QtGui.QApplication.translate("Page08", "Personnes domiciliées en France percevant des revenus à l’étranger cf. déclaration n° 2047", None, QtGui.QApplication.UnicodeUTF8))
        self.label_66.setProperty("class", QtGui.QApplication.translate("Page08", "titreB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_66.setObjectName(_fromUtf8("label_66"))
        self.gridLayout.addWidget(self.label_66, 2, 0, 1, 2)
        self.label_65 = QtGui.QLabel(Page08)
        self.label_65.setStyleSheet(_fromUtf8(""))
        self.label_65.setText(QtGui.QApplication.translate("Page08", "– Revenus exonérés (y compris salaires et primes des détachés à l’étranger) \n"
"non déclarés page 3, retenus pour le calcul du taux effectif", None, QtGui.QApplication.UnicodeUTF8))
        self.label_65.setProperty("class", QtGui.QApplication.translate("Page08", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.label_65.setObjectName(_fromUtf8("label_65"))
        self.gridLayout.addWidget(self.label_65, 3, 0, 1, 1)
        self.label_64 = QtGui.QLabel(Page08)
        self.label_64.setMinimumSize(QtCore.QSize(30, 20))
        self.label_64.setMaximumSize(QtCore.QSize(30, 20))
        self.label_64.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_64.setStyleSheet(_fromUtf8(""))
        self.label_64.setText(QtGui.QApplication.translate("Page08", "8TI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_64.setProperty("class", QtGui.QApplication.translate("Page08", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.gridLayout.addWidget(self.label_64, 3, 4, 1, 1)
        self.f8ti = QtGui.QSpinBox(Page08)
        self.f8ti.setEnabled(True)
        self.f8ti.setMinimumSize(QtCore.QSize(60, 20))
        self.f8ti.setMaximumSize(QtCore.QSize(60, 20))
        self.f8ti.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f8ti.setWrapping(False)
        self.f8ti.setFrame(True)
        self.f8ti.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f8ti.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f8ti.setAccelerated(False)
        self.f8ti.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f8ti.setKeyboardTracking(True)
        self.f8ti.setSuffix(_fromUtf8(""))
        self.f8ti.setPrefix(_fromUtf8(""))
        self.f8ti.setMinimum(0)
        self.f8ti.setMaximum(999999)
        self.f8ti.setSingleStep(1000)
        self.f8ti.setProperty("value", 0)
        self.f8ti.setObjectName(_fromUtf8("f8ti"))
        self.gridLayout.addWidget(self.f8ti, 3, 5, 1, 2)
        self.label_68 = QtGui.QLabel(Page08)
        self.label_68.setStyleSheet(_fromUtf8(""))
        self.label_68.setText(QtGui.QApplication.translate("Page08", "– Revenus étrangers soumis en France à l’impôt sur le revenu et imposables à la CRDS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_68.setProperty("class", QtGui.QApplication.translate("Page08", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.gridLayout.addWidget(self.label_68, 4, 0, 1, 2)
        self.label_67 = QtGui.QLabel(Page08)
        self.label_67.setMinimumSize(QtCore.QSize(30, 20))
        self.label_67.setMaximumSize(QtCore.QSize(30, 20))
        self.label_67.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_67.setStyleSheet(_fromUtf8(""))
        self.label_67.setText(QtGui.QApplication.translate("Page08", "8TL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_67.setProperty("class", QtGui.QApplication.translate("Page08", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_67.setObjectName(_fromUtf8("label_67"))
        self.gridLayout.addWidget(self.label_67, 4, 4, 1, 1)
        self.f8tl = QtGui.QSpinBox(Page08)
        self.f8tl.setEnabled(True)
        self.f8tl.setMinimumSize(QtCore.QSize(60, 20))
        self.f8tl.setMaximumSize(QtCore.QSize(60, 20))
        self.f8tl.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f8tl.setWrapping(False)
        self.f8tl.setFrame(True)
        self.f8tl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f8tl.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f8tl.setAccelerated(False)
        self.f8tl.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f8tl.setKeyboardTracking(True)
        self.f8tl.setSuffix(_fromUtf8(""))
        self.f8tl.setPrefix(_fromUtf8(""))
        self.f8tl.setMinimum(0)
        self.f8tl.setMaximum(999999)
        self.f8tl.setSingleStep(1000)
        self.f8tl.setProperty("value", 0)
        self.f8tl.setObjectName(_fromUtf8("f8tl"))
        self.gridLayout.addWidget(self.f8tl, 4, 5, 1, 2)
        self.label_70 = QtGui.QLabel(Page08)
        self.label_70.setStyleSheet(_fromUtf8(""))
        self.label_70.setText(QtGui.QApplication.translate("Page08", "– Revenus étrangers imposables en France, ouvrant droit à un crédit d’impôt égal \n"
"au montant de l’impôt français", None, QtGui.QApplication.UnicodeUTF8))
        self.label_70.setProperty("class", QtGui.QApplication.translate("Page08", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.gridLayout.addWidget(self.label_70, 5, 0, 1, 1)
        self.label_69 = QtGui.QLabel(Page08)
        self.label_69.setMinimumSize(QtCore.QSize(30, 20))
        self.label_69.setMaximumSize(QtCore.QSize(30, 20))
        self.label_69.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_69.setStyleSheet(_fromUtf8(""))
        self.label_69.setText(QtGui.QApplication.translate("Page08", "8TK", None, QtGui.QApplication.UnicodeUTF8))
        self.label_69.setProperty("class", QtGui.QApplication.translate("Page08", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.gridLayout.addWidget(self.label_69, 5, 4, 1, 1)
        self.f8tk = QtGui.QSpinBox(Page08)
        self.f8tk.setEnabled(True)
        self.f8tk.setMinimumSize(QtCore.QSize(60, 20))
        self.f8tk.setMaximumSize(QtCore.QSize(60, 20))
        self.f8tk.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.f8tk.setWrapping(False)
        self.f8tk.setFrame(True)
        self.f8tk.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.f8tk.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.f8tk.setAccelerated(False)
        self.f8tk.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.f8tk.setKeyboardTracking(True)
        self.f8tk.setSuffix(_fromUtf8(""))
        self.f8tk.setPrefix(_fromUtf8(""))
        self.f8tk.setMinimum(0)
        self.f8tk.setMaximum(999999)
        self.f8tk.setSingleStep(1000)
        self.f8tk.setProperty("value", 0)
        self.f8tk.setObjectName(_fromUtf8("f8tk"))
        self.gridLayout.addWidget(self.f8tk, 5, 5, 1, 2)
        self.label_72 = QtGui.QLabel(Page08)
        self.label_72.setStyleSheet(_fromUtf8(""))
        self.label_72.setText(QtGui.QApplication.translate("Page08", "Revenus exonérés non retenus pour le calcul du taux effectif \n"
"revenus d’organismes internationaux, de représentations étrangères", None, QtGui.QApplication.UnicodeUTF8))
        self.label_72.setProperty("class", QtGui.QApplication.translate("Page08", "texte01", None, QtGui.QApplication.UnicodeUTF8))
        self.label_72.setObjectName(_fromUtf8("label_72"))
        self.gridLayout.addWidget(self.label_72, 6, 0, 1, 1)
        self.label_71 = QtGui.QLabel(Page08)
        self.label_71.setMinimumSize(QtCore.QSize(30, 20))
        self.label_71.setMaximumSize(QtCore.QSize(30, 20))
        self.label_71.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_71.setStyleSheet(_fromUtf8(""))
        self.label_71.setText(QtGui.QApplication.translate("Page08", "8FV", None, QtGui.QApplication.UnicodeUTF8))
        self.label_71.setProperty("class", QtGui.QApplication.translate("Page08", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_71.setObjectName(_fromUtf8("label_71"))
        self.gridLayout.addWidget(self.label_71, 6, 4, 1, 1)
        self.label_73 = QtGui.QLabel(Page08)
        self.label_73.setMinimumSize(QtCore.QSize(41, 20))
        self.label_73.setMaximumSize(QtCore.QSize(41, 20))
        self.label_73.setText(QtGui.QApplication.translate("Page08", "cochez", None, QtGui.QApplication.UnicodeUTF8))
        self.label_73.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_73.setProperty("class", QtGui.QApplication.translate("Page08", "texte02", None, QtGui.QApplication.UnicodeUTF8))
        self.label_73.setObjectName(_fromUtf8("label_73"))
        self.gridLayout.addWidget(self.label_73, 6, 5, 1, 1)
        self.f8fv = QtGui.QCheckBox(Page08)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.f8fv.setFont(font)
        self.f8fv.setText(_fromUtf8(""))
        self.f8fv.setObjectName(_fromUtf8("f8fv"))
        self.gridLayout.addWidget(self.f8fv, 6, 6, 1, 1)
        self.label_75 = QtGui.QLabel(Page08)
        self.label_75.setStyleSheet(_fromUtf8(""))
        self.label_75.setText(QtGui.QApplication.translate("Page08", "Contrats d’assurance-vie conclus à l’étranger", None, QtGui.QApplication.UnicodeUTF8))
        self.label_75.setProperty("class", QtGui.QApplication.translate("Page08", "titreC", None, QtGui.QApplication.UnicodeUTF8))
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.gridLayout.addWidget(self.label_75, 7, 0, 1, 1)
        self.label_74 = QtGui.QLabel(Page08)
        self.label_74.setMinimumSize(QtCore.QSize(30, 20))
        self.label_74.setMaximumSize(QtCore.QSize(30, 20))
        self.label_74.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_74.setStyleSheet(_fromUtf8(""))
        self.label_74.setText(QtGui.QApplication.translate("Page08", "8TT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_74.setProperty("class", QtGui.QApplication.translate("Page08", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_74.setObjectName(_fromUtf8("label_74"))
        self.gridLayout.addWidget(self.label_74, 7, 4, 1, 1)
        self.label_78 = QtGui.QLabel(Page08)
        self.label_78.setMinimumSize(QtCore.QSize(41, 20))
        self.label_78.setMaximumSize(QtCore.QSize(41, 20))
        self.label_78.setText(QtGui.QApplication.translate("Page08", "cochez", None, QtGui.QApplication.UnicodeUTF8))
        self.label_78.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_78.setProperty("class", QtGui.QApplication.translate("Page08", "texte02", None, QtGui.QApplication.UnicodeUTF8))
        self.label_78.setObjectName(_fromUtf8("label_78"))
        self.gridLayout.addWidget(self.label_78, 7, 5, 1, 1)
        self.f8tt = QtGui.QCheckBox(Page08)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.f8tt.setFont(font)
        self.f8tt.setText(_fromUtf8(""))
        self.f8tt.setObjectName(_fromUtf8("f8tt"))
        self.gridLayout.addWidget(self.f8tt, 7, 6, 1, 1)
        self.label_77 = QtGui.QLabel(Page08)
        self.label_77.setStyleSheet(_fromUtf8(""))
        self.label_77.setText(QtGui.QApplication.translate("Page08", "Comptes bancaires à l’étranger", None, QtGui.QApplication.UnicodeUTF8))
        self.label_77.setProperty("class", QtGui.QApplication.translate("Page08", "titreC", None, QtGui.QApplication.UnicodeUTF8))
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.gridLayout.addWidget(self.label_77, 8, 0, 1, 1)
        self.label_76 = QtGui.QLabel(Page08)
        self.label_76.setMinimumSize(QtCore.QSize(30, 20))
        self.label_76.setMaximumSize(QtCore.QSize(30, 20))
        self.label_76.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_76.setStyleSheet(_fromUtf8(""))
        self.label_76.setText(QtGui.QApplication.translate("Page08", "8UU", None, QtGui.QApplication.UnicodeUTF8))
        self.label_76.setProperty("class", QtGui.QApplication.translate("Page08", "code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.gridLayout.addWidget(self.label_76, 8, 4, 1, 1)
        self.label_79 = QtGui.QLabel(Page08)
        self.label_79.setMinimumSize(QtCore.QSize(41, 20))
        self.label_79.setMaximumSize(QtCore.QSize(41, 20))
        self.label_79.setText(QtGui.QApplication.translate("Page08", "cochez", None, QtGui.QApplication.UnicodeUTF8))
        self.label_79.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_79.setProperty("class", QtGui.QApplication.translate("Page08", "texte02", None, QtGui.QApplication.UnicodeUTF8))
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.gridLayout.addWidget(self.label_79, 8, 5, 1, 1)
        self.f8uu = QtGui.QCheckBox(Page08)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.f8uu.setFont(font)
        self.f8uu.setText(_fromUtf8(""))
        self.f8uu.setObjectName(_fromUtf8("f8uu"))
        self.gridLayout.addWidget(self.f8uu, 8, 6, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 53, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)

        self.retranslateUi(Page08)
        QtCore.QMetaObject.connectSlotsByName(Page08)
        Page08.setTabOrder(self.f8by, self.f8cy)
        Page08.setTabOrder(self.f8cy, self.f8ut)
        Page08.setTabOrder(self.f8ut, self.f8ti)
        Page08.setTabOrder(self.f8ti, self.f8tl)
        Page08.setTabOrder(self.f8tl, self.f8tk)
        Page08.setTabOrder(self.f8tk, self.f8fv)
        Page08.setTabOrder(self.f8fv, self.f8tt)
        Page08.setTabOrder(self.f8tt, self.f8uu)

    def retranslateUi(self, Page08):
        pass

