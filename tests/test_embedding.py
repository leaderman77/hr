import cv2
import numpy as np
from src.hr import HR

def test_embedding():
    """
    To test to get face embeddings in 512-d numerical vectors obtained from a defined face:
         - loads 3 .jpg images according to the given path
         - Face embedding is obtained for each detected face on each image,
         - Compare defined face embeddings. Picture_1 and picture_2 are
           images of the same person. picture_3 is an image of third person.
           In comparision, picture_1 and picture_2 should be close to each other
           but different from picture_3.
    """
    hr = HR()
    img1_path = "../data/drive/rasmlar_kirish/1_1_1_2022-10-09-17-32-26.jpg"
    img2_path = "../data/drive/rasmlar_chiqish/1_1_1_2022-10-09-17-38-10.jpg"
    img3_path = "../data/s3/merchant_1/location_1/camera_1/2022-11-02/2022-11-02 18_59_59.jpg"


    img1 = cv2.imread(img1_path)
    feat_1_ruzmat = hr.embeding(img1)
    feat_1_ruzmat = feat_1_ruzmat[0][0].embedding

    img2 = cv2.imread(img2_path)
    feat_2_ruzmat = hr.embeding(img2)
    feat_2_ruzmat = feat_2_ruzmat[0][0].embedding

    img3 = cv2.imread(img3_path)
    feat_3_samariddin = hr.embeding(img3)
    feat_3_samariddin = feat_3_samariddin[0][0].embedding

    sim_same = compute_sim(feat_1_ruzmat, feat_2_ruzmat)
    sim_diff = compute_sim(feat_1_ruzmat, feat_3_samariddin)

    assert sim_same > sim_diff

    if sim_same > sim_diff:
        print("Correct")
        print("{} > {}".format(sim_same, sim_diff))
    else:
        print("Incorrect")
        print("{} > {}".format(sim_same, sim_diff))


def compute_sim(feat1, feat2):
    from numpy.linalg import norm
    feat1 = feat1.ravel()
    feat2 = feat2.ravel()
    sim = np.dot(feat1, feat2) / (norm(feat1) * norm(feat2))
    return sim