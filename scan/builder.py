# Author: Adam Exley
import logging
import os

import cv2
import numpy as np
import open3d as o3d

from tqdm import tqdm


class Builder():
    def __init__(self) -> None:
        pass

    def source(self, frames, thresh = 50):
        self.data = []

        for idx in tqdm(range(len(frames)),desc="Frames",leave=True,position=0):
        
            locations = np.where(frames[idx] >= thresh)
            values = frames[idx][locations]

            img = np.copy(frames[idx]).astype(float)
            img /= 500
            img[locations] = 1

            cv2.imshow("",img)
            cv2.waitKey(10)
            for subidx in tqdm(range(len(locations[0])),desc="Points",leave=False,position=1):
                # X Y Z V
                self.data.append([locations[0][subidx], locations[1][subidx], idx,values[subidx]])
            
        self.data = np.array(self.data).astype(float)
        self.data[:,3] = (self.data[:,3] - thresh) * (255 / (255 - thresh))

    def build(self):
        logging.info("Building point cloud")
        self.pcd = o3d.geometry.PointCloud()
        self.pcd.points = o3d.utility.Vector3dVector(self.data[:,:3])
        a = cv2.applyColorMap(self.data[:,3].astype(np.uint8),cv2.COLORMAP_BONE)
        self.pcd.colors = o3d.utility.Vector3dVector(a[:,0]/255)

    def save(self, file):
        if not file.endswith('.ply'): file += '.ply'
        o3d.io.write_point_cloud(file, self.pcd)

    def load(self, file):
        if not file.endswith('.ply'): file += '.ply'
        self.pcd = o3d.io.read_point_cloud(file)

    def show(self):
        o3d.visualization.draw_geometries([self.pcd])

    def voxel(self, size = 0.5):
        self.vox = o3d.geometry.VoxelGrid.create_from_point_cloud(self.pcd,voxel_size=size)
        o3d.visualization.draw_geometries([self.vox])