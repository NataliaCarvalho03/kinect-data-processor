# kinect-data-processor

This project estimate a point cloud by processing xbox 360 kinect sensor data.

This is a early development project, created for educational purposes. Use it at your own risk.

## Data Organization

Clone the project, install the requirements. The RGB and depth frames must be stored in separated directories and must have standard names. Example:

```
----depth-frames
    ----depth-1.png
    ----depth-2.png

----rgb-frames
    ----rgb-1.png
    ----rgb-2.png
```

Observed that depth-1.png is related to rgb-1.png.

## Running the software

Once you have your RBG and depth images organized, use the following command:

```
python app.py -r "../basic_kinect/rgb" -d "../basic_kinect/depth"
```

The arguments are:

- ```-r``` is the path for the directory containing the RGB frames;
- ```-d``` is the path for the directory containing the depth frames;