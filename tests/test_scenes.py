"""Placeholder tests for asyncio_lifx_scenes."""

from asyncio_lifx_scenes import LifxScenes


def test_list_scenes() -> None:
    """Test list scenes."""
    scenes = LifxScenes("token").list_scenes()
    assert scenes == []
