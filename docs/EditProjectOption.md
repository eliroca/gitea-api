# EditProjectOption

EditProjectOption represents options for editing a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** | Card type: \&quot;text_only\&quot; or \&quot;images_and_text\&quot; | [optional] 
**description** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from gitea_api.models.edit_project_option import EditProjectOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditProjectOption from a JSON string
edit_project_option_instance = EditProjectOption.from_json(json)
# print the JSON string representation of the object
print(EditProjectOption.to_json())

# convert the object into a dict
edit_project_option_dict = edit_project_option_instance.to_dict()
# create an instance of EditProjectOption from a dict
edit_project_option_from_dict = EditProjectOption.from_dict(edit_project_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


