# MoveProjectIssueOption

MoveProjectIssueOption represents options for moving an issue between columns

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_id** | **int** | Target column to move the issue into | 
**sorting** | **int** | Position within the column, ascending. Omit to append. Negative values sort above the rest, equal values are ordered newest first. | [optional] 

## Example

```python
from gitea_api.models.move_project_issue_option import MoveProjectIssueOption

# TODO update the JSON string below
json = "{}"
# create an instance of MoveProjectIssueOption from a JSON string
move_project_issue_option_instance = MoveProjectIssueOption.from_json(json)
# print the JSON string representation of the object
print(MoveProjectIssueOption.to_json())

# convert the object into a dict
move_project_issue_option_dict = move_project_issue_option_instance.to_dict()
# create an instance of MoveProjectIssueOption from a dict
move_project_issue_option_from_dict = MoveProjectIssueOption.from_dict(move_project_issue_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


