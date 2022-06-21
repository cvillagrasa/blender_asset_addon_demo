import bpy
from .data import AddonData
from .op import AssetizeObject, ClearActiveAsset


class VIEW3D_PT_AddonPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = 'objectmode'
    bl_category = 'Asset add-on'
    bl_label = 'Asset custom add-on'

    def draw(self, context):
        if not AddonData.is_loaded:
            AddonData.load()
        layout = self.layout
        row = layout.row()
        row.operator(AssetizeObject.bl_idname)
        icon_id = AddonData.data['icon_id']
        if icon_id is not None:
            row = layout.row()
            row.operator(ClearActiveAsset.bl_idname)
            row = layout.row()
            box = row.box()
            box.template_icon(icon_value=icon_id, scale=5.)
