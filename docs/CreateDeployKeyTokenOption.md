# CreateDeployKeyTokenOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_only** | **bool** | Describe if the token has only read access or read/write | [optional] 
**title** | **str** | Title of the token to add | 

## Example

```python
from gitea_api.models.create_deploy_key_token_option import CreateDeployKeyTokenOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeployKeyTokenOption from a JSON string
create_deploy_key_token_option_instance = CreateDeployKeyTokenOption.from_json(json)
# print the JSON string representation of the object
print(CreateDeployKeyTokenOption.to_json())

# convert the object into a dict
create_deploy_key_token_option_dict = create_deploy_key_token_option_instance.to_dict()
# create an instance of CreateDeployKeyTokenOption from a dict
create_deploy_key_token_option_from_dict = CreateDeployKeyTokenOption.from_dict(create_deploy_key_token_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


