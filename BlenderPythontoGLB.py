import bpy

# Set the path to the Blender Python script
blender_script = "generated.py"

# Set the output GLB file path
glb_file = "generated.glb"

# Clear existing objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Execute the Blender Python script
exec(compile(open(blender_script).read(), blender_script, 'exec'))

# Export the scene to GLB
bpy.ops.export_scene.gltf(filepath=glb_file, export_format='GLB')

print(f"GLB file saved: {glb_file}")
