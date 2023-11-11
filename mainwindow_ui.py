# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gfdgd_xi/Desktop/deep-wine-runner/VM-source/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 512)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.isoPath = QtWidgets.QLineEdit(self.tab)
        self.isoPath.setObjectName("isoPath")
        self.horizontalLayout_2.addWidget(self.isoPath)
        self.browser = QtWidgets.QPushButton(self.tab)
        self.browser.setObjectName("browser")
        self.horizontalLayout_2.addWidget(self.browser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.systemVersion = QtWidgets.QComboBox(self.tab)
        self.systemVersion.setObjectName("systemVersion")
        self.systemVersion.addItem("")
        self.systemVersion.addItem("")
        self.systemVersion.addItem("")
        self.systemVersion.addItem("")
        self.systemVersion.addItem("")
        self.systemVersion.addItem("")
        self.systemVersion.addItem("")
        self.systemVersion.addItem("")
        self.systemVersion.addItem("")
        self.systemVersion.addItem("")
        self.horizontalLayout_3.addWidget(self.systemVersion)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.vmChooser = QtWidgets.QComboBox(self.tab)
        self.vmChooser.setDuplicatesEnabled(False)
        self.vmChooser.setObjectName("vmChooser")
        self.vmChooser.addItem("")
        self.vmChooser.addItem("")
        self.horizontalLayout_7.addWidget(self.vmChooser)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.getQemu = QtWidgets.QPushButton(self.tab)
        self.getQemu.setObjectName("getQemu")
        self.horizontalLayout_4.addWidget(self.getQemu)
        self.kvmTest = QtWidgets.QPushButton(self.tab)
        self.kvmTest.setObjectName("kvmTest")
        self.horizontalLayout_4.addWidget(self.kvmTest)
        self.qemuSetting = QtWidgets.QPushButton(self.tab)
        self.qemuSetting.setObjectName("qemuSetting")
        self.horizontalLayout_4.addWidget(self.qemuSetting)
        self.addQemuDiskButton = QtWidgets.QPushButton(self.tab)
        self.addQemuDiskButton.setObjectName("addQemuDiskButton")
        self.horizontalLayout_4.addWidget(self.addQemuDiskButton)
        self.saveQemuDiskButton = QtWidgets.QPushButton(self.tab)
        self.saveQemuDiskButton.setObjectName("saveQemuDiskButton")
        self.horizontalLayout_4.addWidget(self.saveQemuDiskButton)
        self.delQemuDiskButton = QtWidgets.QPushButton(self.tab)
        self.delQemuDiskButton.setObjectName("delQemuDiskButton")
        self.horizontalLayout_4.addWidget(self.delQemuDiskButton)
        self.getvbox = QtWidgets.QPushButton(self.tab)
        self.getvbox.setObjectName("getvbox")
        self.horizontalLayout_4.addWidget(self.getvbox)
        self.install = QtWidgets.QPushButton(self.tab)
        self.install.setObjectName("install")
        self.horizontalLayout_4.addWidget(self.install)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_3.setOpenLinks(False)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout.addWidget(self.textBrowser_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setUndoRedoEnabled(False)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_5.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(200, 200))
        self.label_3.setMaximumSize(QtCore.QSize(200, 200))
        self.label_3.setStyleSheet("border-image: url(:/deepin-wine-runner.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setOpenLinks(False)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_6.addWidget(self.textBrowser_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.CPUValue = QtWidgets.QStatusBar(MainWindow)
        self.CPUValue.setStatusTip("")
        self.CPUValue.setObjectName("CPUValue")
        MainWindow.setStatusBar(self.CPUValue)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1058, 36))
        self.menuBar.setObjectName("menuBar")
        self.menuVM = QtWidgets.QMenu(self.menuBar)
        self.menuVM.setObjectName("menuVM")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.addQemuDisk = QtWidgets.QAction(MainWindow)
        self.addQemuDisk.setObjectName("addQemuDisk")
        self.delQemuDisk = QtWidgets.QAction(MainWindow)
        self.delQemuDisk.setObjectName("delQemuDisk")
        self.actionVMInstallLog = QtWidgets.QAction(MainWindow)
        self.actionVMInstallLog.setObjectName("actionVMInstallLog")
        self.actionVMRunlLog = QtWidgets.QAction(MainWindow)
        self.actionVMRunlLog.setObjectName("actionVMRunlLog")
        self.actionVMTest = QtWidgets.QAction(MainWindow)
        self.actionVMTest.setObjectName("actionVMTest")
        self.menuVM.addAction(self.actionVMInstallLog)
        self.menuVM.addAction(self.actionVMRunlLog)
        self.menuVM.addSeparator()
        self.menuVM.addAction(self.actionVMTest)
        self.menuBar.addAction(self.menuVM.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.vmChooser.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Windows 应用适配工具"))
        self.label.setText(_translate("MainWindow", "镜像路径："))
        self.isoPath.setPlaceholderText(_translate("MainWindow", "请选择系统镜像"))
        self.browser.setText(_translate("MainWindow", "浏览……"))
        self.label_2.setText(_translate("MainWindow", "系统版本："))
        self.systemVersion.setCurrentText(_translate("MainWindow", "Windows 7 32 位（支持自动安装）"))
        self.systemVersion.setItemText(0, _translate("MainWindow", "Windows 7 32 位（支持自动安装）"))
        self.systemVersion.setItemText(1, _translate("MainWindow", "Windows 7 64 位（支持自动安装）"))
        self.systemVersion.setItemText(2, _translate("MainWindow", "其它 Windows 系统（不支持自动安装，传统启动，推荐 Windows 7 及以下）"))
        self.systemVersion.setItemText(3, _translate("MainWindow", "其他 Windows 系统（不支持自动安装，UEFI 启动，推荐 Windows 8 及以上）"))
        self.systemVersion.setItemText(4, _translate("MainWindow", "安装 WIndows 11（不支持自动安装）"))
        self.systemVersion.setItemText(5, _translate("MainWindow", "安装其他 Windows XP（支持自动安装，只支持 VirtualBox）"))
        self.systemVersion.setItemText(6, _translate("MainWindow", "安装其他 Windows （支持自动安装，传统启动，只支持 VirtualBox）"))
        self.systemVersion.setItemText(7, _translate("MainWindow", "安装其他 Windows（支持自动安装，UEFI 启动，只支持 VirtualBox）"))
        self.systemVersion.setItemText(8, _translate("MainWindow", "安装 arm32 系统（只支持 Qemu）"))
        self.systemVersion.setItemText(9, _translate("MainWindow", "安装 arm64 系统（只支持 Qemu）"))
        self.label_4.setText(_translate("MainWindow", "虚拟机（建议默认）："))
        self.vmChooser.setCurrentText(_translate("MainWindow", "qemu/kvm"))
        self.vmChooser.setItemText(0, _translate("MainWindow", "qemu/kvm"))
        self.vmChooser.setItemText(1, _translate("MainWindow", "VirtualBox"))
        self.getQemu.setText(_translate("MainWindow", "安装 Qemu"))
        self.kvmTest.setText(_translate("MainWindow", "kvm 测试"))
        self.qemuSetting.setText(_translate("MainWindow", "Qemu虚拟机设置"))
        self.addQemuDiskButton.setText(_translate("MainWindow", "添加/覆盖Qemu磁盘"))
        self.saveQemuDiskButton.setText(_translate("MainWindow", "导出Qemu磁盘"))
        self.delQemuDiskButton.setText(_translate("MainWindow", "移除Qemu磁盘"))
        self.getvbox.setText(_translate("MainWindow", "获取VirtualBox"))
        self.install.setText(_translate("MainWindow", "安装"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans CJK SC\'; font-size:10.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">UOS 3a4000 用户在使用 Qemu 时可能会出现虚拟机无法正常开机的问题，需要安装/降级到以下链接的版本：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">蓝奏云：</span><a href=\"https://gfdgdxi.lanzoue.com/b01rk9wza\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">https://gfdgdxi.lanzoue.com/b01rk9wza</span></a><span style=\" font-size:11pt;\"> 密码:6wvf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">诚通网盘：</span><a href=\"http://ctfile.gfdgdxi.top/d/31540479-58662214-c46520?p=2061\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">http://ctfile.gfdgdxi.top/d/31540479-58662214-c46520?p=2061</span></a><span style=\" font-size:11pt;\"> (访问密码: 2061)</span></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">注：Qemu 跨架构效率较低，如无特殊情况不建议跨架构/不开硬件加速（如 kvm）运行 Qemu</span></p>\n"
"<hr />\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">如何安装系统？使用迅雷或者网盘下载以下任意一个链接的 ISO 镜像然后在上面选择即可：</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">123 网盘链接：</span><a href=\"https://www.123pan.com/s/pDSKVv-oypWv\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">https://www.123pan.com/s/pDSKVv-oypWv</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">迅雷网盘：</span><a href=\"https://pan.xunlei.com/s/VNKMz3wgbYHg6JIh50ZKIc7pA1?pwd=35e5\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">https://pan.xunlei.com/s/VNKMz3wgbYHg6JIh50ZKIc7pA1?pwd=35e5</span></a><span style=\" font-size:10pt;\">  提取码：35e5</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">百度网盘：</span><a href=\"https://pan.baidu.com/s/19WbvinITCQJFZpAdZutrjg?pwd=me4y\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">https://pan.baidu.com/s/19WbvinITCQJFZpAdZutrjg?pwd=me4y</span></a><span style=\" font-size:10pt;\"> 提取码: me4y</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">诚通网盘：</span><a href=\"http://ctfile.gfdgdxi.top/d/31540479-58662220-3590cf?p=2061\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">http://ctfile.gfdgdxi.top/d/31540479-58662220-3590cf?p=2061</span></a><span style=\" font-size:10pt;\"> (访问密码: 2061)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">（如果下载这个，系统版本选第一项，一般推荐这个）</span><a href=\"ed2k://|file|cn_windows_7_ultimate_with_sp1_x86_dvd_u_677486.iso|2653276160|7503E4B9B8738DFCB95872445C72AEFB|/\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">ed2k://|file|cn_windows_7_ultimate_with_sp1_x86_dvd_u_677486.iso|2653276160|7503E4B9B8738DFCB95872445C72AEFB|/</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">（如果下载这个，系统版本选第二项）</span><a href=\"ed2k://|file|cn_windows_7_ultimate_with_sp1_x64_dvd_u_677408.iso|3420557312|B58548681854236C7939003B583A8078|/\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">ed2k://|file|cn_windows_7_ultimate_with_sp1_x64_dvd_u_677408.iso|3420557312|B58548681854236C7939003B583A8078|/</span></a></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">常用 Windows 软件：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">百度网盘：链接: </span><a href=\"https://pan.baidu.com/s/1D1NSy7k7XBnOZL_tNTnG6g?pwd=7s2p\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">https://pan.baidu.com/s/1D1NSy7k7XBnOZL_tNTnG6g?pwd=7s2p</span></a><span style=\" font-size:11pt;\"> 提取码: 7s2p </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">诚通网盘：</span><a href=\"http://ctfile.gfdgdxi.top/d/31540479-58659214-0732a8?p=2061\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">http://ctfile.gfdgdxi.top/d/31540479-58659214-0732a8?p=2061</span></a><span style=\" font-size:11pt;\"> (访问密码: 2061)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">123网盘：</span><a href=\"https://www.123pan.com/s/pDSKVv-uCBWv.html\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">https://www.123pan.com/s/pDSKVv-uCBWv.html</span></a></p>\n"
"<hr /></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "设置"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "设置"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans CJK SC\'; font-size:10.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600;\">给小白的一段话</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">其实本质上跑完安装程序就没有然后了，顶多如果想要运行舒服一点点，可以安装加强功能，直接拉到最底下看就可以了，<span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">只限使用 VirtualBox</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">如果你是用非 X86 PC，那暂时只能使用 qemu（没 kvm），且跨架构的性能损失很大，推荐使用 Windows XP 而非 Windows 7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">如果爱折腾的话，下面的都看看也无所谓的，想看往下翻就可以了</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">（这里的帮助更新可能不会那么及时，更详细/新的帮助可以看：https://gitee.com/gfdgd-xi/deep-wine-runner/wikis 或 https://gitee.com/gfdgd-xi/wine-runner-wiki）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">（如果鼠标被锁定到里面了按下键盘右边的“Ctrl”键就可以了，<span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">qemu则是 Ctrl+Alt+G</span> ）</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">VirtualBox 可以安装增强功能以优化体验，安装方法往下翻即可查询</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Qemu 可以安装 Virtio 以优化体验，下载链接：<a href=\"https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/</span></a></p>\n"
"<hr />\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600;\">安装是否需要人工进行操作？</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">如果您下载的镜像本程序支持，则大部分不用，已经尽量省去了让新手头疼的虚拟机程序安装，创建、设置虚拟机，虚拟磁盘分区，寻找原版镜像文件等内容</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_VirtualBox Machine_20220712191756.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">但有些设置依旧需要人工自行设置，例如安装界面密钥的输入、系统的激活（涉及版权问题，不会考虑省略）、增强功能的安装、需要使用的软件等等</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_VirtualBox Machine_20220712192850.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_VirtualBox Machine_20220712193527.png\" /></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600;\">什么样的镜像本程序（可能）不支持自动安装？</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">非 Windows 7 镜像可能不支持自动安装（纯的 Windows 7 企业版镜像可能不支持自动安装），不保证系统能自动安装成功，例如 Windows XP、Windows 10、Deepin、Ubuntu 等等</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600;\">默认的虚拟机设置不习惯怎么改？</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">1、打开启动器，打开 Oracle VM VirtualBox 程序</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">2、选择名字为“Windows”的虚拟机，然后在右边点击设置</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_VirtualBox Manager_20220712223602.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">3、在这里修改即可</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_VirtualBox_20220712223705.png\" /></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600;\">安装加强功能有什么好处？（只限使用 VirtualBox）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1、支持鼠标自由从虚拟机和实体机切换</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2、支持虚拟机根据窗口大小自动设置分辨率</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3、支持文件共享、剪切板共享、文件拖放</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4、支持无缝模式</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_选择区域_20220712224639.png\" /></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:600;\">如何安装加强功能？</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1、点击“设备”=》“加强功能”</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图_VirtualBox Machine_20220712142929.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2、打开“计算机”，找到名为“VirtualBox Guest Additions”的光盘，双击进入，然后双击打开名为“VBoxWindowsAdditions”的程序</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_VirtualBox Machine_20220712143006.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3、在弹出的界面点击“是”</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_VirtualBox Machine_20220712143018.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4、一直点“Next”</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_VirtualBox Machine_20220712143029.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_VirtualBox Machine_20220712143037.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">5、全部选择，然后点击“Install”进行安装</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_VirtualBox Machine_20220712143044.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">6、等待安装完毕后，选择“Reboot now”然后点击“Finish”重启此虚拟机即可安装成功（选择“Reboot now”并点“Finish”会自动重新启动）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/picture/截图/截图_VirtualBox Machine_20220712143103.png\" /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "安装/使用帮助"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans CJK SC\'; font-size:10.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">此为 wine 运行器附属组件（虽然违背了“Wine Is Not An Emulator”&lt;Wine 不是一个模拟器&gt;的原意），旨在能更加完美、简单的运行 Windows 应用</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本程序基于 C++ Qt、Python 和 Virtualbox 制作，通过运行安装 Windows 操作系统的虚拟机实现在 Linux 运行 Windows exe 程序的功能。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">基于 GPL V3 协议开源</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">项目地址：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Gitee：<a href=\"https://gitee.com/gfdgd-xi/deep-wine-runner\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">https://gitee.com/gfdgd-xi/deep-wine-runner</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Github：<a href=\"https://github.com/gfdgd-xi/deep-wine-runner\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">https://github.com/gfdgd-xi/deep-wine-runner</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Gitlink：<a href=\"https://gitlink.org.cn/gfdgd_xi/deep-wine-runner\"><span style=\" font-size:11pt; text-decoration: underline; color:#0082fa;\">https://gitlink.org.cn/gfdgd_xi/deep-wine-runner</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">此组件也有非常大的缺点，就是相比于 Wine，会需要占用大量的空间、安装需要大量的时间、某些情况下需要相比于 Wine 需要消耗更多的系统资源，但可以更加完美、流畅的运行 Windows 应用，会尽量减少因为缺少或未实现导致的 Windows exe 程序运行异常</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">该组件制作者：gfdgd xi</p>\n"
"<hr />\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "关于"))
        self.menuVM.setTitle(_translate("MainWindow", "虚拟机"))
        self.action.setText(_translate("MainWindow", "退出"))
        self.action_2.setText(_translate("MainWindow", "关于"))
        self.addQemuDisk.setText(_translate("MainWindow", "导入/覆盖"))
        self.delQemuDisk.setText(_translate("MainWindow", "导出"))
        self.actionVMInstallLog.setText(_translate("MainWindow", "虚拟机安装日志"))
        self.actionVMRunlLog.setText(_translate("MainWindow", "虚拟机运行日志"))
        self.actionVMTest.setText(_translate("MainWindow", "虚拟机测试（X86、Qemu）"))