import model
from maya import cmds, mel


class MayaOrm(model.DCCORM):
    def add_sphere(self, x, y, z, radius):
        sphere = cmds.polySphere(radius=radius, name="sphere")[0]
        cmds.move(x, y, z, sphere)
        return sphere

    def add_light(self, x, y, z, intensity):
        light = cmds.directionalLight(intensity=intensity, name="light")[0]
        cmds.move(x, y, z, light)
        return light

    def add_camera(self, x, y, z, fov):
        camera = cmds.camera(name="camera")[0]
        cmds.move(x, y, z, camera)
        cmds.setAttr(camera + ".focalLength", fov)
        return camera

    def render(self, geometries, lights, camera, output_path):
        cmds.select(geometries + lights + [camera])
        return mel.eval("render")

    def export_fbx(self, selections, path):
        if not cmds.pluginInfo("fbxmaya", q=True, loaded=True):
            cmds.loadPlugin("fbxmaya")
        cmds.select(selections, replace=True)
        cmds.file(
            path, force=True, options="v=0", typ="FBX export", exportSelected=True
        )

    def load_fbx(self, path):
        cmds.file(path, i=True, type="FBX", ignoreVersion=True, ra=True)
        return "fbx_geo"
