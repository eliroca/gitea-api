# Repository

Repository represents a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_fast_forward_only_merge** | **bool** |  | [optional] 
**allow_manual_merge** | **bool** |  | [optional] 
**allow_merge_commits** | **bool** |  | [optional] 
**allow_rebase** | **bool** |  | [optional] 
**allow_rebase_explicit** | **bool** |  | [optional] 
**allow_rebase_update** | **bool** |  | [optional] 
**allow_squash_merge** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**archived_at** | **datetime** |  | [optional] 
**autodetect_manual_merge** | **bool** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**clone_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**default_allow_maintainer_edit** | **bool** |  | [optional] 
**default_branch** | **str** |  | [optional] 
**default_delete_branch_after_merge** | **bool** |  | [optional] 
**default_merge_style** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**empty** | **bool** |  | [optional] 
**external_tracker** | [**ExternalTracker**](ExternalTracker.md) |  | [optional] 
**external_wiki** | [**ExternalWiki**](ExternalWiki.md) |  | [optional] 
**fork** | **bool** |  | [optional] 
**forks_count** | **int** |  | [optional] 
**full_name** | **str** |  | [optional] 
**has_actions** | **bool** |  | [optional] 
**has_issues** | **bool** |  | [optional] 
**has_packages** | **bool** |  | [optional] 
**has_projects** | **bool** |  | [optional] 
**has_pull_requests** | **bool** |  | [optional] 
**has_releases** | **bool** |  | [optional] 
**has_wiki** | **bool** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**ignore_whitespace_conflicts** | **bool** |  | [optional] 
**internal** | **bool** |  | [optional] 
**internal_tracker** | [**InternalTracker**](InternalTracker.md) |  | [optional] 
**language** | **str** |  | [optional] 
**languages_url** | **str** |  | [optional] 
**licenses** | **List[str]** |  | [optional] 
**link** | **str** |  | [optional] 
**mirror** | **bool** |  | [optional] 
**mirror_interval** | **str** |  | [optional] 
**mirror_updated** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**object_format_name** | **str** | ObjectFormatName of the underlying git repository | [optional] 
**open_issues_count** | **int** |  | [optional] 
**open_pr_counter** | **int** |  | [optional] 
**original_url** | **str** |  | [optional] 
**owner** | [**User**](User.md) |  | [optional] 
**parent** | [**Repository**](Repository.md) |  | [optional] 
**permissions** | [**Permission**](Permission.md) |  | [optional] 
**private** | **bool** |  | [optional] 
**projects_mode** | **str** |  | [optional] 
**release_counter** | **int** |  | [optional] 
**repo_transfer** | [**RepoTransfer**](RepoTransfer.md) |  | [optional] 
**size** | **int** |  | [optional] 
**ssh_url** | **str** |  | [optional] 
**stars_count** | **int** |  | [optional] 
**template** | **bool** |  | [optional] 
**topics** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 
**watchers_count** | **int** |  | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from gitea_api.models.repository import Repository

# TODO update the JSON string below
json = "{}"
# create an instance of Repository from a JSON string
repository_instance = Repository.from_json(json)
# print the JSON string representation of the object
print(Repository.to_json())

# convert the object into a dict
repository_dict = repository_instance.to_dict()
# create an instance of Repository from a dict
repository_from_dict = Repository.from_dict(repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


