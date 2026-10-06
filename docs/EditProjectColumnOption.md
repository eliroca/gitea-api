# EditProjectColumnOption

EditProjectColumnOption represents options for editing a project column

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | Column color in 6-digit hex format, e.g. #FF0000 | [optional] 
**sorting** | **int** | Position of the column within the project, between -128 and 127 | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from gitea_api.models.edit_project_column_option import EditProjectColumnOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditProjectColumnOption from a JSON string
edit_project_column_option_instance = EditProjectColumnOption.from_json(json)
# print the JSON string representation of the object
print(EditProjectColumnOption.to_json())

# convert the object into a dict
edit_project_column_option_dict = edit_project_column_option_instance.to_dict()
# create an instance of EditProjectColumnOption from a dict
edit_project_column_option_from_dict = EditProjectColumnOption.from_dict(edit_project_column_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


