from tlib.ml.img import load_images_from_dir
from tlib.ml.dataset import derive_path_for_dataset, show_multiple_images_as_rank
# from tlib.ml.dataset import derive_path_for_dataset, show_NDArray_image
from tlib.ml.feature import (
    build_resnet152V2_for_feature_extaction,
    FeatureSearchEngine
)
from tlib.ml.base import RESNET_DATA_SIZE
from pathlib import Path
from keras.applications.resnet import preprocess_input


def main():

    search_id = 0
    landscape_data = str(Path("arnaud_landscape_pictures").joinpath("archive"))
    data_path = derive_path_for_dataset(landscape_data, None)
    print("loading images..")
    img_paths, imgs = load_images_from_dir(
        data_path, RESNET_DATA_SIZE, max_num_to_load=None)
    print(f"loading images done. total {len(imgs)}")
    # show_NDArray_image(imgs[0])
    m = build_resnet152V2_for_feature_extaction()
    m.summary()

    preprocessed = preprocess_input(imgs)
    features = m.predict(preprocessed)
    fsearch = FeatureSearchEngine(features)
    print(f"searching by {search_id}..")
    rez, sim_scores = fsearch.search_by_cos_similarty(features[search_id])

    show_multiple_images_as_rank(
        rez,
        sim_scores,
        img_paths,
        RESNET_DATA_SIZE
    )

    print("done.")


if __name__ == "__main__":
    main()
