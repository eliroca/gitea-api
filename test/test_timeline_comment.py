# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.24.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_api.models.timeline_comment import TimelineComment

class TestTimelineComment(unittest.TestCase):
    """TimelineComment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimelineComment:
        """Test TimelineComment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimelineComment`
        """
        model = TimelineComment()
        if include_optional:
            return TimelineComment(
                assignee = gitea_api.models.user.User(
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
                    website = '', ),
                assignee_team = gitea_api.models.team.Team(
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
                body = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dependent_issue = gitea_api.models.issue.Issue(
                    assets = [
                        gitea_api.models.attachment.Attachment(
                            browser_download_url = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            download_count = 56, 
                            id = 56, 
                            name = '', 
                            size = 56, 
                            uuid = '', )
                        ], 
                    assignee = gitea_api.models.user.User(
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
                        website = '', ), 
                    assignees = [
                        gitea_api.models.user.User(
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
                        ], 
                    body = '', 
                    closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    comments = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    html_url = '', 
                    id = 56, 
                    is_locked = True, 
                    labels = [
                        gitea_api.models.label.Label(
                            color = '00aabb', 
                            description = '', 
                            exclusive = False, 
                            id = 56, 
                            is_archived = False, 
                            name = '', 
                            url = '', )
                        ], 
                    milestone = gitea_api.models.milestone.Milestone(
                        closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        closed_issues = 56, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = 56, 
                        open_issues = 56, 
                        state = '', 
                        title = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    number = 56, 
                    original_author = '', 
                    original_author_id = 56, 
                    pin_order = 56, 
                    pull_request = gitea_api.models.pull_request_meta.PullRequestMeta(
                        draft = True, 
                        html_url = '', 
                        merged = True, 
                        merged_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    ref = '', 
                    repository = gitea_api.models.repository_meta.RepositoryMeta(
                        full_name = '', 
                        id = 56, 
                        name = '', 
                        owner = '', ), 
                    state = '', 
                    title = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    url = '', 
                    user = , ),
                html_url = '',
                id = 56,
                issue_url = '',
                label = gitea_api.models.label.Label(
                    color = '00aabb', 
                    description = '', 
                    exclusive = False, 
                    id = 56, 
                    is_archived = False, 
                    name = '', 
                    url = '', ),
                milestone = gitea_api.models.milestone.Milestone(
                    closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    closed_issues = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = 56, 
                    open_issues = 56, 
                    state = '', 
                    title = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                new_ref = '',
                new_title = '',
                old_milestone = gitea_api.models.milestone.Milestone(
                    closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    closed_issues = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = 56, 
                    open_issues = 56, 
                    state = '', 
                    title = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                old_project_id = 56,
                old_ref = '',
                old_title = '',
                project_id = 56,
                pull_request_url = '',
                ref_action = '',
                ref_comment = gitea_api.models.comment.Comment(
                    assets = [
                        gitea_api.models.attachment.Attachment(
                            browser_download_url = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            download_count = 56, 
                            id = 56, 
                            name = '', 
                            size = 56, 
                            uuid = '', )
                        ], 
                    body = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    html_url = '', 
                    id = 56, 
                    issue_url = '', 
                    original_author = '', 
                    original_author_id = 56, 
                    pull_request_url = '', 
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
                        website = '', ), ),
                ref_commit_sha = '',
                ref_issue = gitea_api.models.issue.Issue(
                    assets = [
                        gitea_api.models.attachment.Attachment(
                            browser_download_url = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            download_count = 56, 
                            id = 56, 
                            name = '', 
                            size = 56, 
                            uuid = '', )
                        ], 
                    assignee = gitea_api.models.user.User(
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
                        website = '', ), 
                    assignees = [
                        gitea_api.models.user.User(
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
                        ], 
                    body = '', 
                    closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    comments = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    html_url = '', 
                    id = 56, 
                    is_locked = True, 
                    labels = [
                        gitea_api.models.label.Label(
                            color = '00aabb', 
                            description = '', 
                            exclusive = False, 
                            id = 56, 
                            is_archived = False, 
                            name = '', 
                            url = '', )
                        ], 
                    milestone = gitea_api.models.milestone.Milestone(
                        closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        closed_issues = 56, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = 56, 
                        open_issues = 56, 
                        state = '', 
                        title = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    number = 56, 
                    original_author = '', 
                    original_author_id = 56, 
                    pin_order = 56, 
                    pull_request = gitea_api.models.pull_request_meta.PullRequestMeta(
                        draft = True, 
                        html_url = '', 
                        merged = True, 
                        merged_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    ref = '', 
                    repository = gitea_api.models.repository_meta.RepositoryMeta(
                        full_name = '', 
                        id = 56, 
                        name = '', 
                        owner = '', ), 
                    state = '', 
                    title = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    url = '', 
                    user = , ),
                removed_assignee = True,
                resolve_doer = gitea_api.models.user.User(
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
                    website = '', ),
                review_id = 56,
                tracked_time = gitea_api.models.tracked_time.TrackedTime(
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = 56, 
                    issue = gitea_api.models.issue.Issue(
                        assets = [
                            gitea_api.models.attachment.Attachment(
                                browser_download_url = '', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                download_count = 56, 
                                id = 56, 
                                name = '', 
                                size = 56, 
                                uuid = '', )
                            ], 
                        assignee = gitea_api.models.user.User(
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
                            website = '', ), 
                        assignees = [
                            gitea_api.models.user.User(
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
                            ], 
                        body = '', 
                        closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        comments = 56, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        html_url = '', 
                        id = 56, 
                        is_locked = True, 
                        labels = [
                            gitea_api.models.label.Label(
                                color = '00aabb', 
                                description = '', 
                                exclusive = False, 
                                id = 56, 
                                is_archived = False, 
                                name = '', 
                                url = '', )
                            ], 
                        milestone = gitea_api.models.milestone.Milestone(
                            closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            closed_issues = 56, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = 56, 
                            open_issues = 56, 
                            state = '', 
                            title = '', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        number = 56, 
                        original_author = '', 
                        original_author_id = 56, 
                        pin_order = 56, 
                        pull_request = gitea_api.models.pull_request_meta.PullRequestMeta(
                            draft = True, 
                            html_url = '', 
                            merged = True, 
                            merged_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        ref = '', 
                        repository = gitea_api.models.repository_meta.RepositoryMeta(
                            full_name = '', 
                            id = 56, 
                            name = '', 
                            owner = '', ), 
                        state = '', 
                        title = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', 
                        user = , ), 
                    issue_id = 56, 
                    time = 56, 
                    user_id = 56, 
                    user_name = '', ),
                type = '',
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
            return TimelineComment(
        )
        """

    def testTimelineComment(self):
        """Test TimelineComment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
