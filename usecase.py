import framework

dcc = framework.get_dcc()
sphere = dcc.add_sphere(0, 0, 0, 1)
light = dcc.add_light(1, 1, 1, 1)
camera = dcc.add_camera(2, 2, 2, 90)
dcc.render(geometries=[sphere], lights=[light], camera=camera)
dcc.export_fbx(selections=[sphere], path="scene.fbx")