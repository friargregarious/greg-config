# pip install PyQt6

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

def main():
    # 1. Create the application instance
    # Every PyQt GUI app must have exactly one instance of QApplication.
    app = QApplication(sys.argv)

    # 2. Create the main window (a QWidget is a basic empty window).
    window = QWidget()
    window.setWindowTitle('My First PyQt App')
    window.setGeometry(100, 100, 400, 200) # (x, y, width, height)

    # 3. Create a label (widget) and set its text
    label = QLabel('Hello World!', window)
    label.move(150, 80) # Move the label to a specific position (x, y)

    # 4. Show the application's GUI.
    window.show()

    # 5. Start the event loop (main loop)
    # The application will wait here until the user closes the window.
    sys.exit(app.exec())

if __name__ == '__main__':
    main()


# Qt provides robust support for Android deployment, and the Qt Sensors module offers a cross-platform C++ and QML interface to access device sensors, which can be leveraged in PyQt applications. 

from PySide6.QtSensors import QAccelerometer

accel = QAccelerometer()
accel.readingChanged.connect(lambda: print(f"X: {accel.reading().x()}"))
accel.start()



# Develop the PyQt application: Use the Qt Sensors module in your PyQt code. This module abstracts the underlying Android sensor framework.
  
# Configure the project: The development environment needs the Android SDK, NDK, and other required tools.
  
# Request permissions: Ensure your application's manifest file includes necessary sensor permissions (e.g., location, camera, etc.), similar to native Android development.

# Deploy the application: Use tools like pyqtdeploy or buildozer to package your Python application into an Android Application Package (APK) and install it on the device. 

# Pydroid 3: This IDE for Android includes built-in support for certain "android" and "android.sensor" modules, making it one of the easiest ways to test Python sensor code on a mobile device.




# Pyqtdeploy: To build a standalone .apk, you can use pyqtdeploy, which supports cross-compilation for Android.




# Android devices provide a wide range of hardware and software-based sensors, categorized primarily by the Android Sensor Framework into three main groups. 

#  1. Motion Sensors 
# These track acceleration forces and rotational forces along three axes. 
#     Accelerometer (Hardware): Measures acceleration force in \(m/s^{2}\) on three physical axes (\(x,y,z\)), including gravity.
#     Gyroscope (Hardware): Measures the rate of rotation in \(rad/s\) around the \(x,y,\) and \(z\) axes.
#     Gravity Sensor (Software/Hardware): Measures the force of gravity applied to the device on three axes.
#     Linear Acceleration (Software/Hardware): Measures acceleration force along three axes, excluding the force of gravity.
#     Rotation Vector (Software/Hardware): Measures device orientation by providing three elements of the rotation vector.
#     Step Counter & Detector: Tracks the number of steps taken since the last reboot and detects individual step events. 

# 2. Environmental Sensors These monitor ambient conditions such as air temperature, pressure, and humidity. 
#     Light Sensor (Hardware): Measures ambient light levels (illuminance) in lux. 
#     Barometer/Pressure Sensor (Hardware): Measures ambient air pressure (hPa/mbar). 
#     Ambient Temperature (Hardware): Measures the ambient room temperature in °C. 
#     Relative Humidity (Hardware): Measures relative ambient humidity as a percentage.  

# 3. Position Sensors These determine the device's physical position in the world's frame of reference.  
#     Magnetometer/Magnetic Field (Hardware): Measures the ambient geomagnetic field in \(\mu T\) along three axes. 
#     Proximity Sensor (Hardware): Measures the distance of an object relative to the screen (typically used to detect a face during a call). 
#     Orientation (Software - Deprecated): Measures degrees of rotation; replaced by newer methods using gravity and magnetic field sensors. 

 
# 4. Other Hardware & Data Interfaces While not always managed by the standard "Sensor Framework," these are accessible through dedicated Android APIs:  
#     GPS/GNSS: Provides geographical location (latitude, longitude) and altitude. 
#     Cameras: Image sensors for capturing photos and video. 
#     Microphone: Captures audio data and measures sound levels. 
#     Biometrics: Fingerprint scanners and iris/facial recognition sensors. 
#     Connectivity Hardware: Bluetooth, NFC, Wi-Fi, and 5G/LTE modules. 
#     Hall Sensor: Detects magnetic fields, often used with smart flip covers. 
#     Health Sensors: Heart rate monitors and \(SpO_{2}\) (pulse oximetry) sensors on specialized devices. 

# Are you planning to build an app that combines multiple sensors, such as using the accelerometer and magnetometer for a custom compass?

https://www.google.com/search?q=using+pyqt+to+access+android+mobile+sensors&sca_esv=a5908d9afcf34126&rlz=1C1GCEA_enCA1173CA1173&sxsrf=ANbL-n7aYfx6EsgZy6yAU4iaJScUn85pKw%3A1769713427067&ei=E697affbA7-l5NoP5J2Q6AM&ved=2ahUKEwiP5eS2ubGSAxUtM1kFHd7kCRMQ0NsOegQIAxAB&uact=5&sclient=gws-wiz-serp&udm=50&fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpmAsnXCN5UBx17opt8eaTX5MJRoosnbembaWTjeNSquLeqRCxXBRGAkdJJ_SEV_4VZIQOaNPzfEm0o8TAIGA3dgI3f-MteWchEVNW4zC-tefNBs4jDRpFpqk4-rYVry17OJlfjEMXkf7MzLTN5j__R4X4kIW5WqXLG8UcDFvltmx_V7r9d0G1_QSrkW7XSmJyb1NC1Q&aep=10&ntc=1&mtid=1LB7ac27G5XZ5NoPjp7oyQU&mstk=AUtExfCnn3YE6S_9TYnQ8xOUzPC2HHgGATm3eMV1t_lZBYyFCihdNUHp_RvRdtg4X5wz6iMtIlta0J-D6B1B9HxyWIZk-dEmxlCoRNkEJ3kpL_jjDjiK-jGRjTUU8vO-Lihn7KPWk6yQWt-7uivYfRNop8kxKkce4vbf8mh0g9p4unoZZnYrdjsy6Gu5hQVRfBOjGo75T8RgeGb9r85rhhsxDs3eelJ4p8pyGvputi5FxqhLhYGnAWfgDXbGjB20HaCjyV7dUv2bqCD5pyH7Vk0sOYY5g9pbqf6sJDo9HZJxUZibX4UaK1b1KhpzhMfOfZTu18N4A4GFIHXF1bnYf1ViTmzZFERMYSIrMN9Iww22uRIIxrWL5o_VW94jDOgC5DKEJ65zxJaG19sh&csuir=1

https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview
https://doc.qt.io/qtforpython-6/PySide6/QtPositioning/QGeoPositionInfoSource.html
https://doc.qt.io/qtforpython-6/PySide6/QtSensors/QMagnetometer.html


#######################################################

# To acquire data from these sensors you first create an instance of the SensorManager class, which you can use to get an instance of a physical sensor. Then you register a sensor listener in the onResume() method, and start handling incoming sensor data in the onSensorChanged() callback method. The following code shows you how to do this:


from PyQt6.QtSensors import QSensor
from PyQt6.QtCore import QCoreApplication
import sys

# Necessary for Qt to initialize properly
app = QCoreApplication(sys.argv)

# Get all available sensor types
print("Available Sensors:")
for sensor_type in QSensor.sensorTypes():
    print(f"- {sensor_type}")

# Optional: Get specific info about a sensor type
# print(QSensor.defaultSensorForType("QAccelerometer"))


https://doc.qt.io/qtforpython-6/overviews/qtsensors-cpp.html


# for controlling a robot from my cell phone
# A. Mobile App (PyQt6)
# You need pyserial and pybluez (or just pyserial if the phone pairs it as a serial port). 

import sys
import serial
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

class RobotControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robot Control")
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Click buttons to control robot")
        self.layout.addWidget(self.label)
        
        self.btn_forward = QPushButton("Forward")
        self.btn_forward.pressed.connect(lambda: self.send_command('F'))
        self.btn_forward.released.connect(lambda: self.send_command('S')) # Stop
        self.layout.addWidget(self.btn_forward)
        
        self.setLayout(self.layout)
        
        # Connect to Bluetooth module (Update with your HC-05 MAC address/COM port)
        # On Android, you might need to use rfcomm to map it first
        try:
            self.ser = serial.Serial('/dev/rfcomm0', 9600, timeout=1) # Example for Linux/Android
        except Exception as e:
            self.label.setText(f"Error: {e}")

    def send_command(self, command):
        if self.ser.is_open:
            self.ser.write(command.encode())
            print(f"Sent: {command}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RobotControlApp()
    window.show()
    sys.exit(app.exec())

# B. Robot Side (Arduino Example) ###########################################

void setup() {
  Serial.begin(9600); // Bluetooth modulebaud rate
  pinMode(13, OUTPUT); // Example motor pin
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'F') {
      digitalWrite(13, HIGH); // Move forward
    } else if (command == 'S') {
      digitalWrite(13, LOW); // Stop
    }
  }
}


# 3. Alternative: Wi-Fi (Sockets) 
# If you need higher speed and both devices are on the same network:
# Python Server on Robot (Raspberry Pi):

import socket

def start_server():
    host = '0.0.0.0' # Listen on all interfaces
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print("Waiting for connection...")
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024).decode()
        if not data: break
        print(f"Received: {data}") # Process motor commands here
    conn.close()


# PyQt6 Client on Phone:

import socket
# Inside your button handler:
def send_wifi_cmd(cmd):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.x.x', 12345)) # Robot IP
    client.send(cmd.encode())
    client.close()



# Key Considerations for Mobile
#     Permissions: Ensure your final APK has Bluetooth/Internet permissions.
#     Threading: Use QThread in PyQt6 to send commands so your UI does not freeze.
#     Pairing: For Bluetooth, the phone must be paired with the HC-05 before running the app. 
