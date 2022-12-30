import cv2
from src.hr import HR

hr = HR()

for img_path in imgs_path:
    img = cv2.imread(img_path)
    det_data = hr.detection(img)
 
    for data in det_data:
        bbox, kps, _shape = data
        x1 = int(bbox[0])
        y1 = int(bbox[1])
        x2 = int(bbox[2])
        y2 = int(bbox[3])
        # draw bbox
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        # draw kps 
        # please put here
    filename = ...
    cv2.imwrite(filename, img)
