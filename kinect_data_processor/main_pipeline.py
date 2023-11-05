from .utils.read_data import read_frame_files, write_point_cloud
from .utils.helpers import get_depth_values
from .utils.point_cloud_estimator import get_point_cloud


def start_main_pipeline(rgb_dir_path: str, depth_dir_path: str):
    depth = read_frame_files(depth_dir_path)
    rgb = read_frame_files(rgb_dir_path)
    mm_depth = []
    for d in depth:
        mm_depth.append(get_depth_values(d))
    pc = []
    for i in range(len(mm_depth)):
        sub_cloud = get_point_cloud(rgb[i], mm_depth[i])
        for p in sub_cloud:
            pc.append(p)
    print(f"{len(pc)} points calculated... Writing")
    write_point_cloud(pc, ".")