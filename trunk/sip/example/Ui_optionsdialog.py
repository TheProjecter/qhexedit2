# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\_SVN\QHexEdit\sip\example\optionsdialog.ui'
#
# Created: Tue Aug 30 17:49:24 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_OptionsDialog(object):
    def setupUi(self, OptionsDialog):
        OptionsDialog.setObjectName("OptionsDialog")
        OptionsDialog.resize(395, 351)
        self.verticalLayout = QtGui.QVBoxLayout(OptionsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbFlags = QtGui.QGroupBox(OptionsDialog)
        self.gbFlags.setObjectName("gbFlags")
        self.gridLayout_2 = QtGui.QGridLayout(self.gbFlags)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cbAddressArea = QtGui.QCheckBox(self.gbFlags)
        self.cbAddressArea.setObjectName("cbAddressArea")
        self.gridLayout_2.addWidget(self.cbAddressArea, 0, 0, 1, 1)
        self.cbOverwriteMode = QtGui.QCheckBox(self.gbFlags)
        self.cbOverwriteMode.setObjectName("cbOverwriteMode")
        self.gridLayout_2.addWidget(self.cbOverwriteMode, 0, 1, 1, 1)
        self.cbAsciiArea = QtGui.QCheckBox(self.gbFlags)
        self.cbAsciiArea.setObjectName("cbAsciiArea")
        self.gridLayout_2.addWidget(self.cbAsciiArea, 1, 0, 1, 1)
        self.cbHighlighting = QtGui.QCheckBox(self.gbFlags)
        self.cbHighlighting.setObjectName("cbHighlighting")
        self.gridLayout_2.addWidget(self.cbHighlighting, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.gbFlags)
        self.gbColors = QtGui.QGroupBox(OptionsDialog)
        self.gbColors.setObjectName("gbColors")
        self.gridLayout = QtGui.QGridLayout(self.gbColors)
        self.gridLayout.setObjectName("gridLayout")
        self.pbHighlightingColor = QtGui.QPushButton(self.gbColors)
        self.pbHighlightingColor.setObjectName("pbHighlightingColor")
        self.gridLayout.addWidget(self.pbHighlightingColor, 0, 0, 1, 1)
        self.lbHighlightingColor = QtGui.QLabel(self.gbColors)
        self.lbHighlightingColor.setMinimumSize(QtCore.QSize(100, 0))
        self.lbHighlightingColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbHighlightingColor.setFrameShape(QtGui.QFrame.Panel)
        self.lbHighlightingColor.setFrameShadow(QtGui.QFrame.Sunken)
        self.lbHighlightingColor.setText("")
        self.lbHighlightingColor.setObjectName("lbHighlightingColor")
        self.gridLayout.addWidget(self.lbHighlightingColor, 0, 1, 1, 1)
        self.pbAddressAreaColor = QtGui.QPushButton(self.gbColors)
        self.pbAddressAreaColor.setObjectName("pbAddressAreaColor")
        self.gridLayout.addWidget(self.pbAddressAreaColor, 1, 0, 2, 1)
        self.lbAddressAreaColor = QtGui.QLabel(self.gbColors)
        self.lbAddressAreaColor.setMinimumSize(QtCore.QSize(100, 0))
        self.lbAddressAreaColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbAddressAreaColor.setFrameShape(QtGui.QFrame.Panel)
        self.lbAddressAreaColor.setFrameShadow(QtGui.QFrame.Sunken)
        self.lbAddressAreaColor.setText("")
        self.lbAddressAreaColor.setObjectName("lbAddressAreaColor")
        self.gridLayout.addWidget(self.lbAddressAreaColor, 1, 1, 2, 1)
        self.lbSelectionColor = QtGui.QLabel(self.gbColors)
        self.lbSelectionColor.setMinimumSize(QtCore.QSize(100, 0))
        self.lbSelectionColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbSelectionColor.setFrameShape(QtGui.QFrame.Panel)
        self.lbSelectionColor.setFrameShadow(QtGui.QFrame.Sunken)
        self.lbSelectionColor.setText("")
        self.lbSelectionColor.setObjectName("lbSelectionColor")
        self.gridLayout.addWidget(self.lbSelectionColor, 3, 1, 1, 1)
        self.pbSelectionColor = QtGui.QPushButton(self.gbColors)
        self.pbSelectionColor.setObjectName("pbSelectionColor")
        self.gridLayout.addWidget(self.pbSelectionColor, 3, 0, 1, 1)
        self.pbWidgetFont = QtGui.QPushButton(self.gbColors)
        self.pbWidgetFont.setObjectName("pbWidgetFont")
        self.gridLayout.addWidget(self.pbWidgetFont, 4, 0, 1, 1)
        self.leWidgetFont = QtGui.QLineEdit(self.gbColors)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leWidgetFont.sizePolicy().hasHeightForWidth())
        self.leWidgetFont.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.leWidgetFont.setFont(font)
        self.leWidgetFont.setObjectName("leWidgetFont")
        self.gridLayout.addWidget(self.leWidgetFont, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.gbColors)
        self.gbAddressAreaWidth = QtGui.QGroupBox(OptionsDialog)
        self.gbAddressAreaWidth.setObjectName("gbAddressAreaWidth")
        self.gridLayout_3 = QtGui.QGridLayout(self.gbAddressAreaWidth)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbAddressAreaWidth = QtGui.QLabel(self.gbAddressAreaWidth)
        self.lbAddressAreaWidth.setObjectName("lbAddressAreaWidth")
        self.gridLayout_3.addWidget(self.lbAddressAreaWidth, 0, 0, 1, 1)
        self.sbAddressAreaWidth = QtGui.QSpinBox(self.gbAddressAreaWidth)
        self.sbAddressAreaWidth.setMinimum(1)
        self.sbAddressAreaWidth.setMaximum(6)
        self.sbAddressAreaWidth.setProperty("value", 4)
        self.sbAddressAreaWidth.setObjectName("sbAddressAreaWidth")
        self.gridLayout_3.addWidget(self.sbAddressAreaWidth, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.gbAddressAreaWidth)
        spacerItem = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(OptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(OptionsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), OptionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), OptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OptionsDialog)
        OptionsDialog.setTabOrder(self.cbOverwriteMode, self.cbAsciiArea)
        OptionsDialog.setTabOrder(self.cbAsciiArea, self.cbAddressArea)
        OptionsDialog.setTabOrder(self.cbAddressArea, self.cbHighlighting)
        OptionsDialog.setTabOrder(self.cbHighlighting, self.pbHighlightingColor)
        OptionsDialog.setTabOrder(self.pbHighlightingColor, self.pbAddressAreaColor)
        OptionsDialog.setTabOrder(self.pbAddressAreaColor, self.buttonBox)

    def retranslateUi(self, OptionsDialog):
        OptionsDialog.setWindowTitle(QtGui.QApplication.translate("OptionsDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.gbFlags.setTitle(QtGui.QApplication.translate("OptionsDialog", "Flags", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAddressArea.setText(QtGui.QApplication.translate("OptionsDialog", "Address Area", None, QtGui.QApplication.UnicodeUTF8))
        self.cbOverwriteMode.setText(QtGui.QApplication.translate("OptionsDialog", "Overwrite Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAsciiArea.setText(QtGui.QApplication.translate("OptionsDialog", "Ascii Area", None, QtGui.QApplication.UnicodeUTF8))
        self.cbHighlighting.setText(QtGui.QApplication.translate("OptionsDialog", "Higlighting", None, QtGui.QApplication.UnicodeUTF8))
        self.gbColors.setTitle(QtGui.QApplication.translate("OptionsDialog", "Colors and Fonts", None, QtGui.QApplication.UnicodeUTF8))
        self.pbHighlightingColor.setText(QtGui.QApplication.translate("OptionsDialog", "Highlighting Color", None, QtGui.QApplication.UnicodeUTF8))
        self.pbAddressAreaColor.setText(QtGui.QApplication.translate("OptionsDialog", "Address Area Color", None, QtGui.QApplication.UnicodeUTF8))
        self.pbSelectionColor.setText(QtGui.QApplication.translate("OptionsDialog", "Selection Color", None, QtGui.QApplication.UnicodeUTF8))
        self.pbWidgetFont.setText(QtGui.QApplication.translate("OptionsDialog", "Widget Font", None, QtGui.QApplication.UnicodeUTF8))
        self.leWidgetFont.setText(QtGui.QApplication.translate("OptionsDialog", "01 23 45 67 89 ab cd ef", None, QtGui.QApplication.UnicodeUTF8))
        self.gbAddressAreaWidth.setTitle(QtGui.QApplication.translate("OptionsDialog", "Address Area", None, QtGui.QApplication.UnicodeUTF8))
        self.lbAddressAreaWidth.setText(QtGui.QApplication.translate("OptionsDialog", "Address Area Width", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    OptionsDialog = QtGui.QDialog()
    ui = Ui_OptionsDialog()
    ui.setupUi(OptionsDialog)
    OptionsDialog.show()
    sys.exit(app.exec_())
