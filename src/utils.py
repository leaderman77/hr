import numpy as np


def compute_sim(feat1, feat2):
    """Function to compute cosine similarity between two embedding vectors

    Parameters
    ----------
    feat1 : :obj:`Array`
        The first parameter. Vector
    feat2 : :obj:`Array`
        The second parameter. Vector

    Returns
    -------
    The method returns similarity score in float32 data type
    """

    feat1 = feat1.ravel()
    feat2 = feat2.ravel()
    sim = np.dot(feat1, feat2) / (np.linalg.norm(feat1) * np.linalg.norm(feat2))

    return sim
