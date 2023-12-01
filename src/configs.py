#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2022-2023 All rights reserved.
# FILENAME:    ~~/src/configs.py
# VERSION: 	   0.2.0
# CREATED: 	   2023-12-01 05:31
# AUTHOR: 	   Sitt Guruvanich <aekasitt.g+github@siamintech.co.th>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Standard packages ###
from pydantic import TypeAdapter
from typing import Any, Dict, List, Optional
from yaml import Loader, load, dump

### Local modules ###
from src.constants import YAML_DEFINITIONS
from src.schemas import ClusterEnum, ImageAlias, Service, ServiceName

CLUSTERS: Dict[ClusterEnum, Dict[ServiceName, Service]]
DEPRECATED: List[str]
IMAGES: Dict[ImageAlias, str]
NETWORK: str

constants: Optional[Dict[str, Any]] = load(YAML_DEFINITIONS, Loader=Loader)
if constants:
    CLUSTERS = TypeAdapter(Dict[ClusterEnum, Dict[ServiceName, Service]]).validate_python(
        constants["clusters"]
    )
    DEPRECATED = constants.get("deprecated", [])
    IMAGES = TypeAdapter(Dict[ImageAlias, str]).validate_python(constants["images"])
    NETWORK = constants.get("network", "tranche")

__all__ = ["CLUSTERS", "DEPRECATED", "IMAGES", "NETWORK"]
