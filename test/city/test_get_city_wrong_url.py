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
    req = requests.post("https://api.rajaongkir.com/starter/cityss", headers=head)

    # VERIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds


    # ASSERT
    assert_that(status_code).is_equal_to(404)
    assert_that(latency).is_less_than(max_latency)



