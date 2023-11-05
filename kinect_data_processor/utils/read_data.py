import cv2, glob, os


def read_frame_files(images_dir: str):
    frames = []
    path = os.path.join(images_dir, "*.png")
    frame_paths = glob.glob(path)
    for p in frame_paths:
        frames.append(cv2.imread(p))
    return frames


def write_point_cloud(points: list, file_path: str, file_name="point_cloud.txt"):
    path = os.path.join(file_path, file_name)
    file = open(path, "w")
    for p in points:
        file.write(f"{p[0]} {p[1]} {p[2]} {p[3]} {p[4]} {p[5]}\n")
    file.close()