# ProjectColumn

ProjectColumn represents a project column (board)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**creator** | [**User**](User.md) |  | [optional] 
**default** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**sorting** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **datetime** | null only for legacy rows that carry no update timestamp | [optional] 

## Example

```python
from gitea_api.models.project_column import ProjectColumn

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectColumn from a JSON string
project_column_instance = ProjectColumn.from_json(json)
# print the JSON string representation of the object
print(ProjectColumn.to_json())

# convert the object into a dict
project_column_dict = project_column_instance.to_dict()
# create an instance of ProjectColumn from a dict
project_column_from_dict = ProjectColumn.from_dict(project_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


