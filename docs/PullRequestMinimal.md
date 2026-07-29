# PullRequestMinimal

PullRequestMinimal is the minimal information about a pull request, as returned in the `pull_requests` field of a workflow run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**PullRequestMinimalHead**](PullRequestMinimalHead.md) |  | [optional] 
**head** | [**PullRequestMinimalHead**](PullRequestMinimalHead.md) |  | [optional] 
**id** | **int** |  | [optional] 
**number** | **int** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from gitea_api.models.pull_request_minimal import PullRequestMinimal

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestMinimal from a JSON string
pull_request_minimal_instance = PullRequestMinimal.from_json(json)
# print the JSON string representation of the object
print(PullRequestMinimal.to_json())

# convert the object into a dict
pull_request_minimal_dict = pull_request_minimal_instance.to_dict()
# create an instance of PullRequestMinimal from a dict
pull_request_minimal_from_dict = PullRequestMinimal.from_dict(pull_request_minimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


