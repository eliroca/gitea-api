# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.24.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_api.models.action_variable import ActionVariable

class TestActionVariable(unittest.TestCase):
    """ActionVariable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActionVariable:
        """Test ActionVariable
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActionVariable`
        """
        model = ActionVariable()
        if include_optional:
            return ActionVariable(
                data = '',
                description = '',
                name = '',
                owner_id = 56,
                repo_id = 56
            )
        else:
            return ActionVariable(
        )
        """

    def testActionVariable(self):
        """Test ActionVariable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
