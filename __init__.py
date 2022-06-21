import bpy

bl_info = {
        'name': 'Asset add-on test',
        'author': 'Carlos Villagrasa',
        'version': (0, 0, 1),
        'blender': (3, 0, 0),
        'location': '3d viewport toolbar (N), under the custom asset tab.',
        'category': 'Scene',
        'description': 'Asset add-on test',
        'tracker_url': '',
        'warning': '',
    }


from .ui import VIEW3D_PT_AddonPanel
from .op import AssetizeObject, ClearActiveAsset


classes = [AssetizeObject,  ClearActiveAsset, VIEW3D_PT_AddonPanel]
props = {}


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    for prop_name, prop_value in props.items():
        setattr(bpy.types.Scene, prop_name, prop_value)


def unregister():
    for prop_name in props.keys():
        delattr(bpy.types.Scene, prop_name)

    for cls in classes:
        bpy.utils.unregister_class(cls)
