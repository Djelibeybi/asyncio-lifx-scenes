"""Test asyncio-lifx-scenes CLI."""

import pytest
from pytest_httpx import HTTPXMock
from typer.testing import CliRunner

from asyncio_lifx_scenes.__main__ import app

from . import LIFX_SCENES

runner = CliRunner(env={"LIFX_API_TOKEN": "dummy-token"})


def test_cli() -> None:
    """Test CLI app."""
    result = runner.invoke(app)
    assert result.exit_code == 2
    assert "Missing command" in result.stdout


def test_cli_help() -> None:
    """Test CLI help."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "lifx-scenes" in result.stdout


def test_cli_show_completion() -> None:
    """Test CLI show completion."""
    result = runner.invoke(app, ["--show-completion"])
    assert result.exit_code == 0
    assert "lifx_scenes" in result.stdout


@pytest.mark.httpx_mock(assert_all_responses_were_requested=False)
def test_cli_list(httpx_mock: HTTPXMock) -> None:
    """Test CLI list."""
    httpx_mock.add_response(json=LIFX_SCENES)
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "TestScene1" in result.stdout


@pytest.mark.httpx_mock(assert_all_responses_were_requested=False)
def test_cli_list_short(httpx_mock: HTTPXMock) -> None:
    """Test CLI list short."""
    httpx_mock.add_response(json=LIFX_SCENES)
    result = runner.invoke(app, ["list", "--short"])
    assert result.exit_code == 0
    assert "TestScene1" in result.stdout


@pytest.mark.httpx_mock(assert_all_responses_were_requested=False)
def test_cli_activate(httpx_mock: HTTPXMock) -> None:
    """Test CLI activate."""
    httpx_mock.add_response(json={"results": [{"status": "ok"}]})
    result = runner.invoke(app, ["activate", "test-uuid"])
    assert result.exit_code == 0


@pytest.mark.httpx_mock(assert_all_responses_were_requested=False)
def test_cli_activate_fast(httpx_mock: HTTPXMock) -> None:
    """Test CLI activate fast."""
    httpx_mock.add_response(json={"results": [{"status": "ok"}]})
    result = runner.invoke(app, ["activate", "test-uuid", "--fast"])
    assert result.exit_code == 0
