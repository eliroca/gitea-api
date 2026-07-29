# CurrentAccessToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The timestamp when the token was created | [optional] 
**id** | **int** | The unique identifier of the access token | [optional] 
**last_used_at** | **datetime** | The timestamp when the token was last used | [optional] 
**name** | **str** | The name of the access token | [optional] 
**scopes** | **List[str]** | The scopes granted to this access token | [optional] 
**user** | [**UserMeta**](UserMeta.md) |  | [optional] 

## Example

```python
from gitea_api.models.current_access_token import CurrentAccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentAccessToken from a JSON string
current_access_token_instance = CurrentAccessToken.from_json(json)
# print the JSON string representation of the object
print(CurrentAccessToken.to_json())

# convert the object into a dict
current_access_token_dict = current_access_token_instance.to_dict()
# create an instance of CurrentAccessToken from a dict
current_access_token_from_dict = CurrentAccessToken.from_dict(current_access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


