from PySide2.QtWidgets import QApplication, QDialog, QMainWindow
from PySide2.QtCore import Qt, QThread, Signal, QEvent
from PySide2.QtGui import QImage, QPixmap
from ui_giris import Ui_Dialog
from ui_anasayfa import Ui_MainWindow
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

    def open_camera(self):
        self.kamera_thread.open_camera()

    def close_camera(self):
        self.kamera_thread.close_camera()

    def goruntu_goster(self, image):
        pixmap = QPixmap.fromImage(image)
        self.camera_info.setPixmap(pixmap)

    def goruntu_temizle(self):
        self.camera_info.clear()

if __name__ == "__main__":
    app = QApplication([])
    dialog = MyDialog()
    dialog.anasayfa = MyMainWindow()
    dialog.show()
    app.exec_()
