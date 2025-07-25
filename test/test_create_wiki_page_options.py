# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.24.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_api.models.create_wiki_page_options import CreateWikiPageOptions

class TestCreateWikiPageOptions(unittest.TestCase):
    """CreateWikiPageOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateWikiPageOptions:
        """Test CreateWikiPageOptions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateWikiPageOptions`
        """
        model = CreateWikiPageOptions()
        if include_optional:
            return CreateWikiPageOptions(
                content_base64 = '',
                message = '',
                title = ''
            )
        else:
            return CreateWikiPageOptions(
        )
        """

    def testCreateWikiPageOptions(self):
        """Test CreateWikiPageOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
