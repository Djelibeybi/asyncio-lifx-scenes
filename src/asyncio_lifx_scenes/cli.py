"""Basic LIFX Scenes CLI."""

from __future__ import annotations

from typing import Annotated

import rich
import typer

from .scenes import LifxScenes

app = typer.Typer(name="lifx-scenes")


def complete_ignore() -> list[str]:
    """Return a list of ignore options."""
    return [
        "power",
        "infrared",
        "duration",
        "intensity",
        "hue",
        "saturation",
        "brightness",
        "kelvin",
    ]  # pragma: no cover


@app.command(name="list")
def list_scenes(
    token: Annotated[str, typer.Argument(envvar="LIFX_API_TOKEN")],
    short: Annotated[bool, typer.Option("--short", help="Return scene name and UUID only.")] = False,
) -> None:
    """
    List scenes.

    Requires a LIFX Cloud Personal Access Token.
    """
    scenes = LifxScenes(token).list_scenes()
    if short is True:
        for scene in scenes:
            rich.print(f"{scene.name}: {scene.uuid}")
    else:
        rich.print(scenes)


@app.command(name="activate")
def activate_scene(
    scene_uuid: Annotated[str, typer.Argument()],
    token: Annotated[str, typer.Argument(envvar="LIFX_API_TOKEN")],
    duration: Annotated[
        int, typer.Option(help="Duration in seconds to transition from current state to the scene state.")
    ] = 1,
    ignore: Annotated[
        list[str] | None,
        typer.Option(help="Stored properties to ignore when applying the scene.", autocompletion=complete_ignore),
    ] = None,
    fast: Annotated[
        bool, typer.Option("--fast", help="Apply scene without checking current state or returning a result.")
    ] = False,
) -> None:
    """
    Activate a scene.

    Requires a LIFX Cloud Personal Access Token.
    """
    result = LifxScenes(token).activate_scene(scene_uuid, duration, ignore, fast)
    if fast is False or result is not None:
        rich.print(result)


if __name__ == "__main__":
    """Run the CLI."""
    app()
