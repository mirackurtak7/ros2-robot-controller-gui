from PySide2.QtWidgets import QApplication, QDialog, QMainWindow
from PySide2.QtCore import Qt, QThread, Signal, QEvent, QTimer
from PySide2.QtGui import QImage, QPixmap
from ui_giris import Ui_Dialog
from ui_anasayfa import Ui_MainWindow
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import cv2

class KameraThread(QThread):
    frameCaptured = Signal(QImage)
    cameraClosed = Signal()

    def __init__(self):
        super(KameraThread, self).__init__()
        self.running = False

    def run(self):
        self.capture = cv2.VideoCapture(0)
        self.running = True

        while self.running:
            ret, frame = self.capture.read()
            if ret:
                # BGR'den RGB'ye dönüştür
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = frame.shape
                bytes_per_line = channel * width
                image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
                self.frameCaptured.emit(image)
        
        self.capture.release()
        self.cameraClosed.emit()

    def open_camera(self):
        if not self.isRunning():
            self.start()

    def close_camera(self):
        self.running = False
        self.quit()
        self.wait()

class MyDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setupUi(self)

        # Enter ile Giriş
        self.installEventFilter(self)

        # Giriş butonuna basıldığında yapılacak işlemler
        self.giris_button.clicked.connect(self.giris_yap)
        self.vazgec_button.clicked.connect(self.cikis_yap)

        # Kamera thread'ini başlat
        self.kamera_thread = KameraThread()
        self.kamera_thread.frameCaptured.connect(self.goruntu_goster)
        self.kamera_thread.cameraClosed.connect(self.goruntu_temizle)

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
            self.giris_yap()
            return True
        return super(MyDialog, self).eventFilter(source, event)

    def cikis_yap(self):
        app.exit()

    def giris_yap(self):
        # Kullanıcı adı ve şifreyi al
        kullanici_adi = self.adline.text()
        sifre = self.sifreline.text()

        # Kullanıcı adı ve şifreyi kontrol et (Örnek: Kullanıcı adı 'dogus', şifre 'dogus' ise giriş başarılı)
        if kullanici_adi == 'dogus' and sifre == 'dogus':
            print("Giriş Başarılı")
            self.hide()
            self.anasayfa.show()
        else:
            print("Giriş Başarısız")

    def kamera_ac(self):
        self.kamera_thread.open_camera()

    def goruntu_goster(self, image):
        pixmap = QPixmap.fromImage(image)
        self.camera_info.setPixmap(pixmap)

    def goruntu_temizle(self):
        self.camera_info.clear()

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.camera_button.clicked.connect(self.open_camera)
        self.butonKapat_5.clicked.connect(self.close_camera)
        self.kamera_thread = KameraThread()
        self.kamera_thread.frameCaptured.connect(self.goruntu_goster)
        self.kamera_thread.cameraClosed.connect(self.goruntu_temizle)

        self.buton_ileri.clicked.connect(lambda: self.publish_cmd_vel(0.023, 0.0))
        self.buton_geri.clicked.connect(lambda: self.publish_cmd_vel(-0.0, 0.0))
        self.buton_sag.clicked.connect(lambda: self.publish_cmd_vel(0.0, 0.023))
        self.buton_sol.clicked.connect(lambda: self.publish_cmd_vel(0.0, -0.023))
        self.buton_dur.clicked.connect(lambda: self.publish_cmd_vel(0.0, 0.0))

        rclpy.init(args=None)
        self.node = ROSNode(self.update_linear_info, self.update_angular_info)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ros_spin)
        self.timer.start(100)

    def update_linear_info(self, linear_x):
        self.linear_info.setText(str(linear_x))

    def update_angular_info(self, angular_z):
        self.acisal_hiz_info.setText(str(angular_z))

    def ros_spin(self):
        rclpy.spin_once(self.node, timeout_sec=0.1)

    def closeEvent(self, event):
        self.timer.stop()
        self.node.destroy_node()
        rclpy.shutdown()
        event.accept()

    def open_camera(self):
        self.kamera_thread.open_camera()

    def close_camera(self):
        self.kamera_thread.close_camera()

    def goruntu_goster(self, image):
        pixmap = QPixmap.fromImage(image)
        self.camera_info.setPixmap(pixmap)

    def goruntu_temizle(self):
        self.camera_info.clear()

    def publish_cmd_vel(self, linear_x, angular_z):
        self.node.publish_cmd_vel(linear_x, angular_z)

class ROSNode(Node):
    def __init__(self, linear_callback, angular_callback):
        super().__init__('cmd_vel_listener')
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10
        )
        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)
        self.linear_callback = linear_callback
        self.angular_callback = angular_callback

    def listener_callback(self, msg):
        linear_x = msg.linear.x
        angular_z = msg.angular.z
        self.linear_callback(linear_x)
        self.angular_callback(angular_z)

    def publish_cmd_vel(self, linear_x, angular_z):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        self.publisher.publish(msg)

if __name__ == "__main__":
    app = QApplication([])
    dialog = MyDialog()
    dialog.anasayfa = MyMainWindow()
    dialog.show()
    app.exec_()
