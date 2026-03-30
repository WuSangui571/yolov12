import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from hrsc2016_ms_to_yolo import convert_hrsc2016_ms


def test_convert_hrsc2016_ms_creates_split_dirs_and_labels(tmpdir):
    root = Path(str(tmpdir)) / "HRSC2016-MS"
    (root / "AllImages").mkdir(parents=True)
    (root / "Annotations").mkdir()
    (root / "ImageSets").mkdir()

    (root / "AllImages" / "1001.bmp").write_bytes(b"BMstub")
    (root / "Annotations" / "1001.xml").write_text(
        """<annotation>
<size><width>200</width><height>100</height><depth>3</depth></size>
<object><difficult>0</difficult><bndbox><xmin>10</xmin><ymin>20</ymin><xmax>50</xmax><ymax>40</ymax></bndbox></object>
</annotation>""",
        encoding="utf-8",
    )
    for split in ("train", "val", "test"):
        (root / "ImageSets" / f"{split}.txt").write_text("1001\n", encoding="utf-8")

    summary = convert_hrsc2016_ms(root)

    assert summary == {"train": 1, "val": 1, "test": 1}
    assert (root / "images" / "train" / "1001.bmp").exists()
    assert (root / "labels" / "train" / "1001.txt").read_text(encoding="utf-8").strip() == "0 0.150000 0.300000 0.200000 0.200000"


def test_convert_hrsc2016_ms_writes_empty_labels_for_backgrounds(tmpdir):
    root = Path(str(tmpdir)) / "HRSC2016-MS"
    (root / "AllImages").mkdir(parents=True)
    (root / "Annotations").mkdir()
    (root / "ImageSets").mkdir()

    (root / "AllImages" / "2001.bmp").write_bytes(b"BMstub")
    (root / "Annotations" / "2001.xml").write_text(
        """<annotation>
<size><width>200</width><height>100</height><depth>3</depth></size>
</annotation>""",
        encoding="utf-8",
    )
    for split in ("train", "val", "test"):
        (root / "ImageSets" / f"{split}.txt").write_text("2001\n", encoding="utf-8")

    convert_hrsc2016_ms(root)

    assert (root / "labels" / "test" / "2001.txt").read_text(encoding="utf-8") == ""
