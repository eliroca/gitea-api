# IssueAssigneesOption

IssueAssigneesOption options for adding/removing issue assignees

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignees** | **List[str]** |  | [optional] 

## Example

```python
from gitea_api.models.issue_assignees_option import IssueAssigneesOption

# TODO update the JSON string below
json = "{}"
# create an instance of IssueAssigneesOption from a JSON string
issue_assignees_option_instance = IssueAssigneesOption.from_json(json)
# print the JSON string representation of the object
print(IssueAssigneesOption.to_json())

# convert the object into a dict
issue_assignees_option_dict = issue_assignees_option_instance.to_dict()
# create an instance of IssueAssigneesOption from a dict
issue_assignees_option_from_dict = IssueAssigneesOption.from_dict(issue_assignees_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


