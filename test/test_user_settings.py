# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.24.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_api.models.user_settings import UserSettings

class TestUserSettings(unittest.TestCase):
    """UserSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSettings:
        """Test UserSettings
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSettings`
        """
        model = UserSettings()
        if include_optional:
            return UserSettings(
                description = '',
                diff_view_style = '',
                full_name = '',
                hide_activity = True,
                hide_email = True,
                language = '',
                location = '',
                theme = '',
                website = ''
            )
        else:
            return UserSettings(
        )
        """

    def testUserSettings(self):
        """Test UserSettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
