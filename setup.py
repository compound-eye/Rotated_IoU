from setuptools import setup, Distribution

setup(
    name="bbox_iou",
    version="1.2",
    packages=["bbox_iou"],
    package_data={
        "bbox_iou": [
            "box_intersection_2d.py",
            "min_enclosing_box.py",
            "box_intersection_2d.py",
            "oriented_iou_loss.py",
            "__init__.py",
            "sort_cuda.py",
        ]
    },
    include_package_data=True,
)
