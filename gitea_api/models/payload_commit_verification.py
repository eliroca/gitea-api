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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_api.models.payload_user import PayloadUser
from typing import Optional, Set
from typing_extensions import Self

class PayloadCommitVerification(BaseModel):
    """
    PayloadCommitVerification represents the GPG verification of a commit
    """ # noqa: E501
    payload: Optional[StrictStr] = None
    reason: Optional[StrictStr] = None
    signature: Optional[StrictStr] = None
    signer: Optional[PayloadUser] = None
    verified: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["payload", "reason", "signature", "signer", "verified"]

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
        """Create an instance of PayloadCommitVerification from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of signer
        if self.signer:
            _dict['signer'] = self.signer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PayloadCommitVerification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "payload": obj.get("payload"),
            "reason": obj.get("reason"),
            "signature": obj.get("signature"),
            "signer": PayloadUser.from_dict(obj["signer"]) if obj.get("signer") is not None else None,
            "verified": obj.get("verified")
        })
        return _obj


