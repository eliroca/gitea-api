# EditRepoOption

EditRepoOption options when editing a repository's properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_fast_forward_only_merge** | **bool** | either &#x60;true&#x60; to allow fast-forward-only merging pull requests, or &#x60;false&#x60; to prevent fast-forward-only merging. | [optional] 
**allow_manual_merge** | **bool** | either &#x60;true&#x60; to allow mark pr as merged manually, or &#x60;false&#x60; to prevent it. | [optional] 
**allow_merge_commits** | **bool** | either &#x60;true&#x60; to allow merging pull requests with a merge commit, or &#x60;false&#x60; to prevent merging pull requests with merge commits. | [optional] 
**allow_rebase** | **bool** | either &#x60;true&#x60; to allow rebase-merging pull requests, or &#x60;false&#x60; to prevent rebase-merging. | [optional] 
**allow_rebase_explicit** | **bool** | either &#x60;true&#x60; to allow rebase with explicit merge commits (--no-ff), or &#x60;false&#x60; to prevent rebase with explicit merge commits. | [optional] 
**allow_rebase_update** | **bool** | either &#x60;true&#x60; to allow updating pull request branch by rebase, or &#x60;false&#x60; to prevent it. | [optional] 
**allow_squash_merge** | **bool** | either &#x60;true&#x60; to allow squash-merging pull requests, or &#x60;false&#x60; to prevent squash-merging. | [optional] 
**archived** | **bool** | set to &#x60;true&#x60; to archive this repository. | [optional] 
**autodetect_manual_merge** | **bool** | either &#x60;true&#x60; to enable AutodetectManualMerge, or &#x60;false&#x60; to prevent it. Note: In some special cases, misjudgments can occur. | [optional] 
**default_allow_maintainer_edit** | **bool** | set to &#x60;true&#x60; to allow edits from maintainers by default | [optional] 
**default_branch** | **str** | sets the default branch for this repository. | [optional] 
**default_delete_branch_after_merge** | **bool** | set to &#x60;true&#x60; to delete pr branch after merge by default | [optional] 
**default_merge_style** | **str** | set to a merge style to be used by this repository: \&quot;merge\&quot;, \&quot;rebase\&quot;, \&quot;rebase-merge\&quot;, \&quot;squash\&quot;, or \&quot;fast-forward-only\&quot;. | [optional] 
**description** | **str** | a short description of the repository. | [optional] 
**enable_prune** | **bool** | enable prune - remove obsolete remote-tracking references when mirroring | [optional] 
**external_tracker** | [**ExternalTracker**](ExternalTracker.md) |  | [optional] 
**external_wiki** | [**ExternalWiki**](ExternalWiki.md) |  | [optional] 
**has_actions** | **bool** | either &#x60;true&#x60; to enable actions unit, or &#x60;false&#x60; to disable them. | [optional] 
**has_issues** | **bool** | either &#x60;true&#x60; to enable issues for this repository or &#x60;false&#x60; to disable them. | [optional] 
**has_packages** | **bool** | either &#x60;true&#x60; to enable packages unit, or &#x60;false&#x60; to disable them. | [optional] 
**has_projects** | **bool** | either &#x60;true&#x60; to enable project unit, or &#x60;false&#x60; to disable them. | [optional] 
**has_pull_requests** | **bool** | either &#x60;true&#x60; to allow pull requests, or &#x60;false&#x60; to prevent pull request. | [optional] 
**has_releases** | **bool** | either &#x60;true&#x60; to enable releases unit, or &#x60;false&#x60; to disable them. | [optional] 
**has_wiki** | **bool** | either &#x60;true&#x60; to enable the wiki for this repository or &#x60;false&#x60; to disable it. | [optional] 
**ignore_whitespace_conflicts** | **bool** | either &#x60;true&#x60; to ignore whitespace for conflicts, or &#x60;false&#x60; to not ignore whitespace. | [optional] 
**internal_tracker** | [**InternalTracker**](InternalTracker.md) |  | [optional] 
**mirror_interval** | **str** | set to a string like &#x60;8h30m0s&#x60; to set the mirror interval time | [optional] 
**name** | **str** | name of the repository | [optional] 
**private** | **bool** | either &#x60;true&#x60; to make the repository private or &#x60;false&#x60; to make it public. Note: you will get a 422 error if the organization restricts changing repository visibility to organization owners and a non-owner tries to change the value of private. | [optional] 
**projects_mode** | **str** | &#x60;repo&#x60; to only allow repo-level projects, &#x60;owner&#x60; to only allow owner projects, &#x60;all&#x60; to allow both. | [optional] 
**template** | **bool** | either &#x60;true&#x60; to make this repository a template or &#x60;false&#x60; to make it a normal repository | [optional] 
**website** | **str** | a URL with more information about the repository. | [optional] 

## Example

```python
from gitea_api.models.edit_repo_option import EditRepoOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditRepoOption from a JSON string
edit_repo_option_instance = EditRepoOption.from_json(json)
# print the JSON string representation of the object
print(EditRepoOption.to_json())

# convert the object into a dict
edit_repo_option_dict = edit_repo_option_instance.to_dict()
# create an instance of EditRepoOption from a dict
edit_repo_option_from_dict = EditRepoOption.from_dict(edit_repo_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


