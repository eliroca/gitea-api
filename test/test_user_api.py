# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: 1.24.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gitea_api.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_create_current_user_repo(self) -> None:
        """Test case for create_current_user_repo

        Create a repository
        """
        pass

    def test_create_user_variable(self) -> None:
        """Test case for create_user_variable

        Create a user-level variable
        """
        pass

    def test_delete_user_runner(self) -> None:
        """Test case for delete_user_runner

        Delete an user-level runner
        """
        pass

    def test_delete_user_secret(self) -> None:
        """Test case for delete_user_secret

        Delete a secret in a user scope
        """
        pass

    def test_delete_user_variable(self) -> None:
        """Test case for delete_user_variable

        Delete a user-level variable which is created by current doer
        """
        pass

    def test_get_user_runner(self) -> None:
        """Test case for get_user_runner

        Get an user-level runner
        """
        pass

    def test_get_user_runners(self) -> None:
        """Test case for get_user_runners

        Get user-level runners
        """
        pass

    def test_get_user_settings(self) -> None:
        """Test case for get_user_settings

        Get user settings
        """
        pass

    def test_get_user_variable(self) -> None:
        """Test case for get_user_variable

        Get a user-level variable which is created by current doer
        """
        pass

    def test_get_user_variables_list(self) -> None:
        """Test case for get_user_variables_list

        Get the user-level list of variables which is created by current doer
        """
        pass

    def test_get_verification_token(self) -> None:
        """Test case for get_verification_token

        Get a Token to verify
        """
        pass

    def test_update_user_secret(self) -> None:
        """Test case for update_user_secret

        Create or Update a secret value in a user scope
        """
        pass

    def test_update_user_settings(self) -> None:
        """Test case for update_user_settings

        Update user settings
        """
        pass

    def test_update_user_variable(self) -> None:
        """Test case for update_user_variable

        Update a user-level variable which is created by current doer
        """
        pass

    def test_user_add_email(self) -> None:
        """Test case for user_add_email

        Add email addresses
        """
        pass

    def test_user_block_user(self) -> None:
        """Test case for user_block_user

        Block a user
        """
        pass

    def test_user_check_following(self) -> None:
        """Test case for user_check_following

        Check if one user is following another user
        """
        pass

    def test_user_check_user_block(self) -> None:
        """Test case for user_check_user_block

        Check if a user is blocked by the authenticated user
        """
        pass

    def test_user_create_hook(self) -> None:
        """Test case for user_create_hook

        Create a hook
        """
        pass

    def test_user_create_o_auth2_application(self) -> None:
        """Test case for user_create_o_auth2_application

        creates a new OAuth2 application
        """
        pass

    def test_user_create_runner_registration_token(self) -> None:
        """Test case for user_create_runner_registration_token

        Get an user's actions runner registration token
        """
        pass

    def test_user_create_token(self) -> None:
        """Test case for user_create_token

        Create an access token
        """
        pass

    def test_user_current_check_following(self) -> None:
        """Test case for user_current_check_following

        Check whether a user is followed by the authenticated user
        """
        pass

    def test_user_current_check_starring(self) -> None:
        """Test case for user_current_check_starring

        Whether the authenticated is starring the repo
        """
        pass

    def test_user_current_delete_follow(self) -> None:
        """Test case for user_current_delete_follow

        Unfollow a user
        """
        pass

    def test_user_current_delete_gpg_key(self) -> None:
        """Test case for user_current_delete_gpg_key

        Remove a GPG key
        """
        pass

    def test_user_current_delete_key(self) -> None:
        """Test case for user_current_delete_key

        Delete a public key
        """
        pass

    def test_user_current_delete_star(self) -> None:
        """Test case for user_current_delete_star

        Unstar the given repo
        """
        pass

    def test_user_current_get_gpg_key(self) -> None:
        """Test case for user_current_get_gpg_key

        Get a GPG key
        """
        pass

    def test_user_current_get_key(self) -> None:
        """Test case for user_current_get_key

        Get a public key
        """
        pass

    def test_user_current_list_followers(self) -> None:
        """Test case for user_current_list_followers

        List the authenticated user's followers
        """
        pass

    def test_user_current_list_following(self) -> None:
        """Test case for user_current_list_following

        List the users that the authenticated user is following
        """
        pass

    def test_user_current_list_gpg_keys(self) -> None:
        """Test case for user_current_list_gpg_keys

        List the authenticated user's GPG keys
        """
        pass

    def test_user_current_list_keys(self) -> None:
        """Test case for user_current_list_keys

        List the authenticated user's public keys
        """
        pass

    def test_user_current_list_repos(self) -> None:
        """Test case for user_current_list_repos

        List the repos that the authenticated user owns
        """
        pass

    def test_user_current_list_starred(self) -> None:
        """Test case for user_current_list_starred

        The repos that the authenticated user has starred
        """
        pass

    def test_user_current_list_subscriptions(self) -> None:
        """Test case for user_current_list_subscriptions

        List repositories watched by the authenticated user
        """
        pass

    def test_user_current_post_gpg_key(self) -> None:
        """Test case for user_current_post_gpg_key

        Create a GPG key
        """
        pass

    def test_user_current_post_key(self) -> None:
        """Test case for user_current_post_key

        Create a public key
        """
        pass

    def test_user_current_put_follow(self) -> None:
        """Test case for user_current_put_follow

        Follow a user
        """
        pass

    def test_user_current_put_star(self) -> None:
        """Test case for user_current_put_star

        Star the given repo
        """
        pass

    def test_user_current_tracked_times(self) -> None:
        """Test case for user_current_tracked_times

        List the current user's tracked times
        """
        pass

    def test_user_delete_access_token(self) -> None:
        """Test case for user_delete_access_token

        delete an access token
        """
        pass

    def test_user_delete_avatar(self) -> None:
        """Test case for user_delete_avatar

        Delete Avatar
        """
        pass

    def test_user_delete_email(self) -> None:
        """Test case for user_delete_email

        Delete email addresses
        """
        pass

    def test_user_delete_hook(self) -> None:
        """Test case for user_delete_hook

        Delete a hook
        """
        pass

    def test_user_delete_o_auth2_application(self) -> None:
        """Test case for user_delete_o_auth2_application

        delete an OAuth2 Application
        """
        pass

    def test_user_edit_hook(self) -> None:
        """Test case for user_edit_hook

        Update a hook
        """
        pass

    def test_user_get(self) -> None:
        """Test case for user_get

        Get a user
        """
        pass

    def test_user_get_current(self) -> None:
        """Test case for user_get_current

        Get the authenticated user
        """
        pass

    def test_user_get_heatmap_data(self) -> None:
        """Test case for user_get_heatmap_data

        Get a user's heatmap
        """
        pass

    def test_user_get_hook(self) -> None:
        """Test case for user_get_hook

        Get a hook
        """
        pass

    def test_user_get_o_auth2_application(self) -> None:
        """Test case for user_get_o_auth2_application

        get an OAuth2 Application
        """
        pass

    def test_user_get_oauth2_application(self) -> None:
        """Test case for user_get_oauth2_application

        List the authenticated user's oauth2 applications
        """
        pass

    def test_user_get_runner_registration_token(self) -> None:
        """Test case for user_get_runner_registration_token

        Get an user's actions runner registration token
        """
        pass

    def test_user_get_stop_watches(self) -> None:
        """Test case for user_get_stop_watches

        Get list of all existing stopwatches
        """
        pass

    def test_user_get_tokens(self) -> None:
        """Test case for user_get_tokens

        List the authenticated user's access tokens
        """
        pass

    def test_user_list_activity_feeds(self) -> None:
        """Test case for user_list_activity_feeds

        List a user's activity feeds
        """
        pass

    def test_user_list_blocks(self) -> None:
        """Test case for user_list_blocks

        List users blocked by the authenticated user
        """
        pass

    def test_user_list_emails(self) -> None:
        """Test case for user_list_emails

        List the authenticated user's email addresses
        """
        pass

    def test_user_list_followers(self) -> None:
        """Test case for user_list_followers

        List the given user's followers
        """
        pass

    def test_user_list_following(self) -> None:
        """Test case for user_list_following

        List the users that the given user is following
        """
        pass

    def test_user_list_gpg_keys(self) -> None:
        """Test case for user_list_gpg_keys

        List the given user's GPG keys
        """
        pass

    def test_user_list_hooks(self) -> None:
        """Test case for user_list_hooks

        List the authenticated user's webhooks
        """
        pass

    def test_user_list_keys(self) -> None:
        """Test case for user_list_keys

        List the given user's public keys
        """
        pass

    def test_user_list_repos(self) -> None:
        """Test case for user_list_repos

        List the repos owned by the given user
        """
        pass

    def test_user_list_starred(self) -> None:
        """Test case for user_list_starred

        The repos that the given user has starred
        """
        pass

    def test_user_list_subscriptions(self) -> None:
        """Test case for user_list_subscriptions

        List the repositories watched by a user
        """
        pass

    def test_user_list_teams(self) -> None:
        """Test case for user_list_teams

        List all the teams a user belongs to
        """
        pass

    def test_user_search(self) -> None:
        """Test case for user_search

        Search for users
        """
        pass

    def test_user_unblock_user(self) -> None:
        """Test case for user_unblock_user

        Unblock a user
        """
        pass

    def test_user_update_avatar(self) -> None:
        """Test case for user_update_avatar

        Update Avatar
        """
        pass

    def test_user_update_o_auth2_application(self) -> None:
        """Test case for user_update_o_auth2_application

        update an OAuth2 Application, this includes regenerating the client secret
        """
        pass

    def test_user_verify_gpg_key(self) -> None:
        """Test case for user_verify_gpg_key

        Verify a GPG key
        """
        pass


if __name__ == '__main__':
    unittest.main()
