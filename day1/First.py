import sys
from PySide2.QtWidgets import QApplication,QWidget
if __name__ == '__main__':
    # 创建QApplication类实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(300,150)
    # 窗口显示坐标
    w.move(300,300)
    # 设置title
    w.setWindowTitle('第一个PyQT5应用')
    # 显示窗口
    w.show()
    # 进入程序主循环，使窗口不会退出
    sys.exit(app.exec_())