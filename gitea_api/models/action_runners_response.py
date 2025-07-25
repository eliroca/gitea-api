# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.24.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from gitea_api.models.action_runner import ActionRunner
from typing import Optional, Set
from typing_extensions import Self

class ActionRunnersResponse(BaseModel):
    """
    ActionRunnersResponse returns Runners
    """ # noqa: E501
    runners: Optional[List[ActionRunner]] = None
    total_count: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["runners", "total_count"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ActionRunnersResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in runners (list)
        _items = []
        if self.runners:
            for _item_runners in self.runners:
                if _item_runners:
                    _items.append(_item_runners.to_dict())
            _dict['runners'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActionRunnersResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "runners": [ActionRunner.from_dict(_item) for _item in obj["runners"]] if obj.get("runners") is not None else None,
            "total_count": obj.get("total_count")
        })
        return _obj


