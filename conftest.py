import os
import shutil
from pathlib import Path

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

from helpers import POM

PATH = Path(__file__).resolve().parent


def pytest_configure():
    """
    Copies the .env.example values into .env if the file doesn't exist.
    Creates the reports folder if it doesn't exist.
    """
    env_file = PATH.joinpath(".env")
    env_example_file = PATH.joinpath(".env.example")

    if not env_file.exists() and env_example_file.exists():
        shutil.copyfile(env_example_file, env_file)

    load_dotenv(env_file)

    reports_folder = PATH.joinpath("reports")
    reports_folder.mkdir(exist_ok=True)


@pytest.fixture(scope="session")
def base_url() -> str:
    if url := os.getenv("BASE_URL"):
        return url
    raise RuntimeError("BASE_URL is required")


@pytest.fixture(scope="function")
def pom(page: Page) -> POM:
    return POM(page)
