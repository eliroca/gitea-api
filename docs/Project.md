# Project

Projects track issues and pull requests, standalone note cards are not supported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** | Card type: \&quot;text_only\&quot; or \&quot;images_and_text\&quot; | [optional] 
**closed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**creator** | [**User**](User.md) |  | [optional] 
**creator_id** | **int** | Deprecated: use Creator instead | [optional] 
**description** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_closed** | **bool** | Deprecated: use State instead | [optional] 
**num_closed_issues** | **int** |  | [optional] 
**num_issues** | **int** |  | [optional] 
**num_open_issues** | **int** |  | [optional] 
**owner_id** | **int** |  | [optional] 
**repo_id** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**template_type** | **str** | Template type: \&quot;none\&quot;, \&quot;basic_kanban\&quot; or \&quot;bug_triage\&quot; | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** | Project type: \&quot;individual\&quot;, \&quot;repository\&quot; or \&quot;organization\&quot; | [optional] 
**updated_at** | **datetime** | null only for legacy rows that carry no update timestamp | [optional] 

## Example

```python
from gitea_api.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


