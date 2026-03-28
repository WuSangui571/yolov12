import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from visdrone_to_yolo import convert_visdrone


def test_convert_visdrone_creates_yolo_labels(tmpdir):
    root = Path(str(tmpdir)) / "VisDrone2019"
    split = root / "VisDrone2019-DET-train"
    images_dir = split / "images"
    annotations_dir = split / "annotations"
    images_dir.mkdir(parents=True)
    annotations_dir.mkdir(parents=True)

    Image.new("RGB", (200, 100), color="white").save(images_dir / "000001.jpg")
    (annotations_dir / "000001.txt").write_text(
        "10,20,40,20,1,4,0,0\n0,0,10,10,0,1,0,0\n",
        encoding="utf-8",
    )

    created = convert_visdrone(root)

    label_file = split / "labels" / "000001.txt"
    assert label_file in created
    assert label_file.read_text(encoding="utf-8").strip() == "3 0.150000 0.300000 0.200000 0.200000"


def test_convert_visdrone_supports_multiple_splits(tmpdir):
    root = Path(str(tmpdir)) / "VisDrone2019"
    for split_name in ("VisDrone2019-DET-train", "VisDrone2019-DET-val"):
        split = root / split_name
        (split / "images").mkdir(parents=True)
        (split / "annotations").mkdir(parents=True)
        Image.new("RGB", (50, 50), color="white").save(split / "images" / "sample.jpg")
        (split / "annotations" / "sample.txt").write_text("5,5,10,10,1,1,0,0\n", encoding="utf-8")

    created = convert_visdrone(root)

    assert len(created) == 2
    assert (root / "VisDrone2019-DET-train" / "labels" / "sample.txt").exists()
    assert (root / "VisDrone2019-DET-val" / "labels" / "sample.txt").exists()
