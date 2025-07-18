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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_api.models.repository import Repository
from typing import Optional, Set
from typing_extensions import Self

class DeployKey(BaseModel):
    """
    DeployKey a deploy key
    """ # noqa: E501
    created_at: Optional[datetime] = None
    fingerprint: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    key: Optional[StrictStr] = None
    key_id: Optional[StrictInt] = None
    read_only: Optional[StrictBool] = None
    repository: Optional[Repository] = None
    title: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["created_at", "fingerprint", "id", "key", "key_id", "read_only", "repository", "title", "url"]

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
        """Create an instance of DeployKey from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeployKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "fingerprint": obj.get("fingerprint"),
            "id": obj.get("id"),
            "key": obj.get("key"),
            "key_id": obj.get("key_id"),
            "read_only": obj.get("read_only"),
            "repository": Repository.from_dict(obj["repository"]) if obj.get("repository") is not None else None,
            "title": obj.get("title"),
            "url": obj.get("url")
        })
        return _obj


