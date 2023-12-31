import json
import requests
from assertpy import assert_that
import pytest
from setting.endpoint import API_PROVICE, API_CITY
from setting.general import api_key, max_latency
from jsonschema import validate as validate_json_schema
from jsonschemas.schema_city import *


def test():
    head = {
        "key": api_key
    }
    req = requests.post(API_CITY, headers=head)

    # VERIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds
    description = req.json().get("rajaongkir")["status"]["description"]



    # ASSERT
    assert_that(status_code).is_equal_to(400)
    assert_that(latency).is_less_than(max_latency)
    assert_that(description).is_equal_to("Unknown method. Method tidak ditemukan, harap baca dokumentasi dengan baik.")



