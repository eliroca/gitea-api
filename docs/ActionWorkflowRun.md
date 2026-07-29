# ActionWorkflowRun

ActionWorkflowRun represents a WorkflowRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**User**](User.md) |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**conclusion** | **str** |  | [optional] 
**display_title** | **str** |  | [optional] 
**event** | **str** |  | [optional] 
**head_branch** | **str** |  | [optional] 
**head_repository** | [**Repository**](Repository.md) |  | [optional] 
**head_sha** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**previous_attempt_url** | **str** | PreviousAttemptURL is the API URL of the previous attempt of this run, e.g. \&quot;.../actions/runs/{run_id}/attempts/{attempt-1}\&quot;. It is set only when the current attempt is &gt; 1 (i.e. a rerun). For the first attempt, or for legacy runs that pre-date ActionRunAttempt, it is null. | [optional] 
**pull_requests** | [**List[PullRequestMinimal]**](PullRequestMinimal.md) |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**repository_id** | **int** |  | [optional] 
**run_attempt** | **int** | RunAttempt is 1-based for runs created after ActionRunAttempt was introduced. A value of 0 is a legacy-only sentinel for runs created before attempts existed and indicates no corresponding /attempts/{n} resource is available. | [optional] 
**run_number** | **int** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**trigger_actor** | [**User**](User.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from gitea_api.models.action_workflow_run import ActionWorkflowRun

# TODO update the JSON string below
json = "{}"
# create an instance of ActionWorkflowRun from a JSON string
action_workflow_run_instance = ActionWorkflowRun.from_json(json)
# print the JSON string representation of the object
print(ActionWorkflowRun.to_json())

# convert the object into a dict
action_workflow_run_dict = action_workflow_run_instance.to_dict()
# create an instance of ActionWorkflowRun from a dict
action_workflow_run_from_dict = ActionWorkflowRun.from_dict(action_workflow_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


