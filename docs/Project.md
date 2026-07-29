# Project

Project represents a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**creator_id** | **int** | CreatorID is the user who created the project | [optional] 
**description** | **str** | Description provides details about the project | [optional] 
**id** | **int** | ID is the unique identifier for the project | [optional] 
**is_closed** | **bool** | IsClosed indicates if the project is closed | [optional] 
**owner_id** | **int** | OwnerID is the owner of the project (for org-level projects) | [optional] 
**repo_id** | **int** | RepoID is the repository this project belongs to (for repo-level projects) | [optional] 
**title** | **str** | Title is the title of the project | [optional] 
**updated_at** | **datetime** |  | [optional] 

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


