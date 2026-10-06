# MoveProjectColumnsOption

MoveProjectColumnsOption represents options for reordering a project's columns

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_ids** | **List[int]** | Every column ID of the project, in the desired left-to-right order | 

## Example

```python
from gitea_api.models.move_project_columns_option import MoveProjectColumnsOption

# TODO update the JSON string below
json = "{}"
# create an instance of MoveProjectColumnsOption from a JSON string
move_project_columns_option_instance = MoveProjectColumnsOption.from_json(json)
# print the JSON string representation of the object
print(MoveProjectColumnsOption.to_json())

# convert the object into a dict
move_project_columns_option_dict = move_project_columns_option_instance.to_dict()
# create an instance of MoveProjectColumnsOption from a dict
move_project_columns_option_from_dict = MoveProjectColumnsOption.from_dict(move_project_columns_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


