# gitea_api.RepositoryApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_repo_transfer**](RepositoryApi.md#accept_repo_transfer) | **POST** /repos/{owner}/{repo}/transfer/accept | Accept a repo transfer
[**actions_disable_workflow**](RepositoryApi.md#actions_disable_workflow) | **PUT** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable | Disable a workflow
[**actions_dispatch_workflow**](RepositoryApi.md#actions_dispatch_workflow) | **POST** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches | Create a workflow dispatch event
[**actions_enable_workflow**](RepositoryApi.md#actions_enable_workflow) | **PUT** /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable | Enable a workflow
[**actions_get_workflow**](RepositoryApi.md#actions_get_workflow) | **GET** /repos/{owner}/{repo}/actions/workflows/{workflow_id} | Get a workflow
[**actions_list_repository_workflows**](RepositoryApi.md#actions_list_repository_workflows) | **GET** /repos/{owner}/{repo}/actions/workflows | List repository workflows
[**create_current_user_repo**](RepositoryApi.md#create_current_user_repo) | **POST** /user/repos | Create a repository
[**create_fork**](RepositoryApi.md#create_fork) | **POST** /repos/{owner}/{repo}/forks | Fork a repository
[**create_repo_variable**](RepositoryApi.md#create_repo_variable) | **POST** /repos/{owner}/{repo}/actions/variables/{variablename} | Create a repo-level variable
[**delete_artifact**](RepositoryApi.md#delete_artifact) | **DELETE** /repos/{owner}/{repo}/actions/artifacts/{artifact_id} | Deletes a specific artifact for a workflow run
[**delete_repo_runner**](RepositoryApi.md#delete_repo_runner) | **DELETE** /repos/{owner}/{repo}/actions/runners/{runner_id} | Delete an repo-level runner
[**delete_repo_secret**](RepositoryApi.md#delete_repo_secret) | **DELETE** /repos/{owner}/{repo}/actions/secrets/{secretname} | Delete a secret in a repository
[**delete_repo_variable**](RepositoryApi.md#delete_repo_variable) | **DELETE** /repos/{owner}/{repo}/actions/variables/{variablename} | Delete a repo-level variable
[**download_actions_run_job_logs**](RepositoryApi.md#download_actions_run_job_logs) | **GET** /repos/{owner}/{repo}/actions/jobs/{job_id}/logs | Downloads the job logs for a workflow run
[**download_artifact**](RepositoryApi.md#download_artifact) | **GET** /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip | Downloads a specific artifact for a workflow run redirects to blob url
[**generate_repo**](RepositoryApi.md#generate_repo) | **POST** /repos/{template_owner}/{template_repo}/generate | Create a repository using a template
[**get_annotated_tag**](RepositoryApi.md#get_annotated_tag) | **GET** /repos/{owner}/{repo}/git/tags/{sha} | Gets the tag object of an annotated tag (not lightweight tags)
[**get_artifact**](RepositoryApi.md#get_artifact) | **GET** /repos/{owner}/{repo}/actions/artifacts/{artifact_id} | Gets a specific artifact for a workflow run
[**get_artifacts**](RepositoryApi.md#get_artifacts) | **GET** /repos/{owner}/{repo}/actions/artifacts | Lists all artifacts for a repository
[**get_artifacts_of_run**](RepositoryApi.md#get_artifacts_of_run) | **GET** /repos/{owner}/{repo}/actions/runs/{run}/artifacts | Lists all artifacts for a repository run
[**get_blob**](RepositoryApi.md#get_blob) | **GET** /repos/{owner}/{repo}/git/blobs/{sha} | Gets the blob of a repository.
[**get_repo_runner**](RepositoryApi.md#get_repo_runner) | **GET** /repos/{owner}/{repo}/actions/runners/{runner_id} | Get an repo-level runner
[**get_repo_runners**](RepositoryApi.md#get_repo_runners) | **GET** /repos/{owner}/{repo}/actions/runners | Get repo-level runners
[**get_repo_variable**](RepositoryApi.md#get_repo_variable) | **GET** /repos/{owner}/{repo}/actions/variables/{variablename} | Get a repo-level variable
[**get_repo_variables_list**](RepositoryApi.md#get_repo_variables_list) | **GET** /repos/{owner}/{repo}/actions/variables | Get repo-level variables list
[**get_tree**](RepositoryApi.md#get_tree) | **GET** /repos/{owner}/{repo}/git/trees/{sha} | Gets the tree of a repository.
[**list_action_tasks**](RepositoryApi.md#list_action_tasks) | **GET** /repos/{owner}/{repo}/actions/tasks | List a repository&#39;s action tasks
[**list_forks**](RepositoryApi.md#list_forks) | **GET** /repos/{owner}/{repo}/forks | List a repository&#39;s forks
[**reject_repo_transfer**](RepositoryApi.md#reject_repo_transfer) | **POST** /repos/{owner}/{repo}/transfer/reject | Reject a repo transfer
[**repo_add_collaborator**](RepositoryApi.md#repo_add_collaborator) | **PUT** /repos/{owner}/{repo}/collaborators/{collaborator} | Add or Update a collaborator to a repository
[**repo_add_push_mirror**](RepositoryApi.md#repo_add_push_mirror) | **POST** /repos/{owner}/{repo}/push_mirrors | add a push mirror to the repository
[**repo_add_team**](RepositoryApi.md#repo_add_team) | **PUT** /repos/{owner}/{repo}/teams/{team} | Add a team to a repository
[**repo_add_topic**](RepositoryApi.md#repo_add_topic) | **PUT** /repos/{owner}/{repo}/topics/{topic} | Add a topic to a repository
[**repo_apply_diff_patch**](RepositoryApi.md#repo_apply_diff_patch) | **POST** /repos/{owner}/{repo}/diffpatch | Apply diff patch to repository
[**repo_cancel_scheduled_auto_merge**](RepositoryApi.md#repo_cancel_scheduled_auto_merge) | **DELETE** /repos/{owner}/{repo}/pulls/{index}/merge | Cancel the scheduled auto merge for the given pull request
[**repo_change_files**](RepositoryApi.md#repo_change_files) | **POST** /repos/{owner}/{repo}/contents | Modify multiple files in a repository
[**repo_check_collaborator**](RepositoryApi.md#repo_check_collaborator) | **GET** /repos/{owner}/{repo}/collaborators/{collaborator} | Check if a user is a collaborator of a repository
[**repo_check_team**](RepositoryApi.md#repo_check_team) | **GET** /repos/{owner}/{repo}/teams/{team} | Check if a team is assigned to a repository
[**repo_compare_diff**](RepositoryApi.md#repo_compare_diff) | **GET** /repos/{owner}/{repo}/compare/{basehead} | Get commit comparison information
[**repo_create_branch**](RepositoryApi.md#repo_create_branch) | **POST** /repos/{owner}/{repo}/branches | Create a branch
[**repo_create_branch_protection**](RepositoryApi.md#repo_create_branch_protection) | **POST** /repos/{owner}/{repo}/branch_protections | Create a branch protections for a repository
[**repo_create_file**](RepositoryApi.md#repo_create_file) | **POST** /repos/{owner}/{repo}/contents/{filepath} | Create a file in a repository
[**repo_create_hook**](RepositoryApi.md#repo_create_hook) | **POST** /repos/{owner}/{repo}/hooks | Create a hook
[**repo_create_key**](RepositoryApi.md#repo_create_key) | **POST** /repos/{owner}/{repo}/keys | Add a key to a repository
[**repo_create_pull_request**](RepositoryApi.md#repo_create_pull_request) | **POST** /repos/{owner}/{repo}/pulls | Create a pull request
[**repo_create_pull_review**](RepositoryApi.md#repo_create_pull_review) | **POST** /repos/{owner}/{repo}/pulls/{index}/reviews | Create a review to an pull request
[**repo_create_pull_review_requests**](RepositoryApi.md#repo_create_pull_review_requests) | **POST** /repos/{owner}/{repo}/pulls/{index}/requested_reviewers | create review requests for a pull request
[**repo_create_release**](RepositoryApi.md#repo_create_release) | **POST** /repos/{owner}/{repo}/releases | Create a release
[**repo_create_release_attachment**](RepositoryApi.md#repo_create_release_attachment) | **POST** /repos/{owner}/{repo}/releases/{id}/assets | Create a release attachment
[**repo_create_runner_registration_token**](RepositoryApi.md#repo_create_runner_registration_token) | **POST** /repos/{owner}/{repo}/actions/runners/registration-token | Get a repository&#39;s actions runner registration token
[**repo_create_status**](RepositoryApi.md#repo_create_status) | **POST** /repos/{owner}/{repo}/statuses/{sha} | Create a commit status
[**repo_create_tag**](RepositoryApi.md#repo_create_tag) | **POST** /repos/{owner}/{repo}/tags | Create a new git tag in a repository
[**repo_create_tag_protection**](RepositoryApi.md#repo_create_tag_protection) | **POST** /repos/{owner}/{repo}/tag_protections | Create a tag protections for a repository
[**repo_create_wiki_page**](RepositoryApi.md#repo_create_wiki_page) | **POST** /repos/{owner}/{repo}/wiki/new | Create a wiki page
[**repo_delete**](RepositoryApi.md#repo_delete) | **DELETE** /repos/{owner}/{repo} | Delete a repository
[**repo_delete_avatar**](RepositoryApi.md#repo_delete_avatar) | **DELETE** /repos/{owner}/{repo}/avatar | Delete avatar
[**repo_delete_branch**](RepositoryApi.md#repo_delete_branch) | **DELETE** /repos/{owner}/{repo}/branches/{branch} | Delete a specific branch from a repository
[**repo_delete_branch_protection**](RepositoryApi.md#repo_delete_branch_protection) | **DELETE** /repos/{owner}/{repo}/branch_protections/{name} | Delete a specific branch protection for the repository
[**repo_delete_collaborator**](RepositoryApi.md#repo_delete_collaborator) | **DELETE** /repos/{owner}/{repo}/collaborators/{collaborator} | Delete a collaborator from a repository
[**repo_delete_file**](RepositoryApi.md#repo_delete_file) | **DELETE** /repos/{owner}/{repo}/contents/{filepath} | Delete a file in a repository
[**repo_delete_git_hook**](RepositoryApi.md#repo_delete_git_hook) | **DELETE** /repos/{owner}/{repo}/hooks/git/{id} | Delete a Git hook in a repository
[**repo_delete_hook**](RepositoryApi.md#repo_delete_hook) | **DELETE** /repos/{owner}/{repo}/hooks/{id} | Delete a hook in a repository
[**repo_delete_key**](RepositoryApi.md#repo_delete_key) | **DELETE** /repos/{owner}/{repo}/keys/{id} | Delete a key from a repository
[**repo_delete_pull_review**](RepositoryApi.md#repo_delete_pull_review) | **DELETE** /repos/{owner}/{repo}/pulls/{index}/reviews/{id} | Delete a specific review from a pull request
[**repo_delete_pull_review_requests**](RepositoryApi.md#repo_delete_pull_review_requests) | **DELETE** /repos/{owner}/{repo}/pulls/{index}/requested_reviewers | cancel review requests for a pull request
[**repo_delete_push_mirror**](RepositoryApi.md#repo_delete_push_mirror) | **DELETE** /repos/{owner}/{repo}/push_mirrors/{name} | deletes a push mirror from a repository by remoteName
[**repo_delete_release**](RepositoryApi.md#repo_delete_release) | **DELETE** /repos/{owner}/{repo}/releases/{id} | Delete a release
[**repo_delete_release_attachment**](RepositoryApi.md#repo_delete_release_attachment) | **DELETE** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Delete a release attachment
[**repo_delete_release_by_tag**](RepositoryApi.md#repo_delete_release_by_tag) | **DELETE** /repos/{owner}/{repo}/releases/tags/{tag} | Delete a release by tag name
[**repo_delete_tag**](RepositoryApi.md#repo_delete_tag) | **DELETE** /repos/{owner}/{repo}/tags/{tag} | Delete a repository&#39;s tag by name
[**repo_delete_tag_protection**](RepositoryApi.md#repo_delete_tag_protection) | **DELETE** /repos/{owner}/{repo}/tag_protections/{id} | Delete a specific tag protection for the repository
[**repo_delete_team**](RepositoryApi.md#repo_delete_team) | **DELETE** /repos/{owner}/{repo}/teams/{team} | Delete a team from a repository
[**repo_delete_topic**](RepositoryApi.md#repo_delete_topic) | **DELETE** /repos/{owner}/{repo}/topics/{topic} | Delete a topic from a repository
[**repo_delete_wiki_page**](RepositoryApi.md#repo_delete_wiki_page) | **DELETE** /repos/{owner}/{repo}/wiki/page/{pageName} | Delete a wiki page
[**repo_dismiss_pull_review**](RepositoryApi.md#repo_dismiss_pull_review) | **POST** /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals | Dismiss a review for a pull request
[**repo_download_commit_diff_or_patch**](RepositoryApi.md#repo_download_commit_diff_or_patch) | **GET** /repos/{owner}/{repo}/git/commits/{sha}.{diffType} | Get a commit&#39;s diff or patch
[**repo_download_pull_diff_or_patch**](RepositoryApi.md#repo_download_pull_diff_or_patch) | **GET** /repos/{owner}/{repo}/pulls/{index}.{diffType} | Get a pull request diff or patch
[**repo_edit**](RepositoryApi.md#repo_edit) | **PATCH** /repos/{owner}/{repo} | Edit a repository&#39;s properties. Only fields that are set will be changed.
[**repo_edit_branch_protection**](RepositoryApi.md#repo_edit_branch_protection) | **PATCH** /repos/{owner}/{repo}/branch_protections/{name} | Edit a branch protections for a repository. Only fields that are set will be changed
[**repo_edit_git_hook**](RepositoryApi.md#repo_edit_git_hook) | **PATCH** /repos/{owner}/{repo}/hooks/git/{id} | Edit a Git hook in a repository
[**repo_edit_hook**](RepositoryApi.md#repo_edit_hook) | **PATCH** /repos/{owner}/{repo}/hooks/{id} | Edit a hook in a repository
[**repo_edit_pull_request**](RepositoryApi.md#repo_edit_pull_request) | **PATCH** /repos/{owner}/{repo}/pulls/{index} | Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.
[**repo_edit_release**](RepositoryApi.md#repo_edit_release) | **PATCH** /repos/{owner}/{repo}/releases/{id} | Update a release
[**repo_edit_release_attachment**](RepositoryApi.md#repo_edit_release_attachment) | **PATCH** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Edit a release attachment
[**repo_edit_tag_protection**](RepositoryApi.md#repo_edit_tag_protection) | **PATCH** /repos/{owner}/{repo}/tag_protections/{id} | Edit a tag protections for a repository. Only fields that are set will be changed
[**repo_edit_wiki_page**](RepositoryApi.md#repo_edit_wiki_page) | **PATCH** /repos/{owner}/{repo}/wiki/page/{pageName} | Edit a wiki page
[**repo_get**](RepositoryApi.md#repo_get) | **GET** /repos/{owner}/{repo} | Get a repository
[**repo_get_all_commits**](RepositoryApi.md#repo_get_all_commits) | **GET** /repos/{owner}/{repo}/commits | Get a list of all commits from a repository
[**repo_get_archive**](RepositoryApi.md#repo_get_archive) | **GET** /repos/{owner}/{repo}/archive/{archive} | Get an archive of a repository
[**repo_get_assignees**](RepositoryApi.md#repo_get_assignees) | **GET** /repos/{owner}/{repo}/assignees | Return all users that have write access and can be assigned to issues
[**repo_get_branch**](RepositoryApi.md#repo_get_branch) | **GET** /repos/{owner}/{repo}/branches/{branch} | Retrieve a specific branch from a repository, including its effective branch protection
[**repo_get_branch_protection**](RepositoryApi.md#repo_get_branch_protection) | **GET** /repos/{owner}/{repo}/branch_protections/{name} | Get a specific branch protection for the repository
[**repo_get_by_id**](RepositoryApi.md#repo_get_by_id) | **GET** /repositories/{id} | Get a repository by id
[**repo_get_combined_status_by_ref**](RepositoryApi.md#repo_get_combined_status_by_ref) | **GET** /repos/{owner}/{repo}/commits/{ref}/status | Get a commit&#39;s combined status, by branch/tag/commit reference
[**repo_get_commit_pull_request**](RepositoryApi.md#repo_get_commit_pull_request) | **GET** /repos/{owner}/{repo}/commits/{sha}/pull | Get the merged pull request of the commit
[**repo_get_contents**](RepositoryApi.md#repo_get_contents) | **GET** /repos/{owner}/{repo}/contents/{filepath} | Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir
[**repo_get_contents_list**](RepositoryApi.md#repo_get_contents_list) | **GET** /repos/{owner}/{repo}/contents | Gets the metadata of all the entries of the root dir
[**repo_get_editor_config**](RepositoryApi.md#repo_get_editor_config) | **GET** /repos/{owner}/{repo}/editorconfig/{filepath} | Get the EditorConfig definitions of a file in a repository
[**repo_get_file_contents**](RepositoryApi.md#repo_get_file_contents) | **GET** /repos/{owner}/{repo}/file-contents | Get the metadata and contents of requested files
[**repo_get_file_contents_post**](RepositoryApi.md#repo_get_file_contents_post) | **POST** /repos/{owner}/{repo}/file-contents | Get the metadata and contents of requested files
[**repo_get_git_hook**](RepositoryApi.md#repo_get_git_hook) | **GET** /repos/{owner}/{repo}/hooks/git/{id} | Get a Git hook
[**repo_get_hook**](RepositoryApi.md#repo_get_hook) | **GET** /repos/{owner}/{repo}/hooks/{id} | Get a hook
[**repo_get_issue_config**](RepositoryApi.md#repo_get_issue_config) | **GET** /repos/{owner}/{repo}/issue_config | Returns the issue config for a repo
[**repo_get_issue_templates**](RepositoryApi.md#repo_get_issue_templates) | **GET** /repos/{owner}/{repo}/issue_templates | Get available issue templates for a repository
[**repo_get_key**](RepositoryApi.md#repo_get_key) | **GET** /repos/{owner}/{repo}/keys/{id} | Get a repository&#39;s key by id
[**repo_get_languages**](RepositoryApi.md#repo_get_languages) | **GET** /repos/{owner}/{repo}/languages | Get languages and number of bytes of code written
[**repo_get_latest_release**](RepositoryApi.md#repo_get_latest_release) | **GET** /repos/{owner}/{repo}/releases/latest | Gets the most recent non-prerelease, non-draft release of a repository, sorted by created_at
[**repo_get_licenses**](RepositoryApi.md#repo_get_licenses) | **GET** /repos/{owner}/{repo}/licenses | Get repo licenses
[**repo_get_note**](RepositoryApi.md#repo_get_note) | **GET** /repos/{owner}/{repo}/git/notes/{sha} | Get a note corresponding to a single commit from a repository
[**repo_get_pull_request**](RepositoryApi.md#repo_get_pull_request) | **GET** /repos/{owner}/{repo}/pulls/{index} | Get a pull request
[**repo_get_pull_request_by_base_head**](RepositoryApi.md#repo_get_pull_request_by_base_head) | **GET** /repos/{owner}/{repo}/pulls/{base}/{head} | Get a pull request by base and head
[**repo_get_pull_request_commits**](RepositoryApi.md#repo_get_pull_request_commits) | **GET** /repos/{owner}/{repo}/pulls/{index}/commits | Get commits for a pull request
[**repo_get_pull_request_files**](RepositoryApi.md#repo_get_pull_request_files) | **GET** /repos/{owner}/{repo}/pulls/{index}/files | Get changed files for a pull request
[**repo_get_pull_review**](RepositoryApi.md#repo_get_pull_review) | **GET** /repos/{owner}/{repo}/pulls/{index}/reviews/{id} | Get a specific review for a pull request
[**repo_get_pull_review_comments**](RepositoryApi.md#repo_get_pull_review_comments) | **GET** /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments | Get a specific review for a pull request
[**repo_get_push_mirror_by_remote_name**](RepositoryApi.md#repo_get_push_mirror_by_remote_name) | **GET** /repos/{owner}/{repo}/push_mirrors/{name} | Get push mirror of the repository by remoteName
[**repo_get_raw_file**](RepositoryApi.md#repo_get_raw_file) | **GET** /repos/{owner}/{repo}/raw/{filepath} | Get a file from a repository
[**repo_get_raw_file_or_lfs**](RepositoryApi.md#repo_get_raw_file_or_lfs) | **GET** /repos/{owner}/{repo}/media/{filepath} | Get a file or it&#39;s LFS object from a repository
[**repo_get_release**](RepositoryApi.md#repo_get_release) | **GET** /repos/{owner}/{repo}/releases/{id} | Get a release
[**repo_get_release_attachment**](RepositoryApi.md#repo_get_release_attachment) | **GET** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Get a release attachment
[**repo_get_release_by_tag**](RepositoryApi.md#repo_get_release_by_tag) | **GET** /repos/{owner}/{repo}/releases/tags/{tag} | Get a release by tag name
[**repo_get_repo_permissions**](RepositoryApi.md#repo_get_repo_permissions) | **GET** /repos/{owner}/{repo}/collaborators/{collaborator}/permission | Get repository permissions for a user
[**repo_get_reviewers**](RepositoryApi.md#repo_get_reviewers) | **GET** /repos/{owner}/{repo}/reviewers | Return all users that can be requested to review in this repo
[**repo_get_runner_registration_token**](RepositoryApi.md#repo_get_runner_registration_token) | **GET** /repos/{owner}/{repo}/actions/runners/registration-token | Get a repository&#39;s actions runner registration token
[**repo_get_single_commit**](RepositoryApi.md#repo_get_single_commit) | **GET** /repos/{owner}/{repo}/git/commits/{sha} | Get a single commit from a repository
[**repo_get_tag**](RepositoryApi.md#repo_get_tag) | **GET** /repos/{owner}/{repo}/tags/{tag} | Get the tag of a repository by tag name
[**repo_get_tag_protection**](RepositoryApi.md#repo_get_tag_protection) | **GET** /repos/{owner}/{repo}/tag_protections/{id} | Get a specific tag protection for the repository
[**repo_get_wiki_page**](RepositoryApi.md#repo_get_wiki_page) | **GET** /repos/{owner}/{repo}/wiki/page/{pageName} | Get a wiki page
[**repo_get_wiki_page_revisions**](RepositoryApi.md#repo_get_wiki_page_revisions) | **GET** /repos/{owner}/{repo}/wiki/revisions/{pageName} | Get revisions of a wiki page
[**repo_get_wiki_pages**](RepositoryApi.md#repo_get_wiki_pages) | **GET** /repos/{owner}/{repo}/wiki/pages | Get all wiki pages
[**repo_list_actions_secrets**](RepositoryApi.md#repo_list_actions_secrets) | **GET** /repos/{owner}/{repo}/actions/secrets | List an repo&#39;s actions secrets
[**repo_list_activity_feeds**](RepositoryApi.md#repo_list_activity_feeds) | **GET** /repos/{owner}/{repo}/activities/feeds | List a repository&#39;s activity feeds
[**repo_list_all_git_refs**](RepositoryApi.md#repo_list_all_git_refs) | **GET** /repos/{owner}/{repo}/git/refs | Get specified ref or filtered repository&#39;s refs
[**repo_list_branch_protection**](RepositoryApi.md#repo_list_branch_protection) | **GET** /repos/{owner}/{repo}/branch_protections | List branch protections for a repository
[**repo_list_branches**](RepositoryApi.md#repo_list_branches) | **GET** /repos/{owner}/{repo}/branches | List a repository&#39;s branches
[**repo_list_collaborators**](RepositoryApi.md#repo_list_collaborators) | **GET** /repos/{owner}/{repo}/collaborators | List a repository&#39;s collaborators
[**repo_list_git_hooks**](RepositoryApi.md#repo_list_git_hooks) | **GET** /repos/{owner}/{repo}/hooks/git | List the Git hooks in a repository
[**repo_list_git_refs**](RepositoryApi.md#repo_list_git_refs) | **GET** /repos/{owner}/{repo}/git/refs/{ref} | Get specified ref or filtered repository&#39;s refs
[**repo_list_hooks**](RepositoryApi.md#repo_list_hooks) | **GET** /repos/{owner}/{repo}/hooks | List the hooks in a repository
[**repo_list_keys**](RepositoryApi.md#repo_list_keys) | **GET** /repos/{owner}/{repo}/keys | List a repository&#39;s keys
[**repo_list_pinned_issues**](RepositoryApi.md#repo_list_pinned_issues) | **GET** /repos/{owner}/{repo}/issues/pinned | List a repo&#39;s pinned issues
[**repo_list_pinned_pull_requests**](RepositoryApi.md#repo_list_pinned_pull_requests) | **GET** /repos/{owner}/{repo}/pulls/pinned | List a repo&#39;s pinned pull requests
[**repo_list_pull_requests**](RepositoryApi.md#repo_list_pull_requests) | **GET** /repos/{owner}/{repo}/pulls | List a repo&#39;s pull requests
[**repo_list_pull_reviews**](RepositoryApi.md#repo_list_pull_reviews) | **GET** /repos/{owner}/{repo}/pulls/{index}/reviews | List all reviews for a pull request
[**repo_list_push_mirrors**](RepositoryApi.md#repo_list_push_mirrors) | **GET** /repos/{owner}/{repo}/push_mirrors | Get all push mirrors of the repository
[**repo_list_release_attachments**](RepositoryApi.md#repo_list_release_attachments) | **GET** /repos/{owner}/{repo}/releases/{id}/assets | List release&#39;s attachments
[**repo_list_releases**](RepositoryApi.md#repo_list_releases) | **GET** /repos/{owner}/{repo}/releases | List a repo&#39;s releases
[**repo_list_stargazers**](RepositoryApi.md#repo_list_stargazers) | **GET** /repos/{owner}/{repo}/stargazers | List a repo&#39;s stargazers
[**repo_list_statuses**](RepositoryApi.md#repo_list_statuses) | **GET** /repos/{owner}/{repo}/statuses/{sha} | Get a commit&#39;s statuses
[**repo_list_statuses_by_ref**](RepositoryApi.md#repo_list_statuses_by_ref) | **GET** /repos/{owner}/{repo}/commits/{ref}/statuses | Get a commit&#39;s statuses, by branch/tag/commit reference
[**repo_list_subscribers**](RepositoryApi.md#repo_list_subscribers) | **GET** /repos/{owner}/{repo}/subscribers | List a repo&#39;s watchers
[**repo_list_tag_protection**](RepositoryApi.md#repo_list_tag_protection) | **GET** /repos/{owner}/{repo}/tag_protections | List tag protections for a repository
[**repo_list_tags**](RepositoryApi.md#repo_list_tags) | **GET** /repos/{owner}/{repo}/tags | List a repository&#39;s tags
[**repo_list_teams**](RepositoryApi.md#repo_list_teams) | **GET** /repos/{owner}/{repo}/teams | List a repository&#39;s teams
[**repo_list_topics**](RepositoryApi.md#repo_list_topics) | **GET** /repos/{owner}/{repo}/topics | Get list of topics that a repository has
[**repo_merge_pull_request**](RepositoryApi.md#repo_merge_pull_request) | **POST** /repos/{owner}/{repo}/pulls/{index}/merge | Merge a pull request
[**repo_merge_upstream**](RepositoryApi.md#repo_merge_upstream) | **POST** /repos/{owner}/{repo}/merge-upstream | Merge a branch from upstream
[**repo_migrate**](RepositoryApi.md#repo_migrate) | **POST** /repos/migrate | Migrate a remote git repository
[**repo_mirror_sync**](RepositoryApi.md#repo_mirror_sync) | **POST** /repos/{owner}/{repo}/mirror-sync | Sync a mirrored repository
[**repo_new_pin_allowed**](RepositoryApi.md#repo_new_pin_allowed) | **GET** /repos/{owner}/{repo}/new_pin_allowed | Returns if new Issue Pins are allowed
[**repo_pull_request_is_merged**](RepositoryApi.md#repo_pull_request_is_merged) | **GET** /repos/{owner}/{repo}/pulls/{index}/merge | Check if a pull request has been merged
[**repo_push_mirror_sync**](RepositoryApi.md#repo_push_mirror_sync) | **POST** /repos/{owner}/{repo}/push_mirrors-sync | Sync all push mirrored repository
[**repo_search**](RepositoryApi.md#repo_search) | **GET** /repos/search | Search for repositories
[**repo_signing_key**](RepositoryApi.md#repo_signing_key) | **GET** /repos/{owner}/{repo}/signing-key.gpg | Get signing-key.gpg for given repository
[**repo_submit_pull_review**](RepositoryApi.md#repo_submit_pull_review) | **POST** /repos/{owner}/{repo}/pulls/{index}/reviews/{id} | Submit a pending review to an pull request
[**repo_test_hook**](RepositoryApi.md#repo_test_hook) | **POST** /repos/{owner}/{repo}/hooks/{id}/tests | Test a push webhook
[**repo_tracked_times**](RepositoryApi.md#repo_tracked_times) | **GET** /repos/{owner}/{repo}/times | List a repo&#39;s tracked times
[**repo_transfer**](RepositoryApi.md#repo_transfer) | **POST** /repos/{owner}/{repo}/transfer | Transfer a repo ownership
[**repo_un_dismiss_pull_review**](RepositoryApi.md#repo_un_dismiss_pull_review) | **POST** /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals | Cancel to dismiss a review for a pull request
[**repo_update_avatar**](RepositoryApi.md#repo_update_avatar) | **POST** /repos/{owner}/{repo}/avatar | Update avatar
[**repo_update_branch**](RepositoryApi.md#repo_update_branch) | **PATCH** /repos/{owner}/{repo}/branches/{branch} | Update a branch
[**repo_update_branch_protection_priories**](RepositoryApi.md#repo_update_branch_protection_priories) | **POST** /repos/{owner}/{repo}/branch_protections/priority | Update the priorities of branch protections for a repository.
[**repo_update_file**](RepositoryApi.md#repo_update_file) | **PUT** /repos/{owner}/{repo}/contents/{filepath} | Update a file in a repository
[**repo_update_pull_request**](RepositoryApi.md#repo_update_pull_request) | **POST** /repos/{owner}/{repo}/pulls/{index}/update | Merge PR&#39;s baseBranch into headBranch
[**repo_update_topics**](RepositoryApi.md#repo_update_topics) | **PUT** /repos/{owner}/{repo}/topics | Replace list of topics for a repository
[**repo_validate_issue_config**](RepositoryApi.md#repo_validate_issue_config) | **GET** /repos/{owner}/{repo}/issue_config/validate | Returns the validation information for a issue config
[**topic_search**](RepositoryApi.md#topic_search) | **GET** /topics/search | search topics via keyword
[**update_repo_secret**](RepositoryApi.md#update_repo_secret) | **PUT** /repos/{owner}/{repo}/actions/secrets/{secretname} | Create or Update a secret value in a repository
[**update_repo_variable**](RepositoryApi.md#update_repo_variable) | **PUT** /repos/{owner}/{repo}/actions/variables/{variablename} | Update a repo-level variable
[**user_current_check_subscription**](RepositoryApi.md#user_current_check_subscription) | **GET** /repos/{owner}/{repo}/subscription | Check if the current user is watching a repo
[**user_current_delete_subscription**](RepositoryApi.md#user_current_delete_subscription) | **DELETE** /repos/{owner}/{repo}/subscription | Unwatch a repo
[**user_current_put_subscription**](RepositoryApi.md#user_current_put_subscription) | **PUT** /repos/{owner}/{repo}/subscription | Watch a repo
[**user_tracked_times**](RepositoryApi.md#user_tracked_times) | **GET** /repos/{owner}/{repo}/times/{user} | List a user&#39;s tracked times in a repo


# **accept_repo_transfer**
> Repository accept_repo_transfer(owner, repo)

Accept a repo transfer

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.repository import Repository
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo to transfer
    repo = 'repo_example' # str | name of the repo to transfer

    try:
        # Accept a repo transfer
        api_response = api_instance.accept_repo_transfer(owner, repo)
        print("The response of RepositoryApi->accept_repo_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->accept_repo_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to transfer | 
 **repo** | **str**| name of the repo to transfer | 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_disable_workflow**
> actions_disable_workflow(owner, repo, workflow_id)

Disable a workflow

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    workflow_id = 'workflow_id_example' # str | id of the workflow

    try:
        # Disable a workflow
        api_instance.actions_disable_workflow(owner, repo, workflow_id)
    except Exception as e:
        print("Exception when calling RepositoryApi->actions_disable_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **workflow_id** | **str**| id of the workflow | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_dispatch_workflow**
> actions_dispatch_workflow(owner, repo, workflow_id, body=body)

Create a workflow dispatch event

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_action_workflow_dispatch import CreateActionWorkflowDispatch
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    workflow_id = 'workflow_id_example' # str | id of the workflow
    body = gitea_api.CreateActionWorkflowDispatch() # CreateActionWorkflowDispatch |  (optional)

    try:
        # Create a workflow dispatch event
        api_instance.actions_dispatch_workflow(owner, repo, workflow_id, body=body)
    except Exception as e:
        print("Exception when calling RepositoryApi->actions_dispatch_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **workflow_id** | **str**| id of the workflow | 
 **body** | [**CreateActionWorkflowDispatch**](CreateActionWorkflowDispatch.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_enable_workflow**
> actions_enable_workflow(owner, repo, workflow_id)

Enable a workflow

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    workflow_id = 'workflow_id_example' # str | id of the workflow

    try:
        # Enable a workflow
        api_instance.actions_enable_workflow(owner, repo, workflow_id)
    except Exception as e:
        print("Exception when calling RepositoryApi->actions_enable_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **workflow_id** | **str**| id of the workflow | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**409** | APIConflict is a conflict empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_get_workflow**
> ActionWorkflow actions_get_workflow(owner, repo, workflow_id)

Get a workflow

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.action_workflow import ActionWorkflow
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    workflow_id = 'workflow_id_example' # str | id of the workflow

    try:
        # Get a workflow
        api_response = api_instance.actions_get_workflow(owner, repo, workflow_id)
        print("The response of RepositoryApi->actions_get_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->actions_get_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **workflow_id** | **str**| id of the workflow | 

### Return type

[**ActionWorkflow**](ActionWorkflow.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActionWorkflow |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |
**500** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_list_repository_workflows**
> ActionWorkflowResponse actions_list_repository_workflows(owner, repo)

List repository workflows

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.action_workflow_response import ActionWorkflowResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # List repository workflows
        api_response = api_instance.actions_list_repository_workflows(owner, repo)
        print("The response of RepositoryApi->actions_list_repository_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->actions_list_repository_workflows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**ActionWorkflowResponse**](ActionWorkflowResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActionWorkflowList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |
**500** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_current_user_repo**
> Repository create_current_user_repo(body=body)

Create a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_repo_option import CreateRepoOption
from gitea_api.models.repository import Repository
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    body = gitea_api.CreateRepoOption() # CreateRepoOption |  (optional)

    try:
        # Create a repository
        api_response = api_instance.create_current_user_repo(body=body)
        print("The response of RepositoryApi->create_current_user_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->create_current_user_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRepoOption**](CreateRepoOption.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Repository |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**409** | The repository with the same name already exists. |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fork**
> Repository create_fork(owner, repo, body=body)

Fork a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_fork_option import CreateForkOption
from gitea_api.models.repository import Repository
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo to fork
    repo = 'repo_example' # str | name of the repo to fork
    body = gitea_api.CreateForkOption() # CreateForkOption |  (optional)

    try:
        # Fork a repository
        api_response = api_instance.create_fork(owner, repo, body=body)
        print("The response of RepositoryApi->create_fork:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->create_fork: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to fork | 
 **repo** | **str**| name of the repo to fork | 
 **body** | [**CreateForkOption**](CreateForkOption.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**409** | The repository with the same name already exists. |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repo_variable**
> create_repo_variable(owner, repo, variablename, body=body)

Create a repo-level variable

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_variable_option import CreateVariableOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | name of the owner
    repo = 'repo_example' # str | name of the repository
    variablename = 'variablename_example' # str | name of the variable
    body = gitea_api.CreateVariableOption() # CreateVariableOption |  (optional)

    try:
        # Create a repo-level variable
        api_instance.create_repo_variable(owner, repo, variablename, body=body)
    except Exception as e:
        print("Exception when calling RepositoryApi->create_repo_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repository | 
 **variablename** | **str**| name of the variable | 
 **body** | [**CreateVariableOption**](CreateVariableOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | response when creating a repo-level variable |  -  |
**204** | response when creating a repo-level variable |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact**
> delete_artifact(owner, repo, artifact_id)

Deletes a specific artifact for a workflow run

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | name of the owner
    repo = 'repo_example' # str | name of the repository
    artifact_id = 'artifact_id_example' # str | id of the artifact

    try:
        # Deletes a specific artifact for a workflow run
        api_instance.delete_artifact(owner, repo, artifact_id)
    except Exception as e:
        print("Exception when calling RepositoryApi->delete_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repository | 
 **artifact_id** | **str**| id of the artifact | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repo_runner**
> delete_repo_runner(owner, repo, runner_id)

Delete an repo-level runner

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    runner_id = 'runner_id_example' # str | id of the runner

    try:
        # Delete an repo-level runner
        api_instance.delete_repo_runner(owner, repo, runner_id)
    except Exception as e:
        print("Exception when calling RepositoryApi->delete_repo_runner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **runner_id** | **str**| id of the runner | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | runner has been deleted |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repo_secret**
> delete_repo_secret(owner, repo, secretname)

Delete a secret in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repository
    repo = 'repo_example' # str | name of the repository
    secretname = 'secretname_example' # str | name of the secret

    try:
        # Delete a secret in a repository
        api_instance.delete_repo_secret(owner, repo, secretname)
    except Exception as e:
        print("Exception when calling RepositoryApi->delete_repo_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repository | 
 **repo** | **str**| name of the repository | 
 **secretname** | **str**| name of the secret | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | delete one secret of the repository |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repo_variable**
> ActionVariable delete_repo_variable(owner, repo, variablename)

Delete a repo-level variable

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.action_variable import ActionVariable
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | name of the owner
    repo = 'repo_example' # str | name of the repository
    variablename = 'variablename_example' # str | name of the variable

    try:
        # Delete a repo-level variable
        api_response = api_instance.delete_repo_variable(owner, repo, variablename)
        print("The response of RepositoryApi->delete_repo_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->delete_repo_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repository | 
 **variablename** | **str**| name of the variable | 

### Return type

[**ActionVariable**](ActionVariable.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActionVariable |  -  |
**201** | response when deleting a variable |  -  |
**204** | response when deleting a variable |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_actions_run_job_logs**
> download_actions_run_job_logs(owner, repo, job_id)

Downloads the job logs for a workflow run

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | name of the owner
    repo = 'repo_example' # str | name of the repository
    job_id = 56 # int | id of the job

    try:
        # Downloads the job logs for a workflow run
        api_instance.download_actions_run_job_logs(owner, repo, job_id)
    except Exception as e:
        print("Exception when calling RepositoryApi->download_actions_run_job_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repository | 
 **job_id** | **int**| id of the job | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | output blob content |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_artifact**
> download_artifact(owner, repo, artifact_id)

Downloads a specific artifact for a workflow run redirects to blob url

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | name of the owner
    repo = 'repo_example' # str | name of the repository
    artifact_id = 'artifact_id_example' # str | id of the artifact

    try:
        # Downloads a specific artifact for a workflow run redirects to blob url
        api_instance.download_artifact(owner, repo, artifact_id)
    except Exception as e:
        print("Exception when calling RepositoryApi->download_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repository | 
 **artifact_id** | **str**| id of the artifact | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | redirect to the blob download |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_repo**
> Repository generate_repo(template_owner, template_repo, body=body)

Create a repository using a template

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.generate_repo_option import GenerateRepoOption
from gitea_api.models.repository import Repository
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    template_owner = 'template_owner_example' # str | name of the template repository owner
    template_repo = 'template_repo_example' # str | name of the template repository
    body = gitea_api.GenerateRepoOption() # GenerateRepoOption |  (optional)

    try:
        # Create a repository using a template
        api_response = api_instance.generate_repo(template_owner, template_repo, body=body)
        print("The response of RepositoryApi->generate_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->generate_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_owner** | **str**| name of the template repository owner | 
 **template_repo** | **str**| name of the template repository | 
 **body** | [**GenerateRepoOption**](GenerateRepoOption.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**409** | The repository with the same name already exists. |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_annotated_tag**
> AnnotatedTag get_annotated_tag(owner, repo, sha)

Gets the tag object of an annotated tag (not lightweight tags)

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.annotated_tag import AnnotatedTag
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    sha = 'sha_example' # str | sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags.

    try:
        # Gets the tag object of an annotated tag (not lightweight tags)
        api_response = api_instance.get_annotated_tag(owner, repo, sha)
        print("The response of RepositoryApi->get_annotated_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_annotated_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags. | 

### Return type

[**AnnotatedTag**](AnnotatedTag.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AnnotatedTag |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact**
> ActionArtifact get_artifact(owner, repo, artifact_id)

Gets a specific artifact for a workflow run

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.action_artifact import ActionArtifact
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | name of the owner
    repo = 'repo_example' # str | name of the repository
    artifact_id = 'artifact_id_example' # str | id of the artifact

    try:
        # Gets a specific artifact for a workflow run
        api_response = api_instance.get_artifact(owner, repo, artifact_id)
        print("The response of RepositoryApi->get_artifact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_artifact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repository | 
 **artifact_id** | **str**| id of the artifact | 

### Return type

[**ActionArtifact**](ActionArtifact.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Artifact |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifacts**
> ActionArtifactsResponse get_artifacts(owner, repo, name=name)

Lists all artifacts for a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.action_artifacts_response import ActionArtifactsResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | name of the owner
    repo = 'repo_example' # str | name of the repository
    name = 'name_example' # str | name of the artifact (optional)

    try:
        # Lists all artifacts for a repository
        api_response = api_instance.get_artifacts(owner, repo, name=name)
        print("The response of RepositoryApi->get_artifacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_artifacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repository | 
 **name** | **str**| name of the artifact | [optional] 

### Return type

[**ActionArtifactsResponse**](ActionArtifactsResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ArtifactsList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifacts_of_run**
> ActionArtifactsResponse get_artifacts_of_run(owner, repo, run, name=name)

Lists all artifacts for a repository run

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.action_artifacts_response import ActionArtifactsResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | name of the owner
    repo = 'repo_example' # str | name of the repository
    run = 56 # int | runid of the workflow run
    name = 'name_example' # str | name of the artifact (optional)

    try:
        # Lists all artifacts for a repository run
        api_response = api_instance.get_artifacts_of_run(owner, repo, run, name=name)
        print("The response of RepositoryApi->get_artifacts_of_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_artifacts_of_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repository | 
 **run** | **int**| runid of the workflow run | 
 **name** | **str**| name of the artifact | [optional] 

### Return type

[**ActionArtifactsResponse**](ActionArtifactsResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ArtifactsList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blob**
> GitBlobResponse get_blob(owner, repo, sha)

Gets the blob of a repository.

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.git_blob_response import GitBlobResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    sha = 'sha_example' # str | sha of the commit

    try:
        # Gets the blob of a repository.
        api_response = api_instance.get_blob(owner, repo, sha)
        print("The response of RepositoryApi->get_blob:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_blob: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| sha of the commit | 

### Return type

[**GitBlobResponse**](GitBlobResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GitBlobResponse |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_runner**
> get_repo_runner(owner, repo, runner_id)

Get an repo-level runner

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    runner_id = 'runner_id_example' # str | id of the runner

    try:
        # Get an repo-level runner
        api_instance.get_repo_runner(owner, repo, runner_id)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_repo_runner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **runner_id** | **str**| id of the runner | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_runners**
> get_repo_runners(owner, repo)

Get repo-level runners

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Get repo-level runners
        api_instance.get_repo_runners(owner, repo)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_repo_runners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_variable**
> ActionVariable get_repo_variable(owner, repo, variablename)

Get a repo-level variable

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.action_variable import ActionVariable
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | name of the owner
    repo = 'repo_example' # str | name of the repository
    variablename = 'variablename_example' # str | name of the variable

    try:
        # Get a repo-level variable
        api_response = api_instance.get_repo_variable(owner, repo, variablename)
        print("The response of RepositoryApi->get_repo_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_repo_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repository | 
 **variablename** | **str**| name of the variable | 

### Return type

[**ActionVariable**](ActionVariable.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActionVariable |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo_variables_list**
> List[ActionVariable] get_repo_variables_list(owner, repo, page=page, limit=limit)

Get repo-level variables list

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.action_variable import ActionVariable
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | name of the owner
    repo = 'repo_example' # str | name of the repository
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Get repo-level variables list
        api_response = api_instance.get_repo_variables_list(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->get_repo_variables_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_repo_variables_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repository | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[ActionVariable]**](ActionVariable.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VariableList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree**
> GitTreeResponse get_tree(owner, repo, sha, recursive=recursive, page=page, per_page=per_page)

Gets the tree of a repository.

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.git_tree_response import GitTreeResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    sha = 'sha_example' # str | sha of the commit
    recursive = True # bool | show all directories and files (optional)
    page = 56 # int | page number; the 'truncated' field in the response will be true if there are still more items after this page, false if the last page (optional)
    per_page = 56 # int | number of items per page (optional)

    try:
        # Gets the tree of a repository.
        api_response = api_instance.get_tree(owner, repo, sha, recursive=recursive, page=page, per_page=per_page)
        print("The response of RepositoryApi->get_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_tree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| sha of the commit | 
 **recursive** | **bool**| show all directories and files | [optional] 
 **page** | **int**| page number; the &#39;truncated&#39; field in the response will be true if there are still more items after this page, false if the last page | [optional] 
 **per_page** | **int**| number of items per page | [optional] 

### Return type

[**GitTreeResponse**](GitTreeResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GitTreeResponse |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_action_tasks**
> ActionTaskResponse list_action_tasks(owner, repo, page=page, limit=limit)

List a repository's action tasks

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.action_task_response import ActionTaskResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results, default maximum page size is 50 (optional)

    try:
        # List a repository's action tasks
        api_response = api_instance.list_action_tasks(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->list_action_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->list_action_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results, default maximum page size is 50 | [optional] 

### Return type

[**ActionTaskResponse**](ActionTaskResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TasksList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**409** | APIConflict is a conflict empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_forks**
> List[Repository] list_forks(owner, repo, page=page, limit=limit)

List a repository's forks

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.repository import Repository
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a repository's forks
        api_response = api_instance.list_forks(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->list_forks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->list_forks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Repository]**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RepositoryList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_repo_transfer**
> Repository reject_repo_transfer(owner, repo)

Reject a repo transfer

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.repository import Repository
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo to transfer
    repo = 'repo_example' # str | name of the repo to transfer

    try:
        # Reject a repo transfer
        api_response = api_instance.reject_repo_transfer(owner, repo)
        print("The response of RepositoryApi->reject_repo_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->reject_repo_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to transfer | 
 **repo** | **str**| name of the repo to transfer | 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_add_collaborator**
> repo_add_collaborator(owner, repo, collaborator, body=body)

Add or Update a collaborator to a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.add_collaborator_option import AddCollaboratorOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    collaborator = 'collaborator_example' # str | username of the collaborator to add
    body = gitea_api.AddCollaboratorOption() # AddCollaboratorOption |  (optional)

    try:
        # Add or Update a collaborator to a repository
        api_instance.repo_add_collaborator(owner, repo, collaborator, body=body)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_add_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **collaborator** | **str**| username of the collaborator to add | 
 **body** | [**AddCollaboratorOption**](AddCollaboratorOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_add_push_mirror**
> PushMirror repo_add_push_mirror(owner, repo, body=body)

add a push mirror to the repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_push_mirror_option import CreatePushMirrorOption
from gitea_api.models.push_mirror import PushMirror
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.CreatePushMirrorOption() # CreatePushMirrorOption |  (optional)

    try:
        # add a push mirror to the repository
        api_response = api_instance.repo_add_push_mirror(owner, repo, body=body)
        print("The response of RepositoryApi->repo_add_push_mirror:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_add_push_mirror: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreatePushMirrorOption**](CreatePushMirrorOption.md)|  | [optional] 

### Return type

[**PushMirror**](PushMirror.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PushMirror |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_add_team**
> repo_add_team(owner, repo, team)

Add a team to a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    team = 'team_example' # str | team name

    try:
        # Add a team to a repository
        api_instance.repo_add_team(owner, repo, team)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_add_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **team** | **str**| team name | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**405** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_add_topic**
> repo_add_topic(owner, repo, topic)

Add a topic to a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    topic = 'topic_example' # str | name of the topic to add

    try:
        # Add a topic to a repository
        api_instance.repo_add_topic(owner, repo, topic)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_add_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **topic** | **str**| name of the topic to add | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIInvalidTopicsError is error format response to invalid topics |  * invalidTopics -  <br>  * message -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_apply_diff_patch**
> FileResponse repo_apply_diff_patch(owner, repo, body)

Apply diff patch to repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.file_response import FileResponse
from gitea_api.models.update_file_options import UpdateFileOptions
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.UpdateFileOptions() # UpdateFileOptions | 

    try:
        # Apply diff patch to repository
        api_response = api_instance.repo_apply_diff_patch(owner, repo, body)
        print("The response of RepositoryApi->repo_apply_diff_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_apply_diff_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**UpdateFileOptions**](UpdateFileOptions.md)|  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FileResponse |  -  |
**404** | APINotFound is a not found empty response |  -  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_cancel_scheduled_auto_merge**
> repo_cancel_scheduled_auto_merge(owner, repo, index)

Cancel the scheduled auto merge for the given pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request to merge

    try:
        # Cancel the scheduled auto merge for the given pull request
        api_instance.repo_cancel_scheduled_auto_merge(owner, repo, index)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_cancel_scheduled_auto_merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request to merge | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_change_files**
> FilesResponse repo_change_files(owner, repo, body)

Modify multiple files in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.change_files_options import ChangeFilesOptions
from gitea_api.models.files_response import FilesResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.ChangeFilesOptions() # ChangeFilesOptions | 

    try:
        # Modify multiple files in a repository
        api_response = api_instance.repo_change_files(owner, repo, body)
        print("The response of RepositoryApi->repo_change_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_change_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**ChangeFilesOptions**](ChangeFilesOptions.md)|  | 

### Return type

[**FilesResponse**](FilesResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | FilesResponse |  -  |
**403** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_check_collaborator**
> repo_check_collaborator(owner, repo, collaborator)

Check if a user is a collaborator of a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    collaborator = 'collaborator_example' # str | username of the collaborator

    try:
        # Check if a user is a collaborator of a repository
        api_instance.repo_check_collaborator(owner, repo, collaborator)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_check_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **collaborator** | **str**| username of the collaborator | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_check_team**
> Team repo_check_team(owner, repo, team)

Check if a team is assigned to a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.team import Team
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    team = 'team_example' # str | team name

    try:
        # Check if a team is assigned to a repository
        api_response = api_instance.repo_check_team(owner, repo, team)
        print("The response of RepositoryApi->repo_check_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_check_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **team** | **str**| team name | 

### Return type

[**Team**](Team.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team |  -  |
**404** | APINotFound is a not found empty response |  -  |
**405** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_compare_diff**
> Compare repo_compare_diff(owner, repo, basehead)

Get commit comparison information

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.compare import Compare
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    basehead = 'basehead_example' # str | compare two branches or commits

    try:
        # Get commit comparison information
        api_response = api_instance.repo_compare_diff(owner, repo, basehead)
        print("The response of RepositoryApi->repo_compare_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_compare_diff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **basehead** | **str**| compare two branches or commits | 

### Return type

[**Compare**](Compare.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_branch**
> Branch repo_create_branch(owner, repo, body=body)

Create a branch

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.branch import Branch
from gitea_api.models.create_branch_repo_option import CreateBranchRepoOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.CreateBranchRepoOption() # CreateBranchRepoOption |  (optional)

    try:
        # Create a branch
        api_response = api_instance.repo_create_branch(owner, repo, body=body)
        print("The response of RepositoryApi->repo_create_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreateBranchRepoOption**](CreateBranchRepoOption.md)|  | [optional] 

### Return type

[**Branch**](Branch.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Branch |  -  |
**403** | The branch is archived or a mirror. |  -  |
**404** | The old branch does not exist. |  -  |
**409** | The branch with the same name already exists. |  -  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_branch_protection**
> BranchProtection repo_create_branch_protection(owner, repo, body=body)

Create a branch protections for a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.branch_protection import BranchProtection
from gitea_api.models.create_branch_protection_option import CreateBranchProtectionOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.CreateBranchProtectionOption() # CreateBranchProtectionOption |  (optional)

    try:
        # Create a branch protections for a repository
        api_response = api_instance.repo_create_branch_protection(owner, repo, body=body)
        print("The response of RepositoryApi->repo_create_branch_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreateBranchProtectionOption**](CreateBranchProtectionOption.md)|  | [optional] 

### Return type

[**BranchProtection**](BranchProtection.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | BranchProtection |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_file**
> FileResponse repo_create_file(owner, repo, filepath, body)

Create a file in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_file_options import CreateFileOptions
from gitea_api.models.file_response import FileResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    filepath = 'filepath_example' # str | path of the file to create
    body = gitea_api.CreateFileOptions() # CreateFileOptions | 

    try:
        # Create a file in a repository
        api_response = api_instance.repo_create_file(owner, repo, filepath, body)
        print("The response of RepositoryApi->repo_create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| path of the file to create | 
 **body** | [**CreateFileOptions**](CreateFileOptions.md)|  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | FileResponse |  -  |
**403** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_hook**
> Hook repo_create_hook(owner, repo, body=body)

Create a hook

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_hook_option import CreateHookOption
from gitea_api.models.hook import Hook
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.CreateHookOption() # CreateHookOption |  (optional)

    try:
        # Create a hook
        api_response = api_instance.repo_create_hook(owner, repo, body=body)
        print("The response of RepositoryApi->repo_create_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreateHookOption**](CreateHookOption.md)|  | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Hook |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_key**
> DeployKey repo_create_key(owner, repo, body=body)

Add a key to a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_key_option import CreateKeyOption
from gitea_api.models.deploy_key import DeployKey
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.CreateKeyOption() # CreateKeyOption |  (optional)

    try:
        # Add a key to a repository
        api_response = api_instance.repo_create_key(owner, repo, body=body)
        print("The response of RepositoryApi->repo_create_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreateKeyOption**](CreateKeyOption.md)|  | [optional] 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | DeployKey |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_pull_request**
> PullRequest repo_create_pull_request(owner, repo, body=body)

Create a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_pull_request_option import CreatePullRequestOption
from gitea_api.models.pull_request import PullRequest
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.CreatePullRequestOption() # CreatePullRequestOption |  (optional)

    try:
        # Create a pull request
        api_response = api_instance.repo_create_pull_request(owner, repo, body=body)
        print("The response of RepositoryApi->repo_create_pull_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreatePullRequestOption**](CreatePullRequestOption.md)|  | [optional] 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PullRequest |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**409** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_pull_review**
> PullReview repo_create_pull_review(owner, repo, index, body)

Create a review to an pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_pull_review_options import CreatePullReviewOptions
from gitea_api.models.pull_review import PullReview
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request
    body = gitea_api.CreatePullReviewOptions() # CreatePullReviewOptions | 

    try:
        # Create a review to an pull request
        api_response = api_instance.repo_create_pull_review(owner, repo, index, body)
        print("The response of RepositoryApi->repo_create_pull_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_pull_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 
 **body** | [**CreatePullReviewOptions**](CreatePullReviewOptions.md)|  | 

### Return type

[**PullReview**](PullReview.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReview |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_pull_review_requests**
> List[PullReview] repo_create_pull_review_requests(owner, repo, index, body)

create review requests for a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_review import PullReview
from gitea_api.models.pull_review_request_options import PullReviewRequestOptions
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request
    body = gitea_api.PullReviewRequestOptions() # PullReviewRequestOptions | 

    try:
        # create review requests for a pull request
        api_response = api_instance.repo_create_pull_review_requests(owner, repo, index, body)
        print("The response of RepositoryApi->repo_create_pull_review_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_pull_review_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 
 **body** | [**PullReviewRequestOptions**](PullReviewRequestOptions.md)|  | 

### Return type

[**List[PullReview]**](PullReview.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PullReviewList |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_release**
> Release repo_create_release(owner, repo, body=body)

Create a release

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_release_option import CreateReleaseOption
from gitea_api.models.release import Release
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.CreateReleaseOption() # CreateReleaseOption |  (optional)

    try:
        # Create a release
        api_response = api_instance.repo_create_release(owner, repo, body=body)
        print("The response of RepositoryApi->repo_create_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreateReleaseOption**](CreateReleaseOption.md)|  | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Release |  -  |
**404** | APINotFound is a not found empty response |  -  |
**409** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_release_attachment**
> Attachment repo_create_release_attachment(owner, repo, id, name=name, attachment=attachment)

Create a release attachment

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.attachment import Attachment
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the release
    name = 'name_example' # str | name of the attachment (optional)
    attachment = None # bytearray | attachment to upload (optional)

    try:
        # Create a release attachment
        api_response = api_instance.repo_create_release_attachment(owner, repo, id, name=name, attachment=attachment)
        print("The response of RepositoryApi->repo_create_release_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_release_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release | 
 **name** | **str**| name of the attachment | [optional] 
 **attachment** | **bytearray**| attachment to upload | [optional] 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attachment |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_runner_registration_token**
> repo_create_runner_registration_token(owner, repo)

Get a repository's actions runner registration token

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Get a repository's actions runner registration token
        api_instance.repo_create_runner_registration_token(owner, repo)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_runner_registration_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RegistrationToken is response related to registration token |  * token -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_status**
> CommitStatus repo_create_status(owner, repo, sha, body=body)

Create a commit status

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.commit_status import CommitStatus
from gitea_api.models.create_status_option import CreateStatusOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    sha = 'sha_example' # str | sha of the commit
    body = gitea_api.CreateStatusOption() # CreateStatusOption |  (optional)

    try:
        # Create a commit status
        api_response = api_instance.repo_create_status(owner, repo, sha, body=body)
        print("The response of RepositoryApi->repo_create_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| sha of the commit | 
 **body** | [**CreateStatusOption**](CreateStatusOption.md)|  | [optional] 

### Return type

[**CommitStatus**](CommitStatus.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CommitStatus |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_tag**
> Tag repo_create_tag(owner, repo, body=body)

Create a new git tag in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_tag_option import CreateTagOption
from gitea_api.models.tag import Tag
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.CreateTagOption() # CreateTagOption |  (optional)

    try:
        # Create a new git tag in a repository
        api_response = api_instance.repo_create_tag(owner, repo, body=body)
        print("The response of RepositoryApi->repo_create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreateTagOption**](CreateTagOption.md)|  | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag |  -  |
**404** | APINotFound is a not found empty response |  -  |
**405** | APIEmpty is an empty response |  -  |
**409** | APIConflict is a conflict empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_tag_protection**
> TagProtection repo_create_tag_protection(owner, repo, body=body)

Create a tag protections for a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_tag_protection_option import CreateTagProtectionOption
from gitea_api.models.tag_protection import TagProtection
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.CreateTagProtectionOption() # CreateTagProtectionOption |  (optional)

    try:
        # Create a tag protections for a repository
        api_response = api_instance.repo_create_tag_protection(owner, repo, body=body)
        print("The response of RepositoryApi->repo_create_tag_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_tag_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreateTagProtectionOption**](CreateTagProtectionOption.md)|  | [optional] 

### Return type

[**TagProtection**](TagProtection.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TagProtection |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_wiki_page**
> WikiPage repo_create_wiki_page(owner, repo, body=body)

Create a wiki page

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_wiki_page_options import CreateWikiPageOptions
from gitea_api.models.wiki_page import WikiPage
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.CreateWikiPageOptions() # CreateWikiPageOptions |  (optional)

    try:
        # Create a wiki page
        api_response = api_instance.repo_create_wiki_page(owner, repo, body=body)
        print("The response of RepositoryApi->repo_create_wiki_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_create_wiki_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**CreateWikiPageOptions**](CreateWikiPageOptions.md)|  | [optional] 

### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | WikiPage |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete**
> repo_delete(owner, repo)

Delete a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo to delete
    repo = 'repo_example' # str | name of the repo to delete

    try:
        # Delete a repository
        api_instance.repo_delete(owner, repo)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to delete | 
 **repo** | **str**| name of the repo to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_avatar**
> repo_delete_avatar(owner, repo)

Delete avatar

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Delete avatar
        api_instance.repo_delete_avatar(owner, repo)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_branch**
> repo_delete_branch(owner, repo, branch)

Delete a specific branch from a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    branch = 'branch_example' # str | branch to delete

    try:
        # Delete a specific branch from a repository
        api_instance.repo_delete_branch(owner, repo, branch)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **branch** | **str**| branch to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_branch_protection**
> repo_delete_branch_protection(owner, repo, name)

Delete a specific branch protection for the repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    name = 'name_example' # str | name of protected branch

    try:
        # Delete a specific branch protection for the repository
        api_instance.repo_delete_branch_protection(owner, repo, name)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **name** | **str**| name of protected branch | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_collaborator**
> repo_delete_collaborator(owner, repo, collaborator)

Delete a collaborator from a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    collaborator = 'collaborator_example' # str | username of the collaborator to delete

    try:
        # Delete a collaborator from a repository
        api_instance.repo_delete_collaborator(owner, repo, collaborator)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **collaborator** | **str**| username of the collaborator to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_file**
> FileDeleteResponse repo_delete_file(owner, repo, filepath, body)

Delete a file in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.delete_file_options import DeleteFileOptions
from gitea_api.models.file_delete_response import FileDeleteResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    filepath = 'filepath_example' # str | path of the file to delete
    body = gitea_api.DeleteFileOptions() # DeleteFileOptions | 

    try:
        # Delete a file in a repository
        api_response = api_instance.repo_delete_file(owner, repo, filepath, body)
        print("The response of RepositoryApi->repo_delete_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| path of the file to delete | 
 **body** | [**DeleteFileOptions**](DeleteFileOptions.md)|  | 

### Return type

[**FileDeleteResponse**](FileDeleteResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FileDeleteResponse |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_git_hook**
> repo_delete_git_hook(owner, repo, id)

Delete a Git hook in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 'id_example' # str | id of the hook to get

    try:
        # Delete a Git hook in a repository
        api_instance.repo_delete_git_hook(owner, repo, id)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_git_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **str**| id of the hook to get | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_hook**
> repo_delete_hook(owner, repo, id)

Delete a hook in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the hook to delete

    try:
        # Delete a hook in a repository
        api_instance.repo_delete_hook(owner, repo, id)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the hook to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_key**
> repo_delete_key(owner, repo, id)

Delete a key from a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the key to delete

    try:
        # Delete a key from a repository
        api_instance.repo_delete_key(owner, repo, id)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the key to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_pull_review**
> repo_delete_pull_review(owner, repo, index, id)

Delete a specific review from a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request
    id = 56 # int | id of the review

    try:
        # Delete a specific review from a pull request
        api_instance.repo_delete_pull_review(owner, repo, index, id)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_pull_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 
 **id** | **int**| id of the review | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_pull_review_requests**
> repo_delete_pull_review_requests(owner, repo, index, body)

cancel review requests for a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_review_request_options import PullReviewRequestOptions
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request
    body = gitea_api.PullReviewRequestOptions() # PullReviewRequestOptions | 

    try:
        # cancel review requests for a pull request
        api_instance.repo_delete_pull_review_requests(owner, repo, index, body)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_pull_review_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 
 **body** | [**PullReviewRequestOptions**](PullReviewRequestOptions.md)|  | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_push_mirror**
> repo_delete_push_mirror(owner, repo, name)

deletes a push mirror from a repository by remoteName

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    name = 'name_example' # str | remote name of the pushMirror

    try:
        # deletes a push mirror from a repository by remoteName
        api_instance.repo_delete_push_mirror(owner, repo, name)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_push_mirror: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **name** | **str**| remote name of the pushMirror | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_release**
> repo_delete_release(owner, repo, id)

Delete a release

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the release to delete

    try:
        # Delete a release
        api_instance.repo_delete_release(owner, repo, id)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_release_attachment**
> repo_delete_release_attachment(owner, repo, id, attachment_id)

Delete a release attachment

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the release
    attachment_id = 56 # int | id of the attachment to delete

    try:
        # Delete a release attachment
        api_instance.repo_delete_release_attachment(owner, repo, id, attachment_id)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_release_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release | 
 **attachment_id** | **int**| id of the attachment to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_release_by_tag**
> repo_delete_release_by_tag(owner, repo, tag)

Delete a release by tag name

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    tag = 'tag_example' # str | tag name of the release to delete

    try:
        # Delete a release by tag name
        api_instance.repo_delete_release_by_tag(owner, repo, tag)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_release_by_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **tag** | **str**| tag name of the release to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_tag**
> repo_delete_tag(owner, repo, tag)

Delete a repository's tag by name

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    tag = 'tag_example' # str | name of tag to delete

    try:
        # Delete a repository's tag by name
        api_instance.repo_delete_tag(owner, repo, tag)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **tag** | **str**| name of tag to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**405** | APIEmpty is an empty response |  -  |
**409** | APIConflict is a conflict empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_tag_protection**
> repo_delete_tag_protection(owner, repo, id)

Delete a specific tag protection for the repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of protected tag

    try:
        # Delete a specific tag protection for the repository
        api_instance.repo_delete_tag_protection(owner, repo, id)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_tag_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of protected tag | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_team**
> repo_delete_team(owner, repo, team)

Delete a team from a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    team = 'team_example' # str | team name

    try:
        # Delete a team from a repository
        api_instance.repo_delete_team(owner, repo, team)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **team** | **str**| team name | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**405** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_topic**
> repo_delete_topic(owner, repo, topic)

Delete a topic from a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    topic = 'topic_example' # str | name of the topic to delete

    try:
        # Delete a topic from a repository
        api_instance.repo_delete_topic(owner, repo, topic)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **topic** | **str**| name of the topic to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIInvalidTopicsError is error format response to invalid topics |  * invalidTopics -  <br>  * message -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_wiki_page**
> repo_delete_wiki_page(owner, repo, page_name)

Delete a wiki page

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page_name = 'page_name_example' # str | name of the page

    try:
        # Delete a wiki page
        api_instance.repo_delete_wiki_page(owner, repo, page_name)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_delete_wiki_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page_name** | **str**| name of the page | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_dismiss_pull_review**
> PullReview repo_dismiss_pull_review(owner, repo, index, id, body)

Dismiss a review for a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.dismiss_pull_review_options import DismissPullReviewOptions
from gitea_api.models.pull_review import PullReview
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request
    id = 56 # int | id of the review
    body = gitea_api.DismissPullReviewOptions() # DismissPullReviewOptions | 

    try:
        # Dismiss a review for a pull request
        api_response = api_instance.repo_dismiss_pull_review(owner, repo, index, id, body)
        print("The response of RepositoryApi->repo_dismiss_pull_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_dismiss_pull_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 
 **id** | **int**| id of the review | 
 **body** | [**DismissPullReviewOptions**](DismissPullReviewOptions.md)|  | 

### Return type

[**PullReview**](PullReview.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReview |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_download_commit_diff_or_patch**
> str repo_download_commit_diff_or_patch(owner, repo, sha, diff_type)

Get a commit's diff or patch

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    sha = 'sha_example' # str | SHA of the commit to get
    diff_type = 'diff_type_example' # str | whether the output is diff or patch

    try:
        # Get a commit's diff or patch
        api_response = api_instance.repo_download_commit_diff_or_patch(owner, repo, sha, diff_type)
        print("The response of RepositoryApi->repo_download_commit_diff_or_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_download_commit_diff_or_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| SHA of the commit to get | 
 **diff_type** | **str**| whether the output is diff or patch | 

### Return type

**str**

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIString is a string response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_download_pull_diff_or_patch**
> str repo_download_pull_diff_or_patch(owner, repo, index, diff_type, binary=binary)

Get a pull request diff or patch

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request to get
    diff_type = 'diff_type_example' # str | whether the output is diff or patch
    binary = True # bool | whether to include binary file changes. if true, the diff is applicable with `git apply` (optional)

    try:
        # Get a pull request diff or patch
        api_response = api_instance.repo_download_pull_diff_or_patch(owner, repo, index, diff_type, binary=binary)
        print("The response of RepositoryApi->repo_download_pull_diff_or_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_download_pull_diff_or_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request to get | 
 **diff_type** | **str**| whether the output is diff or patch | 
 **binary** | **bool**| whether to include binary file changes. if true, the diff is applicable with &#x60;git apply&#x60; | [optional] 

### Return type

**str**

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIString is a string response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit**
> Repository repo_edit(owner, repo, body=body)

Edit a repository's properties. Only fields that are set will be changed.

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.edit_repo_option import EditRepoOption
from gitea_api.models.repository import Repository
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo to edit
    repo = 'repo_example' # str | name of the repo to edit
    body = gitea_api.EditRepoOption() # EditRepoOption | Properties of a repo that you can edit (optional)

    try:
        # Edit a repository's properties. Only fields that are set will be changed.
        api_response = api_instance.repo_edit(owner, repo, body=body)
        print("The response of RepositoryApi->repo_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to edit | 
 **repo** | **str**| name of the repo to edit | 
 **body** | [**EditRepoOption**](EditRepoOption.md)| Properties of a repo that you can edit | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_branch_protection**
> BranchProtection repo_edit_branch_protection(owner, repo, name, body=body)

Edit a branch protections for a repository. Only fields that are set will be changed

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.branch_protection import BranchProtection
from gitea_api.models.edit_branch_protection_option import EditBranchProtectionOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    name = 'name_example' # str | name of protected branch
    body = gitea_api.EditBranchProtectionOption() # EditBranchProtectionOption |  (optional)

    try:
        # Edit a branch protections for a repository. Only fields that are set will be changed
        api_response = api_instance.repo_edit_branch_protection(owner, repo, name, body=body)
        print("The response of RepositoryApi->repo_edit_branch_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_edit_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **name** | **str**| name of protected branch | 
 **body** | [**EditBranchProtectionOption**](EditBranchProtectionOption.md)|  | [optional] 

### Return type

[**BranchProtection**](BranchProtection.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BranchProtection |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_git_hook**
> GitHook repo_edit_git_hook(owner, repo, id, body=body)

Edit a Git hook in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.edit_git_hook_option import EditGitHookOption
from gitea_api.models.git_hook import GitHook
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 'id_example' # str | id of the hook to get
    body = gitea_api.EditGitHookOption() # EditGitHookOption |  (optional)

    try:
        # Edit a Git hook in a repository
        api_response = api_instance.repo_edit_git_hook(owner, repo, id, body=body)
        print("The response of RepositoryApi->repo_edit_git_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_edit_git_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **str**| id of the hook to get | 
 **body** | [**EditGitHookOption**](EditGitHookOption.md)|  | [optional] 

### Return type

[**GitHook**](GitHook.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GitHook |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_hook**
> Hook repo_edit_hook(owner, repo, id, body=body)

Edit a hook in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.edit_hook_option import EditHookOption
from gitea_api.models.hook import Hook
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | index of the hook
    body = gitea_api.EditHookOption() # EditHookOption |  (optional)

    try:
        # Edit a hook in a repository
        api_response = api_instance.repo_edit_hook(owner, repo, id, body=body)
        print("The response of RepositoryApi->repo_edit_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_edit_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| index of the hook | 
 **body** | [**EditHookOption**](EditHookOption.md)|  | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hook |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_pull_request**
> PullRequest repo_edit_pull_request(owner, repo, index, body=body)

Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.edit_pull_request_option import EditPullRequestOption
from gitea_api.models.pull_request import PullRequest
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request to edit
    body = gitea_api.EditPullRequestOption() # EditPullRequestOption |  (optional)

    try:
        # Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.repo_edit_pull_request(owner, repo, index, body=body)
        print("The response of RepositoryApi->repo_edit_pull_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_edit_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request to edit | 
 **body** | [**EditPullRequestOption**](EditPullRequestOption.md)|  | [optional] 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PullRequest |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**409** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**412** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_release**
> Release repo_edit_release(owner, repo, id, body=body)

Update a release

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.edit_release_option import EditReleaseOption
from gitea_api.models.release import Release
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the release to edit
    body = gitea_api.EditReleaseOption() # EditReleaseOption |  (optional)

    try:
        # Update a release
        api_response = api_instance.repo_edit_release(owner, repo, id, body=body)
        print("The response of RepositoryApi->repo_edit_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_edit_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release to edit | 
 **body** | [**EditReleaseOption**](EditReleaseOption.md)|  | [optional] 

### Return type

[**Release**](Release.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_release_attachment**
> Attachment repo_edit_release_attachment(owner, repo, id, attachment_id, body=body)

Edit a release attachment

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.attachment import Attachment
from gitea_api.models.edit_attachment_options import EditAttachmentOptions
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the release
    attachment_id = 56 # int | id of the attachment to edit
    body = gitea_api.EditAttachmentOptions() # EditAttachmentOptions |  (optional)

    try:
        # Edit a release attachment
        api_response = api_instance.repo_edit_release_attachment(owner, repo, id, attachment_id, body=body)
        print("The response of RepositoryApi->repo_edit_release_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_edit_release_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release | 
 **attachment_id** | **int**| id of the attachment to edit | 
 **body** | [**EditAttachmentOptions**](EditAttachmentOptions.md)|  | [optional] 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attachment |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_tag_protection**
> TagProtection repo_edit_tag_protection(owner, repo, id, body=body)

Edit a tag protections for a repository. Only fields that are set will be changed

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.edit_tag_protection_option import EditTagProtectionOption
from gitea_api.models.tag_protection import TagProtection
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of protected tag
    body = gitea_api.EditTagProtectionOption() # EditTagProtectionOption |  (optional)

    try:
        # Edit a tag protections for a repository. Only fields that are set will be changed
        api_response = api_instance.repo_edit_tag_protection(owner, repo, id, body=body)
        print("The response of RepositoryApi->repo_edit_tag_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_edit_tag_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of protected tag | 
 **body** | [**EditTagProtectionOption**](EditTagProtectionOption.md)|  | [optional] 

### Return type

[**TagProtection**](TagProtection.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TagProtection |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_wiki_page**
> WikiPage repo_edit_wiki_page(owner, repo, page_name, body=body)

Edit a wiki page

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_wiki_page_options import CreateWikiPageOptions
from gitea_api.models.wiki_page import WikiPage
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page_name = 'page_name_example' # str | name of the page
    body = gitea_api.CreateWikiPageOptions() # CreateWikiPageOptions |  (optional)

    try:
        # Edit a wiki page
        api_response = api_instance.repo_edit_wiki_page(owner, repo, page_name, body=body)
        print("The response of RepositoryApi->repo_edit_wiki_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_edit_wiki_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page_name** | **str**| name of the page | 
 **body** | [**CreateWikiPageOptions**](CreateWikiPageOptions.md)|  | [optional] 

### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WikiPage |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get**
> Repository repo_get(owner, repo)

Get a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.repository import Repository
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Get a repository
        api_response = api_instance.repo_get(owner, repo)
        print("The response of RepositoryApi->repo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_all_commits**
> List[Commit] repo_get_all_commits(owner, repo, sha=sha, path=path, stat=stat, verification=verification, files=files, page=page, limit=limit, var_not=var_not)

Get a list of all commits from a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.commit import Commit
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    sha = 'sha_example' # str | SHA or branch to start listing commits from (usually 'master') (optional)
    path = 'path_example' # str | filepath of a file/dir (optional)
    stat = True # bool | include diff stats for every commit (disable for speedup, default 'true') (optional)
    verification = True # bool | include verification for every commit (disable for speedup, default 'true') (optional)
    files = True # bool | include a list of affected files for every commit (disable for speedup, default 'true') (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (ignored if used with 'path') (optional)
    var_not = 'var_not_example' # str | commits that match the given specifier will not be listed. (optional)

    try:
        # Get a list of all commits from a repository
        api_response = api_instance.repo_get_all_commits(owner, repo, sha=sha, path=path, stat=stat, verification=verification, files=files, page=page, limit=limit, var_not=var_not)
        print("The response of RepositoryApi->repo_get_all_commits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_all_commits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| SHA or branch to start listing commits from (usually &#39;master&#39;) | [optional] 
 **path** | **str**| filepath of a file/dir | [optional] 
 **stat** | **bool**| include diff stats for every commit (disable for speedup, default &#39;true&#39;) | [optional] 
 **verification** | **bool**| include verification for every commit (disable for speedup, default &#39;true&#39;) | [optional] 
 **files** | **bool**| include a list of affected files for every commit (disable for speedup, default &#39;true&#39;) | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results (ignored if used with &#39;path&#39;) | [optional] 
 **var_not** | **str**| commits that match the given specifier will not be listed. | [optional] 

### Return type

[**List[Commit]**](Commit.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommitList |  * X-HasMore - True if there is another page <br>  * X-PageCount - Total number of pages <br>  * X-PerPage - Commits per page <br>  * X-Total - Total commit count <br>  * X-Page - The current page <br>  |
**404** | APINotFound is a not found empty response |  -  |
**409** | EmptyRepository |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_archive**
> repo_get_archive(owner, repo, archive)

Get an archive of a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    archive = 'archive_example' # str | the git reference for download with attached archive format (e.g. master.zip)

    try:
        # Get an archive of a repository
        api_instance.repo_get_archive(owner, repo, archive)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **archive** | **str**| the git reference for download with attached archive format (e.g. master.zip) | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_assignees**
> List[User] repo_get_assignees(owner, repo)

Return all users that have write access and can be assigned to issues

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.user import User
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Return all users that have write access and can be assigned to issues
        api_response = api_instance.repo_get_assignees(owner, repo)
        print("The response of RepositoryApi->repo_get_assignees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_assignees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**List[User]**](User.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_branch**
> Branch repo_get_branch(owner, repo, branch)

Retrieve a specific branch from a repository, including its effective branch protection

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.branch import Branch
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    branch = 'branch_example' # str | branch to get

    try:
        # Retrieve a specific branch from a repository, including its effective branch protection
        api_response = api_instance.repo_get_branch(owner, repo, branch)
        print("The response of RepositoryApi->repo_get_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **branch** | **str**| branch to get | 

### Return type

[**Branch**](Branch.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Branch |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_branch_protection**
> BranchProtection repo_get_branch_protection(owner, repo, name)

Get a specific branch protection for the repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.branch_protection import BranchProtection
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    name = 'name_example' # str | name of protected branch

    try:
        # Get a specific branch protection for the repository
        api_response = api_instance.repo_get_branch_protection(owner, repo, name)
        print("The response of RepositoryApi->repo_get_branch_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **name** | **str**| name of protected branch | 

### Return type

[**BranchProtection**](BranchProtection.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BranchProtection |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_by_id**
> Repository repo_get_by_id(id)

Get a repository by id

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.repository import Repository
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    id = 56 # int | id of the repo to get

    try:
        # Get a repository by id
        api_response = api_instance.repo_get_by_id(id)
        print("The response of RepositoryApi->repo_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the repo to get | 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_combined_status_by_ref**
> CombinedStatus repo_get_combined_status_by_ref(owner, repo, ref, page=page, limit=limit)

Get a commit's combined status, by branch/tag/commit reference

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.combined_status import CombinedStatus
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    ref = 'ref_example' # str | name of branch/tag/commit
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Get a commit's combined status, by branch/tag/commit reference
        api_response = api_instance.repo_get_combined_status_by_ref(owner, repo, ref, page=page, limit=limit)
        print("The response of RepositoryApi->repo_get_combined_status_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_combined_status_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **ref** | **str**| name of branch/tag/commit | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**CombinedStatus**](CombinedStatus.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CombinedStatus |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_commit_pull_request**
> PullRequest repo_get_commit_pull_request(owner, repo, sha)

Get the merged pull request of the commit

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_request import PullRequest
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    sha = 'sha_example' # str | SHA of the commit to get

    try:
        # Get the merged pull request of the commit
        api_response = api_instance.repo_get_commit_pull_request(owner, repo, sha)
        print("The response of RepositoryApi->repo_get_commit_pull_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_commit_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| SHA of the commit to get | 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullRequest |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_contents**
> ContentsResponse repo_get_contents(owner, repo, filepath, ref=ref)

Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.contents_response import ContentsResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    filepath = 'filepath_example' # str | path of the dir, file, symlink or submodule in the repo
    ref = 'ref_example' # str | The name of the commit/branch/tag. Default to the repository’s default branch. (optional)

    try:
        # Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir
        api_response = api_instance.repo_get_contents(owner, repo, filepath, ref=ref)
        print("The response of RepositoryApi->repo_get_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_contents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| path of the dir, file, symlink or submodule in the repo | 
 **ref** | **str**| The name of the commit/branch/tag. Default to the repository’s default branch. | [optional] 

### Return type

[**ContentsResponse**](ContentsResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContentsResponse |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_contents_list**
> List[ContentsResponse] repo_get_contents_list(owner, repo, ref=ref)

Gets the metadata of all the entries of the root dir

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.contents_response import ContentsResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    ref = 'ref_example' # str | The name of the commit/branch/tag. Default to the repository’s default branch. (optional)

    try:
        # Gets the metadata of all the entries of the root dir
        api_response = api_instance.repo_get_contents_list(owner, repo, ref=ref)
        print("The response of RepositoryApi->repo_get_contents_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_contents_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **ref** | **str**| The name of the commit/branch/tag. Default to the repository’s default branch. | [optional] 

### Return type

[**List[ContentsResponse]**](ContentsResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContentsListResponse |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_editor_config**
> repo_get_editor_config(owner, repo, filepath, ref=ref)

Get the EditorConfig definitions of a file in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    filepath = 'filepath_example' # str | filepath of file to get
    ref = 'ref_example' # str | The name of the commit/branch/tag. Default to the repository’s default branch. (optional)

    try:
        # Get the EditorConfig definitions of a file in a repository
        api_instance.repo_get_editor_config(owner, repo, filepath, ref=ref)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_editor_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| filepath of file to get | 
 **ref** | **str**| The name of the commit/branch/tag. Default to the repository’s default branch. | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_file_contents**
> List[ContentsResponse] repo_get_file_contents(owner, repo, body, ref=ref)

Get the metadata and contents of requested files

See the POST method. This GET method supports to use JSON encoded request body in query parameter.

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.contents_response import ContentsResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = 'body_example' # str | The JSON encoded body (see the POST request): {\"files\": [\"filename1\", \"filename2\"]}
    ref = 'ref_example' # str | The name of the commit/branch/tag. Default to the repository’s default branch. (optional)

    try:
        # Get the metadata and contents of requested files
        api_response = api_instance.repo_get_file_contents(owner, repo, body, ref=ref)
        print("The response of RepositoryApi->repo_get_file_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_file_contents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | **str**| The JSON encoded body (see the POST request): {\&quot;files\&quot;: [\&quot;filename1\&quot;, \&quot;filename2\&quot;]} | 
 **ref** | **str**| The name of the commit/branch/tag. Default to the repository’s default branch. | [optional] 

### Return type

[**List[ContentsResponse]**](ContentsResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContentsListResponse |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_file_contents_post**
> List[ContentsResponse] repo_get_file_contents_post(owner, repo, body, ref=ref)

Get the metadata and contents of requested files

Uses automatic pagination based on default page size and max response size and returns the maximum allowed number of files. Files which could not be retrieved are null. Files which are too large are being returned with `encoding == null`, `content == null` and `size > 0`, they can be requested separately by using the `download_url`.

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.contents_response import ContentsResponse
from gitea_api.models.get_files_options import GetFilesOptions
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.GetFilesOptions() # GetFilesOptions | 
    ref = 'ref_example' # str | The name of the commit/branch/tag. Default to the repository’s default branch. (optional)

    try:
        # Get the metadata and contents of requested files
        api_response = api_instance.repo_get_file_contents_post(owner, repo, body, ref=ref)
        print("The response of RepositoryApi->repo_get_file_contents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_file_contents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**GetFilesOptions**](GetFilesOptions.md)|  | 
 **ref** | **str**| The name of the commit/branch/tag. Default to the repository’s default branch. | [optional] 

### Return type

[**List[ContentsResponse]**](ContentsResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContentsListResponse |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_git_hook**
> GitHook repo_get_git_hook(owner, repo, id)

Get a Git hook

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.git_hook import GitHook
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 'id_example' # str | id of the hook to get

    try:
        # Get a Git hook
        api_response = api_instance.repo_get_git_hook(owner, repo, id)
        print("The response of RepositoryApi->repo_get_git_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_git_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **str**| id of the hook to get | 

### Return type

[**GitHook**](GitHook.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GitHook |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_hook**
> Hook repo_get_hook(owner, repo, id)

Get a hook

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.hook import Hook
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the hook to get

    try:
        # Get a hook
        api_response = api_instance.repo_get_hook(owner, repo, id)
        print("The response of RepositoryApi->repo_get_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the hook to get | 

### Return type

[**Hook**](Hook.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hook |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_issue_config**
> IssueConfig repo_get_issue_config(owner, repo)

Returns the issue config for a repo

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.issue_config import IssueConfig
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Returns the issue config for a repo
        api_response = api_instance.repo_get_issue_config(owner, repo)
        print("The response of RepositoryApi->repo_get_issue_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_issue_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**IssueConfig**](IssueConfig.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RepoIssueConfig |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_issue_templates**
> List[IssueTemplate] repo_get_issue_templates(owner, repo)

Get available issue templates for a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.issue_template import IssueTemplate
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Get available issue templates for a repository
        api_response = api_instance.repo_get_issue_templates(owner, repo)
        print("The response of RepositoryApi->repo_get_issue_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_issue_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**List[IssueTemplate]**](IssueTemplate.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IssueTemplates |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_key**
> DeployKey repo_get_key(owner, repo, id)

Get a repository's key by id

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.deploy_key import DeployKey
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the key to get

    try:
        # Get a repository's key by id
        api_response = api_instance.repo_get_key(owner, repo, id)
        print("The response of RepositoryApi->repo_get_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the key to get | 

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeployKey |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_languages**
> Dict[str, int] repo_get_languages(owner, repo)

Get languages and number of bytes of code written

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Get languages and number of bytes of code written
        api_response = api_instance.repo_get_languages(owner, repo)
        print("The response of RepositoryApi->repo_get_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_languages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

**Dict[str, int]**

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LanguageStatistics |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_latest_release**
> Release repo_get_latest_release(owner, repo)

Gets the most recent non-prerelease, non-draft release of a repository, sorted by created_at

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.release import Release
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Gets the most recent non-prerelease, non-draft release of a repository, sorted by created_at
        api_response = api_instance.repo_get_latest_release(owner, repo)
        print("The response of RepositoryApi->repo_get_latest_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_latest_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**Release**](Release.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_licenses**
> List[str] repo_get_licenses(owner, repo)

Get repo licenses

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Get repo licenses
        api_response = api_instance.repo_get_licenses(owner, repo)
        print("The response of RepositoryApi->repo_get_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_licenses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

**List[str]**

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LicensesList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_note**
> Note repo_get_note(owner, repo, sha, verification=verification, files=files)

Get a note corresponding to a single commit from a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.note import Note
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    sha = 'sha_example' # str | a git ref or commit sha
    verification = True # bool | include verification for every commit (disable for speedup, default 'true') (optional)
    files = True # bool | include a list of affected files for every commit (disable for speedup, default 'true') (optional)

    try:
        # Get a note corresponding to a single commit from a repository
        api_response = api_instance.repo_get_note(owner, repo, sha, verification=verification, files=files)
        print("The response of RepositoryApi->repo_get_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| a git ref or commit sha | 
 **verification** | **bool**| include verification for every commit (disable for speedup, default &#39;true&#39;) | [optional] 
 **files** | **bool**| include a list of affected files for every commit (disable for speedup, default &#39;true&#39;) | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_pull_request**
> PullRequest repo_get_pull_request(owner, repo, index)

Get a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_request import PullRequest
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request to get

    try:
        # Get a pull request
        api_response = api_instance.repo_get_pull_request(owner, repo, index)
        print("The response of RepositoryApi->repo_get_pull_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request to get | 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullRequest |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_pull_request_by_base_head**
> PullRequest repo_get_pull_request_by_base_head(owner, repo, base, head)

Get a pull request by base and head

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_request import PullRequest
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    base = 'base_example' # str | base of the pull request to get
    head = 'head_example' # str | head of the pull request to get

    try:
        # Get a pull request by base and head
        api_response = api_instance.repo_get_pull_request_by_base_head(owner, repo, base, head)
        print("The response of RepositoryApi->repo_get_pull_request_by_base_head:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_pull_request_by_base_head: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **base** | **str**| base of the pull request to get | 
 **head** | **str**| head of the pull request to get | 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullRequest |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_pull_request_commits**
> List[Commit] repo_get_pull_request_commits(owner, repo, index, page=page, limit=limit, verification=verification, files=files)

Get commits for a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.commit import Commit
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request to get
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)
    verification = True # bool | include verification for every commit (disable for speedup, default 'true') (optional)
    files = True # bool | include a list of affected files for every commit (disable for speedup, default 'true') (optional)

    try:
        # Get commits for a pull request
        api_response = api_instance.repo_get_pull_request_commits(owner, repo, index, page=page, limit=limit, verification=verification, files=files)
        print("The response of RepositoryApi->repo_get_pull_request_commits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_pull_request_commits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request to get | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 
 **verification** | **bool**| include verification for every commit (disable for speedup, default &#39;true&#39;) | [optional] 
 **files** | **bool**| include a list of affected files for every commit (disable for speedup, default &#39;true&#39;) | [optional] 

### Return type

[**List[Commit]**](Commit.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommitList |  * X-HasMore - True if there is another page <br>  * X-PageCount - Total number of pages <br>  * X-PerPage - Commits per page <br>  * X-Total - Total commit count <br>  * X-Page - The current page <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_pull_request_files**
> List[ChangedFile] repo_get_pull_request_files(owner, repo, index, skip_to=skip_to, whitespace=whitespace, page=page, limit=limit)

Get changed files for a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.changed_file import ChangedFile
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request to get
    skip_to = 'skip_to_example' # str | skip to given file (optional)
    whitespace = 'whitespace_example' # str | whitespace behavior (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Get changed files for a pull request
        api_response = api_instance.repo_get_pull_request_files(owner, repo, index, skip_to=skip_to, whitespace=whitespace, page=page, limit=limit)
        print("The response of RepositoryApi->repo_get_pull_request_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_pull_request_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request to get | 
 **skip_to** | **str**| skip to given file | [optional] 
 **whitespace** | **str**| whitespace behavior | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[ChangedFile]**](ChangedFile.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChangedFileList |  * X-HasMore - True if there is another page <br>  * X-PageCount - Total number of pages <br>  * X-PerPage - Commits per page <br>  * X-Total - Total commit count <br>  * X-Page - The current page <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_pull_review**
> PullReview repo_get_pull_review(owner, repo, index, id)

Get a specific review for a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_review import PullReview
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request
    id = 56 # int | id of the review

    try:
        # Get a specific review for a pull request
        api_response = api_instance.repo_get_pull_review(owner, repo, index, id)
        print("The response of RepositoryApi->repo_get_pull_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_pull_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 
 **id** | **int**| id of the review | 

### Return type

[**PullReview**](PullReview.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReview |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_pull_review_comments**
> List[PullReviewComment] repo_get_pull_review_comments(owner, repo, index, id)

Get a specific review for a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_review_comment import PullReviewComment
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request
    id = 56 # int | id of the review

    try:
        # Get a specific review for a pull request
        api_response = api_instance.repo_get_pull_review_comments(owner, repo, index, id)
        print("The response of RepositoryApi->repo_get_pull_review_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_pull_review_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 
 **id** | **int**| id of the review | 

### Return type

[**List[PullReviewComment]**](PullReviewComment.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullCommentList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_push_mirror_by_remote_name**
> PushMirror repo_get_push_mirror_by_remote_name(owner, repo, name)

Get push mirror of the repository by remoteName

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.push_mirror import PushMirror
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    name = 'name_example' # str | remote name of push mirror

    try:
        # Get push mirror of the repository by remoteName
        api_response = api_instance.repo_get_push_mirror_by_remote_name(owner, repo, name)
        print("The response of RepositoryApi->repo_get_push_mirror_by_remote_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_push_mirror_by_remote_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **name** | **str**| remote name of push mirror | 

### Return type

[**PushMirror**](PushMirror.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PushMirror |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_raw_file**
> bytearray repo_get_raw_file(owner, repo, filepath, ref=ref)

Get a file from a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    filepath = 'filepath_example' # str | path of the file to get, it should be \"{ref}/{filepath}\". If there is no ref could be inferred, it will be treated as the default branch
    ref = 'ref_example' # str | The name of the commit/branch/tag. Default the repository’s default branch (optional)

    try:
        # Get a file from a repository
        api_response = api_instance.repo_get_raw_file(owner, repo, filepath, ref=ref)
        print("The response of RepositoryApi->repo_get_raw_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_raw_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| path of the file to get, it should be \&quot;{ref}/{filepath}\&quot;. If there is no ref could be inferred, it will be treated as the default branch | 
 **ref** | **str**| The name of the commit/branch/tag. Default the repository’s default branch | [optional] 

### Return type

**bytearray**

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns raw file content. |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_raw_file_or_lfs**
> bytearray repo_get_raw_file_or_lfs(owner, repo, filepath, ref=ref)

Get a file or it's LFS object from a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    filepath = 'filepath_example' # str | path of the file to get, it should be \"{ref}/{filepath}\". If there is no ref could be inferred, it will be treated as the default branch
    ref = 'ref_example' # str | The name of the commit/branch/tag. Default the repository’s default branch (optional)

    try:
        # Get a file or it's LFS object from a repository
        api_response = api_instance.repo_get_raw_file_or_lfs(owner, repo, filepath, ref=ref)
        print("The response of RepositoryApi->repo_get_raw_file_or_lfs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_raw_file_or_lfs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| path of the file to get, it should be \&quot;{ref}/{filepath}\&quot;. If there is no ref could be inferred, it will be treated as the default branch | 
 **ref** | **str**| The name of the commit/branch/tag. Default the repository’s default branch | [optional] 

### Return type

**bytearray**

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns raw file content. |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_release**
> Release repo_get_release(owner, repo, id)

Get a release

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.release import Release
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the release to get

    try:
        # Get a release
        api_response = api_instance.repo_get_release(owner, repo, id)
        print("The response of RepositoryApi->repo_get_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release to get | 

### Return type

[**Release**](Release.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_release_attachment**
> Attachment repo_get_release_attachment(owner, repo, id, attachment_id)

Get a release attachment

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.attachment import Attachment
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the release
    attachment_id = 56 # int | id of the attachment to get

    try:
        # Get a release attachment
        api_response = api_instance.repo_get_release_attachment(owner, repo, id, attachment_id)
        print("The response of RepositoryApi->repo_get_release_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_release_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release | 
 **attachment_id** | **int**| id of the attachment to get | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_release_by_tag**
> Release repo_get_release_by_tag(owner, repo, tag)

Get a release by tag name

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.release import Release
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    tag = 'tag_example' # str | tag name of the release to get

    try:
        # Get a release by tag name
        api_response = api_instance.repo_get_release_by_tag(owner, repo, tag)
        print("The response of RepositoryApi->repo_get_release_by_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_release_by_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **tag** | **str**| tag name of the release to get | 

### Return type

[**Release**](Release.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_repo_permissions**
> RepoCollaboratorPermission repo_get_repo_permissions(owner, repo, collaborator)

Get repository permissions for a user

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.repo_collaborator_permission import RepoCollaboratorPermission
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    collaborator = 'collaborator_example' # str | username of the collaborator

    try:
        # Get repository permissions for a user
        api_response = api_instance.repo_get_repo_permissions(owner, repo, collaborator)
        print("The response of RepositoryApi->repo_get_repo_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_repo_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **collaborator** | **str**| username of the collaborator | 

### Return type

[**RepoCollaboratorPermission**](RepoCollaboratorPermission.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RepoCollaboratorPermission |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_reviewers**
> List[User] repo_get_reviewers(owner, repo)

Return all users that can be requested to review in this repo

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.user import User
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Return all users that can be requested to review in this repo
        api_response = api_instance.repo_get_reviewers(owner, repo)
        print("The response of RepositoryApi->repo_get_reviewers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_reviewers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**List[User]**](User.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_runner_registration_token**
> repo_get_runner_registration_token(owner, repo)

Get a repository's actions runner registration token

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Get a repository's actions runner registration token
        api_instance.repo_get_runner_registration_token(owner, repo)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_runner_registration_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RegistrationToken is response related to registration token |  * token -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_single_commit**
> Commit repo_get_single_commit(owner, repo, sha, stat=stat, verification=verification, files=files)

Get a single commit from a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.commit import Commit
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    sha = 'sha_example' # str | a git ref or commit sha
    stat = True # bool | include diff stats for every commit (disable for speedup, default 'true') (optional)
    verification = True # bool | include verification for every commit (disable for speedup, default 'true') (optional)
    files = True # bool | include a list of affected files for every commit (disable for speedup, default 'true') (optional)

    try:
        # Get a single commit from a repository
        api_response = api_instance.repo_get_single_commit(owner, repo, sha, stat=stat, verification=verification, files=files)
        print("The response of RepositoryApi->repo_get_single_commit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_single_commit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| a git ref or commit sha | 
 **stat** | **bool**| include diff stats for every commit (disable for speedup, default &#39;true&#39;) | [optional] 
 **verification** | **bool**| include verification for every commit (disable for speedup, default &#39;true&#39;) | [optional] 
 **files** | **bool**| include a list of affected files for every commit (disable for speedup, default &#39;true&#39;) | [optional] 

### Return type

[**Commit**](Commit.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Commit |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_tag**
> Tag repo_get_tag(owner, repo, tag)

Get the tag of a repository by tag name

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.tag import Tag
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    tag = 'tag_example' # str | name of tag

    try:
        # Get the tag of a repository by tag name
        api_response = api_instance.repo_get_tag(owner, repo, tag)
        print("The response of RepositoryApi->repo_get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **tag** | **str**| name of tag | 

### Return type

[**Tag**](Tag.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_tag_protection**
> TagProtection repo_get_tag_protection(owner, repo, id)

Get a specific tag protection for the repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.tag_protection import TagProtection
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the tag protect to get

    try:
        # Get a specific tag protection for the repository
        api_response = api_instance.repo_get_tag_protection(owner, repo, id)
        print("The response of RepositoryApi->repo_get_tag_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_tag_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the tag protect to get | 

### Return type

[**TagProtection**](TagProtection.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TagProtection |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_wiki_page**
> WikiPage repo_get_wiki_page(owner, repo, page_name)

Get a wiki page

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.wiki_page import WikiPage
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page_name = 'page_name_example' # str | name of the page

    try:
        # Get a wiki page
        api_response = api_instance.repo_get_wiki_page(owner, repo, page_name)
        print("The response of RepositoryApi->repo_get_wiki_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_wiki_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page_name** | **str**| name of the page | 

### Return type

[**WikiPage**](WikiPage.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WikiPage |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_wiki_page_revisions**
> WikiCommitList repo_get_wiki_page_revisions(owner, repo, page_name, page=page)

Get revisions of a wiki page

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.wiki_commit_list import WikiCommitList
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page_name = 'page_name_example' # str | name of the page
    page = 56 # int | page number of results to return (1-based) (optional)

    try:
        # Get revisions of a wiki page
        api_response = api_instance.repo_get_wiki_page_revisions(owner, repo, page_name, page=page)
        print("The response of RepositoryApi->repo_get_wiki_page_revisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_wiki_page_revisions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page_name** | **str**| name of the page | 
 **page** | **int**| page number of results to return (1-based) | [optional] 

### Return type

[**WikiCommitList**](WikiCommitList.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WikiCommitList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_wiki_pages**
> List[WikiPageMetaData] repo_get_wiki_pages(owner, repo, page=page, limit=limit)

Get all wiki pages

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.wiki_page_meta_data import WikiPageMetaData
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Get all wiki pages
        api_response = api_instance.repo_get_wiki_pages(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->repo_get_wiki_pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_get_wiki_pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[WikiPageMetaData]**](WikiPageMetaData.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WikiPageList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_actions_secrets**
> List[Secret] repo_list_actions_secrets(owner, repo, page=page, limit=limit)

List an repo's actions secrets

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.secret import Secret
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repository
    repo = 'repo_example' # str | name of the repository
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List an repo's actions secrets
        api_response = api_instance.repo_list_actions_secrets(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_actions_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_actions_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repository | 
 **repo** | **str**| name of the repository | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Secret]**](Secret.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_activity_feeds**
> List[Activity] repo_list_activity_feeds(owner, repo, var_date=var_date, page=page, limit=limit)

List a repository's activity feeds

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.activity import Activity
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    var_date = '2013-10-20' # date | the date of the activities to be found (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a repository's activity feeds
        api_response = api_instance.repo_list_activity_feeds(owner, repo, var_date=var_date, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_activity_feeds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_activity_feeds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **var_date** | **date**| the date of the activities to be found | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Activity]**](Activity.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActivityFeedsList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_all_git_refs**
> List[Reference] repo_list_all_git_refs(owner, repo)

Get specified ref or filtered repository's refs

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.reference import Reference
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Get specified ref or filtered repository's refs
        api_response = api_instance.repo_list_all_git_refs(owner, repo)
        print("The response of RepositoryApi->repo_list_all_git_refs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_all_git_refs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**List[Reference]**](Reference.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReferenceList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_branch_protection**
> List[BranchProtection] repo_list_branch_protection(owner, repo)

List branch protections for a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.branch_protection import BranchProtection
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # List branch protections for a repository
        api_response = api_instance.repo_list_branch_protection(owner, repo)
        print("The response of RepositoryApi->repo_list_branch_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**List[BranchProtection]**](BranchProtection.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BranchProtectionList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_branches**
> List[Branch] repo_list_branches(owner, repo, page=page, limit=limit)

List a repository's branches

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.branch import Branch
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a repository's branches
        api_response = api_instance.repo_list_branches(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_branches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Branch]**](Branch.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BranchList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_collaborators**
> List[User] repo_list_collaborators(owner, repo, page=page, limit=limit)

List a repository's collaborators

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.user import User
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a repository's collaborators
        api_response = api_instance.repo_list_collaborators(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_collaborators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_collaborators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_git_hooks**
> List[GitHook] repo_list_git_hooks(owner, repo)

List the Git hooks in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.git_hook import GitHook
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # List the Git hooks in a repository
        api_response = api_instance.repo_list_git_hooks(owner, repo)
        print("The response of RepositoryApi->repo_list_git_hooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_git_hooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**List[GitHook]**](GitHook.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GitHookList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_git_refs**
> List[Reference] repo_list_git_refs(owner, repo, ref)

Get specified ref or filtered repository's refs

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.reference import Reference
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    ref = 'ref_example' # str | part or full name of the ref

    try:
        # Get specified ref or filtered repository's refs
        api_response = api_instance.repo_list_git_refs(owner, repo, ref)
        print("The response of RepositoryApi->repo_list_git_refs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_git_refs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **ref** | **str**| part or full name of the ref | 

### Return type

[**List[Reference]**](Reference.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReferenceList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_hooks**
> List[Hook] repo_list_hooks(owner, repo, page=page, limit=limit)

List the hooks in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.hook import Hook
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List the hooks in a repository
        api_response = api_instance.repo_list_hooks(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_hooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_hooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Hook]**](Hook.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HookList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_keys**
> List[DeployKey] repo_list_keys(owner, repo, key_id=key_id, fingerprint=fingerprint, page=page, limit=limit)

List a repository's keys

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.deploy_key import DeployKey
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    key_id = 56 # int | the key_id to search for (optional)
    fingerprint = 'fingerprint_example' # str | fingerprint of the key (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a repository's keys
        api_response = api_instance.repo_list_keys(owner, repo, key_id=key_id, fingerprint=fingerprint, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **key_id** | **int**| the key_id to search for | [optional] 
 **fingerprint** | **str**| fingerprint of the key | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[DeployKey]**](DeployKey.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeployKeyList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_pinned_issues**
> List[Issue] repo_list_pinned_issues(owner, repo)

List a repo's pinned issues

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.issue import Issue
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # List a repo's pinned issues
        api_response = api_instance.repo_list_pinned_issues(owner, repo)
        print("The response of RepositoryApi->repo_list_pinned_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_pinned_issues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**List[Issue]**](Issue.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IssueList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_pinned_pull_requests**
> List[PullRequest] repo_list_pinned_pull_requests(owner, repo)

List a repo's pinned pull requests

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_request import PullRequest
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # List a repo's pinned pull requests
        api_response = api_instance.repo_list_pinned_pull_requests(owner, repo)
        print("The response of RepositoryApi->repo_list_pinned_pull_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_pinned_pull_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**List[PullRequest]**](PullRequest.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullRequestList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_pull_requests**
> List[PullRequest] repo_list_pull_requests(owner, repo, base_branch=base_branch, state=state, sort=sort, milestone=milestone, labels=labels, poster=poster, page=page, limit=limit)

List a repo's pull requests

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_request import PullRequest
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | Owner of the repo
    repo = 'repo_example' # str | Name of the repo
    base_branch = 'base_branch_example' # str | Filter by target base branch of the pull request (optional)
    state = open # str | State of pull request (optional) (default to open)
    sort = 'sort_example' # str | Type of sort (optional)
    milestone = 56 # int | ID of the milestone (optional)
    labels = [56] # List[int] | Label IDs (optional)
    poster = 'poster_example' # str | Filter by pull request author (optional)
    page = 1 # int | Page number of results to return (1-based) (optional) (default to 1)
    limit = 56 # int | Page size of results (optional)

    try:
        # List a repo's pull requests
        api_response = api_instance.repo_list_pull_requests(owner, repo, base_branch=base_branch, state=state, sort=sort, milestone=milestone, labels=labels, poster=poster, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_pull_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_pull_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| Owner of the repo | 
 **repo** | **str**| Name of the repo | 
 **base_branch** | **str**| Filter by target base branch of the pull request | [optional] 
 **state** | **str**| State of pull request | [optional] [default to open]
 **sort** | **str**| Type of sort | [optional] 
 **milestone** | **int**| ID of the milestone | [optional] 
 **labels** | [**List[int]**](int.md)| Label IDs | [optional] 
 **poster** | **str**| Filter by pull request author | [optional] 
 **page** | **int**| Page number of results to return (1-based) | [optional] [default to 1]
 **limit** | **int**| Page size of results | [optional] 

### Return type

[**List[PullRequest]**](PullRequest.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullRequestList |  -  |
**404** | APINotFound is a not found empty response |  -  |
**500** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_pull_reviews**
> List[PullReview] repo_list_pull_reviews(owner, repo, index, page=page, limit=limit)

List all reviews for a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_review import PullReview
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List all reviews for a pull request
        api_response = api_instance.repo_list_pull_reviews(owner, repo, index, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_pull_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_pull_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[PullReview]**](PullReview.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReviewList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_push_mirrors**
> List[PushMirror] repo_list_push_mirrors(owner, repo, page=page, limit=limit)

Get all push mirrors of the repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.push_mirror import PushMirror
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Get all push mirrors of the repository
        api_response = api_instance.repo_list_push_mirrors(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_push_mirrors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_push_mirrors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[PushMirror]**](PushMirror.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PushMirrorList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_release_attachments**
> List[Attachment] repo_list_release_attachments(owner, repo, id)

List release's attachments

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.attachment import Attachment
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the release

    try:
        # List release's attachments
        api_response = api_instance.repo_list_release_attachments(owner, repo, id)
        print("The response of RepositoryApi->repo_list_release_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_release_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the release | 

### Return type

[**List[Attachment]**](Attachment.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AttachmentList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_releases**
> List[Release] repo_list_releases(owner, repo, draft=draft, pre_release=pre_release, page=page, limit=limit)

List a repo's releases

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.release import Release
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    draft = True # bool | filter (exclude / include) drafts, if you dont have repo write access none will show (optional)
    pre_release = True # bool | filter (exclude / include) pre-releases (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a repo's releases
        api_response = api_instance.repo_list_releases(owner, repo, draft=draft, pre_release=pre_release, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_releases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_releases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **draft** | **bool**| filter (exclude / include) drafts, if you dont have repo write access none will show | [optional] 
 **pre_release** | **bool**| filter (exclude / include) pre-releases | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Release]**](Release.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReleaseList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_stargazers**
> List[User] repo_list_stargazers(owner, repo, page=page, limit=limit)

List a repo's stargazers

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.user import User
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a repo's stargazers
        api_response = api_instance.repo_list_stargazers(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_stargazers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_stargazers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_statuses**
> List[CommitStatus] repo_list_statuses(owner, repo, sha, sort=sort, state=state, page=page, limit=limit)

Get a commit's statuses

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.commit_status import CommitStatus
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    sha = 'sha_example' # str | sha of the commit
    sort = 'sort_example' # str | type of sort (optional)
    state = 'state_example' # str | type of state (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Get a commit's statuses
        api_response = api_instance.repo_list_statuses(owner, repo, sha, sort=sort, state=state, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **sha** | **str**| sha of the commit | 
 **sort** | **str**| type of sort | [optional] 
 **state** | **str**| type of state | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[CommitStatus]**](CommitStatus.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommitStatusList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_statuses_by_ref**
> List[CommitStatus] repo_list_statuses_by_ref(owner, repo, ref, sort=sort, state=state, page=page, limit=limit)

Get a commit's statuses, by branch/tag/commit reference

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.commit_status import CommitStatus
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    ref = 'ref_example' # str | name of branch/tag/commit
    sort = 'sort_example' # str | type of sort (optional)
    state = 'state_example' # str | type of state (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Get a commit's statuses, by branch/tag/commit reference
        api_response = api_instance.repo_list_statuses_by_ref(owner, repo, ref, sort=sort, state=state, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_statuses_by_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_statuses_by_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **ref** | **str**| name of branch/tag/commit | 
 **sort** | **str**| type of sort | [optional] 
 **state** | **str**| type of state | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[CommitStatus]**](CommitStatus.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommitStatusList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_subscribers**
> List[User] repo_list_subscribers(owner, repo, page=page, limit=limit)

List a repo's watchers

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.user import User
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a repo's watchers
        api_response = api_instance.repo_list_subscribers(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_subscribers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_subscribers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_tag_protection**
> List[TagProtection] repo_list_tag_protection(owner, repo)

List tag protections for a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.tag_protection import TagProtection
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # List tag protections for a repository
        api_response = api_instance.repo_list_tag_protection(owner, repo)
        print("The response of RepositoryApi->repo_list_tag_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_tag_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**List[TagProtection]**](TagProtection.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TagProtectionList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_tags**
> List[Tag] repo_list_tags(owner, repo, page=page, limit=limit)

List a repository's tags

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.tag import Tag
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results, default maximum page size is 50 (optional)

    try:
        # List a repository's tags
        api_response = api_instance.repo_list_tags(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results, default maximum page size is 50 | [optional] 

### Return type

[**List[Tag]**](Tag.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TagList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_teams**
> List[Team] repo_list_teams(owner, repo)

List a repository's teams

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.team import Team
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # List a repository's teams
        api_response = api_instance.repo_list_teams(owner, repo)
        print("The response of RepositoryApi->repo_list_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**List[Team]**](Team.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TeamList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_topics**
> TopicName repo_list_topics(owner, repo, page=page, limit=limit)

Get list of topics that a repository has

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.topic_name import TopicName
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Get list of topics that a repository has
        api_response = api_instance.repo_list_topics(owner, repo, page=page, limit=limit)
        print("The response of RepositoryApi->repo_list_topics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_list_topics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**TopicName**](TopicName.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TopicNames |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_merge_pull_request**
> repo_merge_pull_request(owner, repo, index, body=body)

Merge a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.merge_pull_request_option import MergePullRequestOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request to merge
    body = gitea_api.MergePullRequestOption() # MergePullRequestOption |  (optional)

    try:
        # Merge a pull request
        api_instance.repo_merge_pull_request(owner, repo, index, body=body)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_merge_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request to merge | 
 **body** | [**MergePullRequestOption**](MergePullRequestOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**405** | APIEmpty is an empty response |  -  |
**409** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_merge_upstream**
> MergeUpstreamResponse repo_merge_upstream(owner, repo, body=body)

Merge a branch from upstream

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.merge_upstream_request import MergeUpstreamRequest
from gitea_api.models.merge_upstream_response import MergeUpstreamResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.MergeUpstreamRequest() # MergeUpstreamRequest |  (optional)

    try:
        # Merge a branch from upstream
        api_response = api_instance.repo_merge_upstream(owner, repo, body=body)
        print("The response of RepositoryApi->repo_merge_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_merge_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**MergeUpstreamRequest**](MergeUpstreamRequest.md)|  | [optional] 

### Return type

[**MergeUpstreamResponse**](MergeUpstreamResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_migrate**
> Repository repo_migrate(body=body)

Migrate a remote git repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.migrate_repo_options import MigrateRepoOptions
from gitea_api.models.repository import Repository
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    body = gitea_api.MigrateRepoOptions() # MigrateRepoOptions |  (optional)

    try:
        # Migrate a remote git repository
        api_response = api_instance.repo_migrate(body=body)
        print("The response of RepositoryApi->repo_migrate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_migrate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrateRepoOptions**](MigrateRepoOptions.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**409** | The repository with the same name already exists. |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_mirror_sync**
> repo_mirror_sync(owner, repo)

Sync a mirrored repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo to sync
    repo = 'repo_example' # str | name of the repo to sync

    try:
        # Sync a mirrored repository
        api_instance.repo_mirror_sync(owner, repo)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_mirror_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to sync | 
 **repo** | **str**| name of the repo to sync | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_new_pin_allowed**
> NewIssuePinsAllowed repo_new_pin_allowed(owner, repo)

Returns if new Issue Pins are allowed

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.new_issue_pins_allowed import NewIssuePinsAllowed
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Returns if new Issue Pins are allowed
        api_response = api_instance.repo_new_pin_allowed(owner, repo)
        print("The response of RepositoryApi->repo_new_pin_allowed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_new_pin_allowed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**NewIssuePinsAllowed**](NewIssuePinsAllowed.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RepoNewIssuePinsAllowed |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_pull_request_is_merged**
> repo_pull_request_is_merged(owner, repo, index)

Check if a pull request has been merged

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request

    try:
        # Check if a pull request has been merged
        api_instance.repo_pull_request_is_merged(owner, repo, index)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_pull_request_is_merged: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | pull request has been merged |  -  |
**404** | pull request has not been merged |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_push_mirror_sync**
> repo_push_mirror_sync(owner, repo)

Sync all push mirrored repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo to sync
    repo = 'repo_example' # str | name of the repo to sync

    try:
        # Sync all push mirrored repository
        api_instance.repo_push_mirror_sync(owner, repo)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_push_mirror_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to sync | 
 **repo** | **str**| name of the repo to sync | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIEmpty is an empty response |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_search**
> SearchResults repo_search(q=q, topic=topic, include_desc=include_desc, uid=uid, priority_owner_id=priority_owner_id, team_id=team_id, starred_by=starred_by, private=private, is_private=is_private, template=template, archived=archived, mode=mode, exclusive=exclusive, sort=sort, order=order, page=page, limit=limit)

Search for repositories

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.search_results import SearchResults
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    q = 'q_example' # str | keyword (optional)
    topic = True # bool | Limit search to repositories with keyword as topic (optional)
    include_desc = True # bool | include search of keyword within repository description (optional)
    uid = 56 # int | search only for repos that the user with the given id owns or contributes to (optional)
    priority_owner_id = 56 # int | repo owner to prioritize in the results (optional)
    team_id = 56 # int | search only for repos that belong to the given team id (optional)
    starred_by = 56 # int | search only for repos that the user with the given id has starred (optional)
    private = True # bool | include private repositories this user has access to (defaults to true) (optional)
    is_private = True # bool | show only pubic, private or all repositories (defaults to all) (optional)
    template = True # bool | include template repositories this user has access to (defaults to true) (optional)
    archived = True # bool | show only archived, non-archived or all repositories (defaults to all) (optional)
    mode = 'mode_example' # str | type of repository to search for. Supported values are \"fork\", \"source\", \"mirror\" and \"collaborative\" (optional)
    exclusive = True # bool | if `uid` is given, search only for repos that the user owns (optional)
    sort = 'sort_example' # str | sort repos by attribute. Supported values are \"alpha\", \"created\", \"updated\", \"size\", \"git_size\", \"lfs_size\", \"stars\", \"forks\" and \"id\". Default is \"alpha\" (optional)
    order = 'order_example' # str | sort order, either \"asc\" (ascending) or \"desc\" (descending). Default is \"asc\", ignored if \"sort\" is not specified. (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Search for repositories
        api_response = api_instance.repo_search(q=q, topic=topic, include_desc=include_desc, uid=uid, priority_owner_id=priority_owner_id, team_id=team_id, starred_by=starred_by, private=private, is_private=is_private, template=template, archived=archived, mode=mode, exclusive=exclusive, sort=sort, order=order, page=page, limit=limit)
        print("The response of RepositoryApi->repo_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| keyword | [optional] 
 **topic** | **bool**| Limit search to repositories with keyword as topic | [optional] 
 **include_desc** | **bool**| include search of keyword within repository description | [optional] 
 **uid** | **int**| search only for repos that the user with the given id owns or contributes to | [optional] 
 **priority_owner_id** | **int**| repo owner to prioritize in the results | [optional] 
 **team_id** | **int**| search only for repos that belong to the given team id | [optional] 
 **starred_by** | **int**| search only for repos that the user with the given id has starred | [optional] 
 **private** | **bool**| include private repositories this user has access to (defaults to true) | [optional] 
 **is_private** | **bool**| show only pubic, private or all repositories (defaults to all) | [optional] 
 **template** | **bool**| include template repositories this user has access to (defaults to true) | [optional] 
 **archived** | **bool**| show only archived, non-archived or all repositories (defaults to all) | [optional] 
 **mode** | **str**| type of repository to search for. Supported values are \&quot;fork\&quot;, \&quot;source\&quot;, \&quot;mirror\&quot; and \&quot;collaborative\&quot; | [optional] 
 **exclusive** | **bool**| if &#x60;uid&#x60; is given, search only for repos that the user owns | [optional] 
 **sort** | **str**| sort repos by attribute. Supported values are \&quot;alpha\&quot;, \&quot;created\&quot;, \&quot;updated\&quot;, \&quot;size\&quot;, \&quot;git_size\&quot;, \&quot;lfs_size\&quot;, \&quot;stars\&quot;, \&quot;forks\&quot; and \&quot;id\&quot;. Default is \&quot;alpha\&quot; | [optional] 
 **order** | **str**| sort order, either \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default is \&quot;asc\&quot;, ignored if \&quot;sort\&quot; is not specified. | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SearchResults |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_signing_key**
> str repo_signing_key(owner, repo)

Get signing-key.gpg for given repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Get signing-key.gpg for given repository
        api_response = api_instance.repo_signing_key(owner, repo)
        print("The response of RepositoryApi->repo_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

**str**

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GPG armored public key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_submit_pull_review**
> PullReview repo_submit_pull_review(owner, repo, index, id, body)

Submit a pending review to an pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_review import PullReview
from gitea_api.models.submit_pull_review_options import SubmitPullReviewOptions
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request
    id = 56 # int | id of the review
    body = gitea_api.SubmitPullReviewOptions() # SubmitPullReviewOptions | 

    try:
        # Submit a pending review to an pull request
        api_response = api_instance.repo_submit_pull_review(owner, repo, index, id, body)
        print("The response of RepositoryApi->repo_submit_pull_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_submit_pull_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 
 **id** | **int**| id of the review | 
 **body** | [**SubmitPullReviewOptions**](SubmitPullReviewOptions.md)|  | 

### Return type

[**PullReview**](PullReview.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReview |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_test_hook**
> repo_test_hook(owner, repo, id, ref=ref)

Test a push webhook

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    id = 56 # int | id of the hook to test
    ref = 'ref_example' # str | The name of the commit/branch/tag, indicates which commit will be loaded to the webhook payload. (optional)

    try:
        # Test a push webhook
        api_instance.repo_test_hook(owner, repo, id, ref=ref)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_test_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **id** | **int**| id of the hook to test | 
 **ref** | **str**| The name of the commit/branch/tag, indicates which commit will be loaded to the webhook payload. | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_tracked_times**
> List[TrackedTime] repo_tracked_times(owner, repo, user=user, since=since, before=before, page=page, limit=limit)

List a repo's tracked times

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.tracked_time import TrackedTime
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    user = 'user_example' # str | optional filter by user (available for issue managers) (optional)
    since = '2013-10-20T19:20:30+01:00' # datetime | Only show times updated after the given time. This is a timestamp in RFC 3339 format (optional)
    before = '2013-10-20T19:20:30+01:00' # datetime | Only show times updated before the given time. This is a timestamp in RFC 3339 format (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a repo's tracked times
        api_response = api_instance.repo_tracked_times(owner, repo, user=user, since=since, before=before, page=page, limit=limit)
        print("The response of RepositoryApi->repo_tracked_times:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_tracked_times: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **user** | **str**| optional filter by user (available for issue managers) | [optional] 
 **since** | **datetime**| Only show times updated after the given time. This is a timestamp in RFC 3339 format | [optional] 
 **before** | **datetime**| Only show times updated before the given time. This is a timestamp in RFC 3339 format | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[TrackedTime]**](TrackedTime.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TrackedTimeList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_transfer**
> Repository repo_transfer(owner, repo, body)

Transfer a repo ownership

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.repository import Repository
from gitea_api.models.transfer_repo_option import TransferRepoOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo to transfer
    repo = 'repo_example' # str | name of the repo to transfer
    body = gitea_api.TransferRepoOption() # TransferRepoOption | Transfer Options

    try:
        # Transfer a repo ownership
        api_response = api_instance.repo_transfer(owner, repo, body)
        print("The response of RepositoryApi->repo_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to transfer | 
 **repo** | **str**| name of the repo to transfer | 
 **body** | [**TransferRepoOption**](TransferRepoOption.md)| Transfer Options | 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_un_dismiss_pull_review**
> PullReview repo_un_dismiss_pull_review(owner, repo, index, id)

Cancel to dismiss a review for a pull request

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.pull_review import PullReview
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request
    id = 56 # int | id of the review

    try:
        # Cancel to dismiss a review for a pull request
        api_response = api_instance.repo_un_dismiss_pull_review(owner, repo, index, id)
        print("The response of RepositoryApi->repo_un_dismiss_pull_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_un_dismiss_pull_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request | 
 **id** | **int**| id of the review | 

### Return type

[**PullReview**](PullReview.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReview |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_update_avatar**
> repo_update_avatar(owner, repo, body=body)

Update avatar

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.update_repo_avatar_option import UpdateRepoAvatarOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.UpdateRepoAvatarOption() # UpdateRepoAvatarOption |  (optional)

    try:
        # Update avatar
        api_instance.repo_update_avatar(owner, repo, body=body)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_update_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**UpdateRepoAvatarOption**](UpdateRepoAvatarOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_update_branch**
> repo_update_branch(owner, repo, branch, body=body)

Update a branch

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.update_branch_repo_option import UpdateBranchRepoOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    branch = 'branch_example' # str | name of the branch
    body = gitea_api.UpdateBranchRepoOption() # UpdateBranchRepoOption |  (optional)

    try:
        # Update a branch
        api_instance.repo_update_branch(owner, repo, branch, body=body)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_update_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **branch** | **str**| name of the branch | 
 **body** | [**UpdateBranchRepoOption**](UpdateBranchRepoOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_update_branch_protection_priories**
> repo_update_branch_protection_priories(owner, repo, body=body)

Update the priorities of branch protections for a repository.

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.update_branch_protection_priories import UpdateBranchProtectionPriories
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.UpdateBranchProtectionPriories() # UpdateBranchProtectionPriories |  (optional)

    try:
        # Update the priorities of branch protections for a repository.
        api_instance.repo_update_branch_protection_priories(owner, repo, body=body)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_update_branch_protection_priories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**UpdateBranchProtectionPriories**](UpdateBranchProtectionPriories.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_update_file**
> FileResponse repo_update_file(owner, repo, filepath, body)

Update a file in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.file_response import FileResponse
from gitea_api.models.update_file_options import UpdateFileOptions
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    filepath = 'filepath_example' # str | path of the file to update
    body = gitea_api.UpdateFileOptions() # UpdateFileOptions | 

    try:
        # Update a file in a repository
        api_response = api_instance.repo_update_file(owner, repo, filepath, body)
        print("The response of RepositoryApi->repo_update_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_update_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **filepath** | **str**| path of the file to update | 
 **body** | [**UpdateFileOptions**](UpdateFileOptions.md)|  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FileResponse |  -  |
**403** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**423** | APIRepoArchivedError is an error that is raised when an archived repo should be modified |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_update_pull_request**
> repo_update_pull_request(owner, repo, index, style=style)

Merge PR's baseBranch into headBranch

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    index = 56 # int | index of the pull request to get
    style = 'style_example' # str | how to update pull request (optional)

    try:
        # Merge PR's baseBranch into headBranch
        api_instance.repo_update_pull_request(owner, repo, index, style=style)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_update_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **index** | **int**| index of the pull request to get | 
 **style** | **str**| how to update pull request | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**409** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_update_topics**
> repo_update_topics(owner, repo, body=body)

Replace list of topics for a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.repo_topic_options import RepoTopicOptions
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    body = gitea_api.RepoTopicOptions() # RepoTopicOptions |  (optional)

    try:
        # Replace list of topics for a repository
        api_instance.repo_update_topics(owner, repo, body=body)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_update_topics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **body** | [**RepoTopicOptions**](RepoTopicOptions.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIInvalidTopicsError is error format response to invalid topics |  * invalidTopics -  <br>  * message -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_validate_issue_config**
> IssueConfigValidation repo_validate_issue_config(owner, repo)

Returns the validation information for a issue config

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.issue_config_validation import IssueConfigValidation
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Returns the validation information for a issue config
        api_response = api_instance.repo_validate_issue_config(owner, repo)
        print("The response of RepositoryApi->repo_validate_issue_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->repo_validate_issue_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**IssueConfigValidation**](IssueConfigValidation.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RepoIssueConfigValidation |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topic_search**
> List[TopicResponse] topic_search(q, page=page, limit=limit)

search topics via keyword

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.topic_response import TopicResponse
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    q = 'q_example' # str | keywords to search
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # search topics via keyword
        api_response = api_instance.topic_search(q, page=page, limit=limit)
        print("The response of RepositoryApi->topic_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->topic_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| keywords to search | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[TopicResponse]**](TopicResponse.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TopicListResponse |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repo_secret**
> update_repo_secret(owner, repo, secretname, body=body)

Create or Update a secret value in a repository

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.create_or_update_secret_option import CreateOrUpdateSecretOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repository
    repo = 'repo_example' # str | name of the repository
    secretname = 'secretname_example' # str | name of the secret
    body = gitea_api.CreateOrUpdateSecretOption() # CreateOrUpdateSecretOption |  (optional)

    try:
        # Create or Update a secret value in a repository
        api_instance.update_repo_secret(owner, repo, secretname, body=body)
    except Exception as e:
        print("Exception when calling RepositoryApi->update_repo_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repository | 
 **repo** | **str**| name of the repository | 
 **secretname** | **str**| name of the secret | 
 **body** | [**CreateOrUpdateSecretOption**](CreateOrUpdateSecretOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | response when creating a secret |  -  |
**204** | response when updating a secret |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repo_variable**
> update_repo_variable(owner, repo, variablename, body=body)

Update a repo-level variable

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.update_variable_option import UpdateVariableOption
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | name of the owner
    repo = 'repo_example' # str | name of the repository
    variablename = 'variablename_example' # str | name of the variable
    body = gitea_api.UpdateVariableOption() # UpdateVariableOption |  (optional)

    try:
        # Update a repo-level variable
        api_instance.update_repo_variable(owner, repo, variablename, body=body)
    except Exception as e:
        print("Exception when calling RepositoryApi->update_repo_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repository | 
 **variablename** | **str**| name of the variable | 
 **body** | [**UpdateVariableOption**](UpdateVariableOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | response when updating a repo-level variable |  -  |
**204** | response when updating a repo-level variable |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_current_check_subscription**
> WatchInfo user_current_check_subscription(owner, repo)

Check if the current user is watching a repo

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.watch_info import WatchInfo
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Check if the current user is watching a repo
        api_response = api_instance.user_current_check_subscription(owner, repo)
        print("The response of RepositoryApi->user_current_check_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->user_current_check_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**WatchInfo**](WatchInfo.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WatchInfo |  -  |
**404** | User is not watching this repo or repo do not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_current_delete_subscription**
> user_current_delete_subscription(owner, repo)

Unwatch a repo

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Unwatch a repo
        api_instance.user_current_delete_subscription(owner, repo)
    except Exception as e:
        print("Exception when calling RepositoryApi->user_current_delete_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_current_put_subscription**
> WatchInfo user_current_put_subscription(owner, repo)

Watch a repo

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.watch_info import WatchInfo
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo

    try:
        # Watch a repo
        api_response = api_instance.user_current_put_subscription(owner, repo)
        print("The response of RepositoryApi->user_current_put_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->user_current_put_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 

### Return type

[**WatchInfo**](WatchInfo.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WatchInfo |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tracked_times**
> List[TrackedTime] user_tracked_times(owner, repo, user)

List a user's tracked times in a repo

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_api
from gitea_api.models.tracked_time import TrackedTime
from gitea_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_api.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_api.RepositoryApi(api_client)
    owner = 'owner_example' # str | owner of the repo
    repo = 'repo_example' # str | name of the repo
    user = 'user_example' # str | username of user

    try:
        # List a user's tracked times in a repo
        api_response = api_instance.user_tracked_times(owner, repo, user)
        print("The response of RepositoryApi->user_tracked_times:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->user_tracked_times: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo | 
 **repo** | **str**| name of the repo | 
 **user** | **str**| username of user | 

### Return type

[**List[TrackedTime]**](TrackedTime.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TrackedTimeList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

