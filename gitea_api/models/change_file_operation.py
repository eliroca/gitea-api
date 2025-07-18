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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ChangeFileOperation(BaseModel):
    """
    ChangeFileOperation for creating, updating or deleting a file
    """ # noqa: E501
    content: Optional[StrictStr] = Field(default=None, description="new or updated file content, must be base64 encoded")
    from_path: Optional[StrictStr] = Field(default=None, description="old path of the file to move")
    operation: StrictStr = Field(description="indicates what to do with the file")
    path: StrictStr = Field(description="path to the existing or new file")
    sha: Optional[StrictStr] = Field(default=None, description="sha is the SHA for the file that already exists, required for update or delete")
    __properties: ClassVar[List[str]] = ["content", "from_path", "operation", "path", "sha"]

    @field_validator('operation')
    def operation_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['create', 'update', 'delete']):
            raise ValueError("must be one of enum values ('create', 'update', 'delete')")
        return value

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
        """Create an instance of ChangeFileOperation from a JSON string"""
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
        """Create an instance of ChangeFileOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "content": obj.get("content"),
            "from_path": obj.get("from_path"),
            "operation": obj.get("operation"),
            "path": obj.get("path"),
            "sha": obj.get("sha")
        })
        return _obj


