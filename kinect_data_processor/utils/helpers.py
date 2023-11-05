import numpy as np

def get_depth_values(depth_frame: np.array):
    depth_values = []
    for i in range(depth_frame.shape[0]): #line
        for j in range(depth_frame.shape[1]): #column
            d = (depth_frame[i][j] * 2048.0)/255.0
            depth_values.append(d[0])
    mm_depth_frame = np.array(depth_values).reshape(depth_frame.shape[0:2])
    return mm_depth_frame