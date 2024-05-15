import pytest
from pixel_chef import Tile

class TestTile:
    def test_transform_cartesian_to_isometric(self):
        tile = Tile(0, 0, None)
        cartesian_coordinates = (2, 0)
        expected_isometric_coordinates = (2, 0)
        assert tile.transform_cartesian_to_isometric(cartesian_coordinates) == expected_isometric_coordinates

    def test_transform_cartesian_to_isometric_negative_coordinates(self):
        tile = Tile(0, 0, None)
        cartesian_coordinates = (-3, 0)
        expected_isometric_coordinates = (-3, 0)
        assert tile.transform_cartesian_to_isometric(cartesian_coordinates) == expected_isometric_coordinates

    def test_transform_cartesian_to_isometric_zero_coordinates(self):
        tile = Tile(0, 0, None)
        cartesian_coordinates = (0, 0)
        expected_isometric_coordinates = (0, 0)
        assert tile.transform_cartesian_to_isometric(cartesian_coordinates) == expected_isometric_coordinates

    def test_transform_cartesian_to_isometric_large_coordinates(self):
        tile = Tile(0, 0, None)
        cartesian_coordinates = (1000, 0)
        expected_isometric_coordinates = (1000, 0)
        assert tile.transform_cartesian_to_isometric(cartesian_coordinates) == expected_isometric_coordinates

    def test_transform_cartesian_to_isometric_extreme_large_coordinates(self):
        tile = Tile(0, 0, None)
        cartesian_coordinates = (1000000, 0)
        expected_isometric_coordinates = (1000000, 0)
        assert tile.transform_cartesian_to_isometric(cartesian_coordinates) == expected_isometric_coordinates