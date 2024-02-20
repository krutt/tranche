#!/usr/bin/env python3.8
# coding:utf-8
# Copyright (C) 2022-2023 All rights reserved.
# FILENAME:    ~~/src/types/open_channel.py
# VERSION: 	   0.3.3
# CREATED: 	   2023-12-02 20:50
# AUTHOR: 	   Sitt Guruvanich <aekasitt.g+github@siamintech.co.th>
# DESCRIPTION:
#
# HISTORY:
# *************************************************************

### Third-party packages ###
from pydantic import BaseModel, StrictStr


class OpenChannel(BaseModel):
  funding_txid: StrictStr


__all__ = ["OpenChannel"]
