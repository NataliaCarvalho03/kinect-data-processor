from .constants import *

def get_point_cloud(rgb, depth, P=None, K=None, R=None, T=None):
    cloud = []
    for x in range(depth.shape[0]):
        for y in range(depth.shape[1]):
            X = ((x - KINECT_V1_CX) * depth[x][y]) / KINECT_V1_FX
            Y = ((y - KINECT_V1_CY) * depth[x][y]) / KINECT_V1_FY
            Z = depth[x][y]
            color = rgb[x][y]
            cloud.append([X,Y,Z] + list(color))
    return cloud
        