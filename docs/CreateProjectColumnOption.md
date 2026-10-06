# CreateProjectColumnOption

CreateProjectColumnOption represents options for creating a project column

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | Column color in 6-digit hex format, e.g. #FF0000 | [optional] 
**title** | **str** |  | 

## Example

```python
from gitea_api.models.create_project_column_option import CreateProjectColumnOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectColumnOption from a JSON string
create_project_column_option_instance = CreateProjectColumnOption.from_json(json)
# print the JSON string representation of the object
print(CreateProjectColumnOption.to_json())

# convert the object into a dict
create_project_column_option_dict = create_project_column_option_instance.to_dict()
# create an instance of CreateProjectColumnOption from a dict
create_project_column_option_from_dict = CreateProjectColumnOption.from_dict(create_project_column_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


