from typing import TYPE_CHECKING

import numpy as np
from napari_plugin_engine import napari_hook_implementation
from napari_tools_menu import register_function
import napari


# This is the actual plugin function, where we export our function
# (The functions themselves are defined below)
@napari_hook_implementation
def napari_experimental_provide_function_labels2points():
    return [labels2points]


@register_function(menu="Utilities > Labels to points")
def labels2points(labels_layer: napari.layers.Labels, points_layer: napari.layers.Points, viewer: napari.Viewer):
    # if points_layer is None:
    #     points_layer = viewer.add_points([])
    #     points_layer.mode = 'ADD'
    #     return

    labels = labels_layer.data

    from skimage.measure import regionprops

    props = regionprops(labels)

    centroids = []
    for label_prop in props:
        centroids.append(np.array(label_prop.centroid).astype(np.int))

    points_layer = viewer.add_points(centroids, size=30)