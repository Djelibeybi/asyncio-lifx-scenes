"""Placeholder tests for asyncio_lifx_scenes."""

import pytest
from pytest_httpx import HTTPXMock

from asyncio_lifx_scenes import LifxScenes

from . import LIFX_SCENES


def test_list_scenes(httpx_mock: HTTPXMock) -> None:
    """Test list scenes."""
    httpx_mock.add_response(json=LIFX_SCENES)
    scenes = LifxScenes("token").list_scenes()
    assert len(scenes) == 2


def test_list_scene_forbidden(httpx_mock: HTTPXMock) -> None:
    """Test list scene exception."""
    httpx_mock.add_response(status_code=403, text="403 Forbidden")
    response = LifxScenes("token").list_scenes()
    assert response == []


def test_activate_scene(httpx_mock: HTTPXMock) -> None:
    """Test activate scene."""
    httpx_mock.add_response(json={"results": []})
    scenes = LifxScenes("token").activate_scene("uuid")
    assert scenes == []


def test_activate_scene_fast(httpx_mock: HTTPXMock) -> None:
    """Test activate scene fast."""
    httpx_mock.add_response(json={"results": []})
    scenes = LifxScenes("token").activate_scene("uuid", fast=True)
    assert scenes is None


def test_activate_scene_forbidden(httpx_mock: HTTPXMock) -> None:
    """Test activate scene exception."""
    httpx_mock.add_response(status_code=403, text="403 Forbidden")
    response = LifxScenes("token").activate_scene("uuid")
    assert response == []


@pytest.mark.asyncio
async def test_async_list_scenes(httpx_mock: HTTPXMock) -> None:
    """Test async list scenes."""
    httpx_mock.add_response(json=LIFX_SCENES)
    scenes = await LifxScenes("token").async_list_scenes()
    assert len(scenes) == 2


@pytest.mark.asyncio
async def test_async_list_scene_forbidden(httpx_mock: HTTPXMock) -> None:
    """Test async list scene exception."""
    httpx_mock.add_response(status_code=403, text="403 Forbidden")
    response = await LifxScenes("token").async_list_scenes()
    assert response == []


@pytest.mark.asyncio
async def test_async_activate_scene(httpx_mock: HTTPXMock) -> None:
    """Test async activate scene."""
    httpx_mock.add_response(json={"results": []})
    scenes = await LifxScenes("token").async_activate_scene("uuid")
    assert scenes == []


@pytest.mark.asyncio
async def test_async_activate_scene_no_results(httpx_mock: HTTPXMock) -> None:
    """Test async activate scene fast."""
    httpx_mock.add_response(json={})
    scenes = await LifxScenes("token").async_activate_scene("uuid", fast=True)
    assert scenes is None


@pytest.mark.asyncio
async def test_async_activate_scene_fast(httpx_mock: HTTPXMock) -> None:
    """Test async activate scene fast."""
    httpx_mock.add_response(json={"results": []})
    scenes = await LifxScenes("token").async_activate_scene("uuid", fast=True)
    assert scenes is None


@pytest.mark.asyncio
async def test_async_activate_scene_forbidden(httpx_mock: HTTPXMock) -> None:
    """Test async activate scene exception."""
    httpx_mock.add_response(status_code=403, text="403 Forbidden")
    response = await LifxScenes("token").async_activate_scene("uuid")
    assert response == []
