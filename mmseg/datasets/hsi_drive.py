from .builder import DATASETS
from .custom import CustomDataset

classes_exp2 = ('Unlabelled', 'Road', 'RoadMarks', 'Vegetation', 'Sky', 'NoDrivable')
palette_exp2 = [[128, 128, 128], [129, 127, 38], [120, 69, 125], [53, 125, 34], [0, 11, 123], [118, 20, 12]]


@DATASETS.register_module()
class HSIDrive20(CustomDataset):
  METAINFO = dict(classes = classes_exp2, palette = palette_exp2)

  CLASSES = classes_exp2

  def __init__(self,
               img_suffix='.npy',
               seg_map_suffix='.png',
               **kwargs) -> None:
    super().__init__(
      img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)