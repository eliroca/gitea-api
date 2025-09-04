# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from gitea_api.api.activitypub_api import ActivitypubApi
    from gitea_api.api.admin_api import AdminApi
    from gitea_api.api.issue_api import IssueApi
    from gitea_api.api.miscellaneous_api import MiscellaneousApi
    from gitea_api.api.notification_api import NotificationApi
    from gitea_api.api.organization_api import OrganizationApi
    from gitea_api.api.package_api import PackageApi
    from gitea_api.api.repository_api import RepositoryApi
    from gitea_api.api.settings_api import SettingsApi
    from gitea_api.api.user_api import UserApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from gitea_api.api.activitypub_api import ActivitypubApi
from gitea_api.api.admin_api import AdminApi
from gitea_api.api.issue_api import IssueApi
from gitea_api.api.miscellaneous_api import MiscellaneousApi
from gitea_api.api.notification_api import NotificationApi
from gitea_api.api.organization_api import OrganizationApi
from gitea_api.api.package_api import PackageApi
from gitea_api.api.repository_api import RepositoryApi
from gitea_api.api.settings_api import SettingsApi
from gitea_api.api.user_api import UserApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
