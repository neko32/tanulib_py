import fiftyone as fo
import fiftyone.types as fotypes
import fiftyone.utils.cvat as focvat

class Viewer:
    """View images with/without annotations on FiftyOne app"""

    def __init__(self, src_path:str, dataset_name:str):
        self.src_path = src_path
        self.dataset_name = dataset_name

    def start_as_plain_img_viewer(self) -> None:
        """Create a session and start FiftyOne as a plain image viewer"""
        
        self.datasets = fo.Dataset.from_images_dir(self.src_path)
        self._session = fo.launch_app(self.datasets)

    def start_as_cvat_annotated_viewer(self) -> None:
        """Create a session and start FiftyOne as a viewer for CVAT image annotation"""

        # NOTE!!! Export from CVAT's label xml is annotations.xml
        # But FO assumes as labels.xml
        # also CVAT export put data under image but FO assumes data
        #print(fo.config)
        self.datasets = fo.Dataset.from_dir(
            dataset_dir=self.src_path,
            data_path="images",
            dataset_type=fotypes.CVATImageDataset,
            name=self.dataset_name,
            labels_path='annotations.xml'
        )
        #print(self.datasets.head())
        
        self._session = fo.launch_app(self.datasets)

    def wait(self) -> None:
        """wait till fiftyone app is closed"""
        self._session.wait()

