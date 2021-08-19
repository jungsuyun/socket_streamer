import urllib.request
import io
import cv2
import numpy as np

img_url = 'http://192.168.0.2:7079/hi'
while True:
    data = urllib.request.urlopen(img_url)
    raw_data = data.read()

    nparr = np.frombuffer(raw_data, np.byte)
    image_raw = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
    cv2.imshow("test", image_raw)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()