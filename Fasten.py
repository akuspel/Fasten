import bpy

bl_info = {
    "name": "Fasten",
    "description": "",
    "author": "Erk Blender",
    "version": (1, 1),
    "blender": (2, 74, 0),
    "location": "Object properties",
    "warning": "",
    "wiki_url": "",
    "category": "Object" }
    

class FastenPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Fasten"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Fasten!", icon='FORWARD')
        
        row = layout.row()
        row.operator("render.render", text="Render", icon='RENDER_STILL')
        row.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True
        row.operator("sound.mixdown", text="Audio", icon='PLAY_AUDIO')
        
        row = layout.row()
        row.operator("object.shade_smooth", text="Smooth")
        
        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name", icon='OBJECT_DATA')

        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Cube", icon='MESH_CUBE')

        row = layout.row()
        layout.operator("mesh.primitive_plane_add", text="Plane", icon='MESH_PLANE')
        
        row = layout.row()
        layout.operator("mesh.primitive_monkey_add", text="Monkey", icon='MESH_MONKEY')
        
        layout.operator_menu_enum("object.modifier_add", "type")

def register():
    bpy.utils.register_class(FastenPanel)


def unregister():
    bpy.utils.unregister_class(FastenPanel)
    

if __name__ == "__main__":
    register()
