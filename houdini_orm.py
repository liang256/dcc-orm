import model
import hou


class HouiniOrm(model.DCCORM):
    def load_fbx(self, path):
        fbx_node = hou.node("/obj").createNode("geo", "imported_fbx")
        fbx_node.setName("fbx_geo", unique_name=True)
        fbx_import = fbx_node.createNode("file", "fbx_file")
        fbx_import.parm("file").set(path)
        return fbx_node.path()

    def add_camera(self, x, y, z, fov):
        camera = hou.node("/obj").createNode("cam", "camera")
        camera.parmTuple("t").set((x, y, z))
        camera.parm("focal").set(fov)
        return camera.path()

    def add_light(self, x, y, z, intensity):
        light = hou.node("/obj").createNode("hlight", "light")
        light.parmTuple("t").set((x, y, z))
        light.parm("light_intensity").set(intensity)
        return light.path()

    def add_sphere(self, x, y, z, radius):
        sphere = hou.node("/obj").createNode("geo", "sphere")
        sphere.parmTuple("t").set((x, y, z))
        sphere.parm("scale").set(radius)
        return sphere.path()

    def render(self, geometries, lights, camera, output_path):
        mantra_node = hou.node("/out").createNode("ifd", "mantra")
        mantra_node.parm("vm_picture").set(output_path)
        mantra_node.parm("camera").set(camera)
        mantra_node.render()
        print(
            f"Rendered scene with {len(geometries)} geometries, {len(lights)} lights, and camera {camera}"
        )
