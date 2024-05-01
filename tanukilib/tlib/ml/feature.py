import keras.applications as kerasapp
from keras.models import Model
from typing import Tuple
from tlib.math.math import Coordinate, cosaine_similarity2d
import numpy as np
from math import isnan


def build_resnet152_for_feature_extaction() -> Model:
    """Build RESNET152 in suitable config for feature extraction"""

    m: Model = kerasapp.ResNet152(
        include_top=False,
        weights="imagenet",
        input_tensor=None,
        input_shape=None,
        pooling="avg",
        classes=1000
    )
    return m


def build_resnet152V2_for_feature_extaction() -> Model:
    """Build RESNET152 V2 in suitable config for feature extraction"""

    m: Model = kerasapp.ResNet152V2(
        include_top=False,
        weights="imagenet",
        input_tensor=None,
        input_shape=None,
        pooling="avg",
        classes=1000
    )
    return m


class FeatureSearchEngine:
    """Search engine by features using Cosine similarity"""

    def __init__(self, features):
        self.features = features

    def search_by_cos_similarty(
            self,
            q_vec: Tuple[float, float],
            pick_top_n: int = 5
    ):
        """Search feature by cosine similarity and return N cases order by similarity score"""
        simrank = []
        q_coord = Coordinate(q_vec[0], q_vec[1])
        for v in self.features:
            v_coord = Coordinate(v[0], v[1])
            cos_sim = cosaine_similarity2d(q_coord, v_coord)
            if not isnan(cos_sim):
                simrank.append(cos_sim)
        simrank = np.array(simrank)

        # -pick_top_n gives desc sorted list
        index_part = np.argpartition(simrank, -pick_top_n)[-pick_top_n:]
        indices = index_part[np.argsort(simrank[index_part])][::-1]
        return indices, simrank[indices]
