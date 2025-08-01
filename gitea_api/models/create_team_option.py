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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateTeamOption(BaseModel):
    """
    CreateTeamOption options for creating a team
    """ # noqa: E501
    can_create_org_repo: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    includes_all_repositories: Optional[StrictBool] = None
    name: StrictStr
    permission: Optional[StrictStr] = None
    units: Optional[List[StrictStr]] = None
    units_map: Optional[Dict[str, StrictStr]] = None
    __properties: ClassVar[List[str]] = ["can_create_org_repo", "description", "includes_all_repositories", "name", "permission", "units", "units_map"]

    @field_validator('permission')
    def permission_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['read', 'write', 'admin']):
            raise ValueError("must be one of enum values ('read', 'write', 'admin')")
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
        """Create an instance of CreateTeamOption from a JSON string"""
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
        """Create an instance of CreateTeamOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "can_create_org_repo": obj.get("can_create_org_repo"),
            "description": obj.get("description"),
            "includes_all_repositories": obj.get("includes_all_repositories"),
            "name": obj.get("name"),
            "permission": obj.get("permission"),
            "units": obj.get("units"),
            "units_map": obj.get("units_map")
        })
        return _obj


