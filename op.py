import bpy
from .data import AddonData


class AssetizeObject(bpy.types.Operator):
    """Marks selected object as an asset and displays it"""

    bl_idname = 'wm.assetize_object'
    bl_label = 'Make asset & display'

    def execute(self, context):
        objects = context.selected_objects
        num_objects = len(objects)
        if num_objects == 0:
            self.report({'INFO'}, 'At least one object needs to be selected to make an asset of it.')
            return {'CANCELLED'}
        elif num_objects > 1:
            self.report({'INFO'}, 'Only one object needs to be selected to make an asset of it.')
            return {'CANCELLED'}
        else:
            curr_obj = AddonData.data['obj']
            if curr_obj is not None and curr_obj.asset_data is not None:
                curr_obj.asset_clear()
            obj = objects[0]
            if obj.asset_data is not None:
                obj.asset_clear()
            obj.asset_mark()
            obj.asset_generate_preview()
            AddonData.set_preview_obj(obj)
            AddonData.set_icon_id(obj.preview.icon_id)
            return {'FINISHED'}


class ClearActiveAsset(bpy.types.Operator):
    """Unmarks current asset being displayed"""

    bl_idname = 'wm.unassetize'
    bl_label = 'Clear asset'

    def execute(self, context):
        curr_obj = AddonData.data['obj']
        if curr_obj is not None and curr_obj.asset_data is not None:
            curr_obj.asset_clear()
        AddonData.set_icon_id(None)
        return {'FINISHED'}
