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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ActionTask(BaseModel):
    """
    ActionTask represents a ActionTask
    """ # noqa: E501
    created_at: Optional[datetime] = None
    display_title: Optional[StrictStr] = None
    event: Optional[StrictStr] = None
    head_branch: Optional[StrictStr] = None
    head_sha: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    run_number: Optional[StrictInt] = None
    run_started_at: Optional[datetime] = None
    status: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    workflow_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["created_at", "display_title", "event", "head_branch", "head_sha", "id", "name", "run_number", "run_started_at", "status", "updated_at", "url", "workflow_id"]

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
        """Create an instance of ActionTask from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActionTask from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "display_title": obj.get("display_title"),
            "event": obj.get("event"),
            "head_branch": obj.get("head_branch"),
            "head_sha": obj.get("head_sha"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "run_number": obj.get("run_number"),
            "run_started_at": obj.get("run_started_at"),
            "status": obj.get("status"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "workflow_id": obj.get("workflow_id")
        })
        return _obj


