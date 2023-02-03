import cv2
import os.path
from hr import HR
from utils import compute_sim, project_dir, crop_face

PROJECT_DIR = project_dir()


def test_embedding_from_face_crop():
    """
    To test to get face embeddings in 512-d numerical vectors obtained from
    cropped and then resized face:
        - loads 3 .jpg images according to the given path
        - via detection method get the list of face's bbox and kps
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

    #### person A
    img1 = cv2.imread(img1_path)

    # get face bbox and crop, kps from detection method
    detection = hr.detection(img1)

    # get crop and kps from loc img
    crop_img, adjusted_kps = crop_face(img1, detection[0][1], detection[0][0])

    # get embedding
    feat_1_person = hr.get_embedding_from_face_crop(crop_img, adjusted_kps)
    feat_1_person = feat_1_person[1]

    #### person A
    img2 = cv2.imread(img2_path)

    # get face bbox and crop, kps from detection method
    detection = hr.detection(img2)

    # get crop and kps from loc img
    crop_img, adjusted_kps = crop_face(img2, detection[0][1], detection[0][0])

    # get embedding
    feat_2_person = hr.get_embedding_from_face_crop(crop_img, adjusted_kps)
    feat_2_person = feat_2_person[1]

    # person B
    img3 = cv2.imread(img3_path)

    # get face bbox and crop, kps from detection method
    detection = hr.detection(img3)

    # get crop and kps from loc img
    crop_img, adjusted_kps = crop_face(img3, detection[0][1], detection[0][0])

    # get embedding
    feat_3_person = hr.get_embedding_from_face_crop(crop_img, adjusted_kps)
    feat_3_person = feat_3_person[1]

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
