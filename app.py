import argparse
from kinect_data_processor.main_pipeline import start_main_pipeline

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--depth_dir", type=str, help="path for the directory containing the depth frame files.")
parser.add_argument("-r", "--rgb_dir", type=str, help="path for the directory containing the RGB frame files.")
args = parser.parse_args()

start_main_pipeline(args.rgb_dir, args.depth_dir)