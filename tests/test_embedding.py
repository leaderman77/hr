import cv2
from src.hr import HR
import numpy as np

def test_embedding():
    """
    Aniqlashngan yuzdan vektor korinishidagi embedding olinishini test qilish:
        - berilgan path bo'yicha 3ta .jpg rasmlarni load qiladi
        - Har bir rasm boyicha xar bir yuz uchun yuz embedding olinadi,
        - Toplangan embeddinglarni solishtiramiza. Bunda rasm_1 va rasm_2 bitta odam va
          embedding solishtirsak ular yaqin bo'lish kerak rasm_3 ga nisbatan.
    """
    hr = HR()
    img1_path = "../data/drive/rasmlar_kirish/1_1_1_2022-10-09-17-32-26.jpg"
    img2_path = "../data/drive/rasmlar_chiqish/1_1_1_2022-10-09-17-38-10.jpg"
    img3_path = "../data/s3/merchant_1/location_1/camera_1/2022-11-02/2022-11-02 18_59_59.jpg"
    imgPath_list = [img1_path, img2_path, img3_path]

    output_img_list = []

    for img_path in imgPath_list:
        img = cv2.imread(img_path)
        embedding_data = hr.embeding(img)
        output_img_list.append(embedding_data[0])
    print(output_img_list)


    img1 = cv2.imread(img1_path)
    feat1 = hr.embeding(img1)
    feat1 = feat1[0]

    img2 = cv2.imread(img2_path)
    feat2 = hr.embeding(img2)
    feat2 = feat2[0]

    img3 = cv2.imread(img3_path)
    feat3 = hr.embeding(img3)
    feat3 = feat3[0]

    sim = compute_sim(feat2, feat3)
    if sim < 0.2:
        conclu = 'They are NOT the same person'
    elif sim >= 0.2 and sim < 0.28:
        conclu = 'They are LIKELY TO be the same person'
    else:
        conclu = 'They ARE the same person'
    print(sim)
    print(conclu)


def compute_sim(feat1, feat2):
    from numpy.linalg import norm
    feat1 = feat1.ravel()
    feat2 = feat2.ravel()
    sim = np.dot(feat1, feat2) / (norm(feat1) * norm(feat2))
    return sim