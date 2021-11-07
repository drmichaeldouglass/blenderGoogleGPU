#Bake Blender Fluids on Google Colab
#Created by microSingularity

https://www.youtube.com/c/MicroSingularity


import bpy

#Change Fluid Domain Type: Can be "GAS" or "LIQUID". Domain needs to be changed to name of fluid domain object.
bpy.data.objects["Domain"].modifiers["Fluid"].domain_settings.domain_type = 'LIQUID'

#Change Output Directory of Fluid Cache: "//test" means render in folder called "test" which is in the same folder as blender file
bpy.data.objects["Domain"].modifiers["Fluid"].domain_settings.cache_directory = "//test"

#Change Cache Type
bpy.data.objects["Domain"].modifiers["Fluid"].domain_settings.cache_type = 'ALL'

#Bake all Fluid Simulations in the scene
bpy.ops.fluid.bake_all()

#Free all Fluid Simulations in the scene
bpy.ops.fluid.free_all()



#Some other useful commands:
############################

#Select Domain
#bpy.data.objects['Domain'].select_set(1)


#Change Cache End Frame
#bpy.data.objects['Domain'].modifiers["Fluid"].domain_settings.cache_frame_end = 100
#Change Domain Resolution
#bpy.data.objects['Domain'].modifiers["Fluid"].domain_settings.resolution_max = 32

#Enable Particles, Foam and Bubbles
#bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.use_spray_particles = True
#bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.use_foam_particles = True
#bpy.data.objects['Cube'].modifiers["Fluid"].domain_settings.use_bubble_particles = True


#Change Mesh and Particle Scale
#bpy.data.objects['Domain'].modifiers["Fluid"].domain_settings.particle_scale = 2
#bpy.data.objects['Domain'].modifiers["Fluid"].domain_settings.mesh_scale = 2


#Bake Individual Elements
#bpy.ops.fluid.bake_data()
#bpy.ops.fluid.bake_particles()
#bpy.ops.fluid.bake_mesh()

#Bake All
#bpy.ops.fluid.bake_all()

#Free Individual Elements
#bpy.ops.fluid.free_data()
#bpy.ops.fluid.free_mesh()
#bpy.ops.fluid.free_particles()

