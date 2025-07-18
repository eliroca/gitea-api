# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.24.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_api.models.pull_review import PullReview

class TestPullReview(unittest.TestCase):
    """PullReview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PullReview:
        """Test PullReview
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PullReview`
        """
        model = PullReview()
        if include_optional:
            return PullReview(
                body = '',
                comments_count = 56,
                commit_id = '',
                dismissed = True,
                html_url = '',
                id = 56,
                official = True,
                pull_request_url = '',
                stale = True,
                state = '',
                submitted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                team = gitea_api.models.team.Team(
                    can_create_org_repo = True, 
                    description = '', 
                    id = 56, 
                    includes_all_repositories = True, 
                    name = '', 
                    organization = gitea_api.models.organization.Organization(
                        avatar_url = '', 
                        description = '', 
                        email = '', 
                        full_name = '', 
                        id = 56, 
                        location = '', 
                        name = '', 
                        repo_admin_change_team_access = True, 
                        username = '', 
                        visibility = '', 
                        website = '', ), 
                    permission = 'none', 
                    units = [repo.code, repo.issues, repo.ext_issues, repo.wiki, repo.pulls, repo.releases, repo.projects, repo.ext_wiki], 
                    units_map = {"repo.code":"read","repo.ext_issues":"none","repo.ext_wiki":"none","repo.issues":"write","repo.projects":"none","repo.pulls":"owner","repo.releases":"none","repo.wiki":"admin"}, ),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user = gitea_api.models.user.User(
                    active = True, 
                    avatar_url = '', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    email = '', 
                    followers_count = 56, 
                    following_count = 56, 
                    full_name = '', 
                    html_url = '', 
                    id = 56, 
                    is_admin = True, 
                    language = '', 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    location = '', 
                    login = '', 
                    login_name = 'empty', 
                    prohibit_login = True, 
                    restricted = True, 
                    source_id = 56, 
                    starred_repos_count = 56, 
                    visibility = '', 
                    website = '', )
            )
        else:
            return PullReview(
        )
        """

    def testPullReview(self):
        """Test PullReview"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
