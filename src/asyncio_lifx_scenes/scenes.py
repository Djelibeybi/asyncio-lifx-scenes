"""Main module."""

from __future__ import annotations

import logging
from typing import Any

import httpx
from httpx_auth import HeaderApiKey

from .models import LifxScene

_LOGGER = logging.getLogger(__name__)

LIFX_URL = "https://api.lifx.com/v1/scenes"
TIMEOUT = 3.0


class LifxScenes:
    """Class to represent LIFX scenes."""

    def __init__(self, token: str) -> None:
        """Initialize the LIFX scene."""
        self.scenes: list[LifxScene] = []
        self._auth_token = HeaderApiKey(f"Bearer {token}", header_name="Authorization")

    def list_scenes(self) -> list[LifxScene]:
        """Return a list of scenes stored on LIFX Cloud."""
        header = {"accept": "application/json"}
        with httpx.Client(auth=self._auth_token, timeout=TIMEOUT) as client:
            resp = client.get(LIFX_URL, headers=header)
            try:
                resp.raise_for_status()
                for scene in resp.json():
                    self.scenes.append(LifxScene(**scene))
            except httpx.HTTPStatusError as exc:
                _LOGGER.exception("Error response %s from %s", exc.response.status_code, exc.request.url)
                return []
            else:
                return self.scenes

    async def async_list_scenes(self) -> list[LifxScene]:
        """Asynchronously return a list of scenes stored on LIFX Cloud."""
        header = {"accept": "application/json"}
        async with httpx.AsyncClient(auth=self._auth_token, timeout=TIMEOUT) as client:
            resp = await client.get(LIFX_URL, headers=header)
            try:
                resp.raise_for_status()
                for scene in resp.json():
                    self.scenes.append(LifxScene(**scene))
            except httpx.HTTPStatusError as exc:
                _LOGGER.exception("Error response %s from %s", exc.response.status_code, exc.request.url)
                return []
            else:
                return self.scenes

    def activate_scene(
        self, scene_uuid: str, duration: int = 1, ignore: list[str] | None = None, fast: bool = False
    ) -> list[dict[str, Any]] | None:
        """Activate a scene by UUID."""
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
        }

        payload = {
            "duration": duration,
            "ignore": ignore if ignore is not None else [],
            "fast": fast,
        }

        with httpx.Client(auth=self._auth_token, timeout=TIMEOUT) as client:
            resp = client.put(f"{LIFX_URL}/scene_id:{scene_uuid}/activate", json=payload, headers=headers)
            results: list[dict[str, Any]] = []

            try:
                resp.raise_for_status()
                if fast:
                    return None
                results = resp.json().get("results", None)

            except httpx.HTTPStatusError as exc:
                _LOGGER.exception("Error response %s from %s", exc.response.status_code, exc.request.url)

            return results

    async def async_activate_scene(
        self, scene_uuid: str, duration: int = 1, ignore: list[str] | None = None, fast: bool = False
    ) -> list[dict[str, str]] | None:
        """Activate a scene by UUID."""
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
        }

        payload = {
            "duration": duration,
            "ignore": ignore if ignore is not None else [],
            "fast": fast,
        }

        async with httpx.AsyncClient(auth=self._auth_token, timeout=TIMEOUT) as client:
            resp = await client.put(f"{LIFX_URL}/scene_id:{scene_uuid}/activate", json=payload, headers=headers)
            results: list[dict[str, str]] = []

            try:
                resp.raise_for_status()
                if fast:
                    return None
                results = resp.json().get("results", None)

            except httpx.HTTPStatusError as exc:
                _LOGGER.exception("Error response %s from %s", exc.response.status_code, exc.request.url)

            return results
