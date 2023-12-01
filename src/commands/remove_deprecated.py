#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2022-2023 All rights reserved.
# FILENAME:    ~~/src/commands/remove_deprecated.py
# VERSION: 	   0.2.0
# CREATED: 	   2023-12-01 06:24
# AUTHOR: 	   Sitt Guruvanich <aekasitt.g+github@siamintech.co.th>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from typing import Set

### Third-party packages ###
from click import command
from docker import DockerClient, from_env
from rich.progress import track

### Local modules ###
from src.configs import DEPRECATED


@command
def remove_deprecated() -> None:
    """Remove images deprecated by workspace."""
    client: DockerClient = from_env()
    if client.ping():
        docker_images: Set[str] = {image.tags[0] for image in client.images.list()}
        for registry_id in track(DEPRECATED, description="Remove images deprecated by workspace."):
            if registry_id in docker_images:
                client.images.remove(registry_id)
                print(f"<Image: '{ registry_id }'> removed.")
    else:
        print("!! Unable to connect to docker daemon.")


__all__ = ["remove_deprecated"]
