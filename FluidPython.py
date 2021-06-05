import bpy

bpy.data.objects['Cube'].select_set(1)
bpy.ops.fluid.free_all()

bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.cache_frame_end = 100

bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.resolution_max = 32


#bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.use_spray_particles = True
#bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.use_foam_particles = True
#bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.use_bubble_particles = True


bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.particle_scale = 2
bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.mesh_scale = 2


bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.cache_type = 'MODULAR'

bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.cache_directory = '//fluid'



#bpy.ops.fluid.bake_data()
#bpy.ops.fluid.bake_particles()
#bpy.ops.fluid.bake_mesh()

bpy.ops.fluid.bake_all()

#bpy.ops.fluid.free_data()
#bpy.ops.fluid.free_mesh()
#bpy.ops.fluid.free_particles()

