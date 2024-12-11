from abc import ABC, abstractmethod


class DCCORM(ABC):
    @abstractmethod
    def add_sphere(self, x, y, z, radius) -> str:
        """
        Create a sphere at the given position with the given radius

        Returns:
            str -- The id of the created sphere
        """
        pass

    @abstractmethod
    def add_light(self, x, y, z, intensity) -> str:
        """
        Create a light at the given position with the given intensity

        Returns:
            str -- The id of the created light
        """
        pass

    @abstractmethod
    def add_camera(self, x, y, z, fov) -> str:
        """
        Create a camera at the given position with the given field of view

        Returns:
            str -- The id of the created camera
        """
        pass

    @abstractmethod
    def render(
        self, geometries: list, lights: list, camera: str, output_path: str
    ) -> str:
        """
        Render the scene with the given geometries, lights, and camera

        Returns:
            str -- The id of the rendered image
        """
        pass

    @abstractmethod
    def export_fbx(self, selections, path):
        """
        Export the selected objects to an FBX file at the given path
        """
        pass

    @abstractmethod
    def load_fbx(self, path) -> str:
        """
        Load an FBX file from the given path

        Returns:
            str -- The id of the loaded FBX file
        """
        pass
