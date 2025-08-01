# PackageFile

PackageFile represents a package file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**md5** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**sha1** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 
**sha512** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from gitea_api.models.package_file import PackageFile

# TODO update the JSON string below
json = "{}"
# create an instance of PackageFile from a JSON string
package_file_instance = PackageFile.from_json(json)
# print the JSON string representation of the object
print(PackageFile.to_json())

# convert the object into a dict
package_file_dict = package_file_instance.to_dict()
# create an instance of PackageFile from a dict
package_file_from_dict = PackageFile.from_dict(package_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


