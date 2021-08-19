import urllib.request

import cv2
import numpy as np

image_url = 'http://192.168.0.24:7079/hi'
while True:
    resp = urllib.request.urlopen(image_url)
    nparr = np.frombuffer(resp.read(), np.byte)
    image_raw = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    cv2.imshow("output", image_raw)
