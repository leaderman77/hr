import cv2
import os.path
from hr import HR
from utils import compute_sim
from utils import project_dir

PROJECT_DIR = project_dir()


def test_resized_crop_embedding():
    """
    To test to get face embeddings in 512-d numerical vectors obtained from
    cropped and then resized face:
        - loads 3 .jpg images according to the given path
        - get faces, each face's bbox and kps
        - crop face and calculate kps according to this cropped img
        - resize cropped face img as well as crop kps
        - face embedding is obtained for each resized face on each image,
        - Compare defined face embeddings. Picture_1 and picture_2 are
          images of the same person. picture_3 is an image of third person.
          In comparision, picture_1 and picture_2 should be close to each other
          but different from picture_3.
    """
    hr = HR()
    root_emb_data = os.path.join(PROJECT_DIR, "tests", "embedding")
    img1_path = os.path.join(root_emb_data, "1_1_1_2022-10-09-17-32-26.jpg")
    img2_path = os.path.join(root_emb_data, "1_1_1_2022-10-09-17-38-10.jpg")
    img3_path = os.path.join(root_emb_data, "2022-11-02 18_59_59.jpg")

    # person A
    img1 = cv2.imread(img1_path)
    feat_1_person = hr.get_embedding_by_crop_img(img1)
    feat_1_person = feat_1_person[0][2]

    # person A
    img2 = cv2.imread(img2_path)
    feat_2_person = hr.get_embedding_by_crop_img(img2)
    feat_2_person = feat_2_person[0][2]

    # person B
    img3 = cv2.imread(img3_path)
    feat_3_person = hr.get_embedding_by_crop_img(img3)
    feat_3_person = feat_3_person[0][2]

    sim_same_crp = compute_sim(feat_1_person, feat_2_person)
    sim_diff_crp = compute_sim(feat_1_person, feat_3_person)

    print("Sim Same Crop: ", sim_same_crp)
    print("Sim Diff Crop: ", sim_diff_crp)

    assert sim_same_crp > sim_diff_crp

    if sim_same_crp > sim_diff_crp:
        print("Correct")
        print("{} > {}".format(sim_same_crp, sim_diff_crp))
    else:
        print("Incorrect")
        print("{} > {}".format(sim_same_crp, sim_diff_crp))
