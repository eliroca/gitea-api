# CreateProjectOption

CreateProjectOption represents options for creating a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** | Card type: \&quot;text_only\&quot; or \&quot;images_and_text\&quot; | [optional] 
**description** | **str** |  | [optional] 
**template_type** | **str** | Template type: \&quot;none\&quot;, \&quot;basic_kanban\&quot; or \&quot;bug_triage\&quot; | [optional] 
**title** | **str** |  | 

## Example

```python
from gitea_api.models.create_project_option import CreateProjectOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectOption from a JSON string
create_project_option_instance = CreateProjectOption.from_json(json)
# print the JSON string representation of the object
print(CreateProjectOption.to_json())

# convert the object into a dict
create_project_option_dict = create_project_option_instance.to_dict()
# create an instance of CreateProjectOption from a dict
create_project_option_from_dict = CreateProjectOption.from_dict(create_project_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


