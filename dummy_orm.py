import model

class DummyORM(model.DCCORM):
    def add_sphere(self, x, y, z, radius) -> str:
        print(f"Added sphere at ({x}, {y}, {z}) with radius {radius}")
        return "sphere"
    
    def add_light(self, x, y, z, intensity) -> str:
        print(f"Added light at ({x}, {y}, {z}) with intensity {intensity}")
        return "light"
    
    def add_camera(self, x, y, z, fov):
        print(f"Added camera at ({x}, {y}, {z}) with fov {fov}")
        return "camera"
    
    def render(self, geometries, lights, camera, output_path: str) -> str:
        print(f"Rendered scene with {len(geometries)} geometries, {len(lights)} lights, and camera {camera} to {output_path}")
        return "image"
    
    def export_fbx(self, selections, path):
        print(f"Exported {len(selections)} selections to FBX file at {path}")
    