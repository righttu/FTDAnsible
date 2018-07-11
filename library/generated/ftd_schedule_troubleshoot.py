#!/usr/bin/python

# Copyright (c) 2018 Cisco Systems, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}

DOCUMENTATION = """
---
module: ftd_schedule_troubleshoot
short_description: Manages ScheduleTroubleshoot objects on Cisco FTD devices
version_added: "2.7"
author: "Cisco Systems, Inc."
options:
  operation:
    description:
      - Specified the name of the operation to execute in the task.
    required: true
  register_as:
    description:
      - Specifies Ansible fact name that is used to register received response from the FTD device.
  filter
    description:
      - The criteria used to filter the models you are requesting. It should have the following format: {field}{operator}{value}[;{field}{operator}{value}]. Supported operators are: "!"(not equals), ":"(equals), "<"(null), "~"(similar), ">"(null). Supported fields are: "name".
  forceOperation
    description:
      - For Internal use.
  id
    description:
      - A unique string identifier assigned by the system when the object is created. No assumption can be made on the format or content of this identifier. The identifier must be provided whenever attempting to modify/delete (or reference) an existing object.<br>Field level constraints: must match pattern ^((?!;).)*$, cannot have HTML. (Note: Additional constraints might exist)
  ipAddress
    description:
      - IP address of actor who initiated a job execution<br>Field level constraints: must match pattern ^((?!;).)*$, cannot have HTML. (Note: Additional constraints might exist)
  jobHistoryUuid
    description:
      - For Internal use.<br>Field level constraints: must match pattern ^((?!;).)*$, cannot have HTML. (Note: Additional constraints might exist)
  jobName
    description:
      - See derived class.
  limit
    description:
      - An integer representing the maximum amount of objects to return. If not specified, the maximum amount is 10
  offset
    description:
      - An integer representing the index of the first requested object. Index starts from 0. If not specified, the returned objects will start from index 0
  scheduleType
    description:
      - A mandatory enum value that specifies the type of job schedule. Only allowed value is:<p>IMMEDIATE - the job will be posted when the request is received. <p>Note that the job will be posted in the queue when it is received, but the actual execution can be delayed if other jobs were scheduled for execution at the same time or are being currently processed. After a system restart the job will not be recovered.
  sort
    description:
      - The field used to sort the requested object list
  type
    description:
      - A UTF8 string, all letters lower-case, that represents the class-type. This corresponds to the class name.
  user
    description:
      - System provided ID of the user who scheduled the job.<br>Field level constraints: must match pattern ^((?!;).)*$, cannot have HTML. (Note: Additional constraints might exist)
  version
    description:
      - A unique string version assigned by the system when the object is created or modified. No assumption can be made on the format or content of this identifier. The identifier must be provided whenever attempting to modify/delete an existing object. As the version will change every time the object is modified, the value provided in this identifier must match exactly what is present in the system or the request will be rejected.

extends_documentation_fragment: ftd
"""

EXAMPLES = """
- name: Fetch ScheduleTroubleshoot with a given name
  ftd_schedule_troubleshoot:
    hostname: "https://127.0.0.1:8585"
    access_token: 'ACCESS_TOKEN'
    refresh_token: 'REFRESH_TOKEN'
    operation: "getScheduleTroubleshootByName"
    name: "Ansible ScheduleTroubleshoot"

- name: Create a ScheduleTroubleshoot
  ftd_schedule_troubleshoot:
    hostname: "https://127.0.0.1:8585"
    access_token: 'ACCESS_TOKEN'
    refresh_token: 'REFRESH_TOKEN'
    operation: 'addScheduleTroubleshoot'

    type: "scheduletroubleshoot"
"""

RETURN = """
response:
  description: HTTP response returned from the API call.
  returned: success
  type: dict
error_code:
  description: HTTP error code returned from the server.
  returned: error
  type: int
msg:
  description: Error message returned from the server.
  returned: error
  type: dict
"""
import json

from ansible.module_utils.authorization import retry_on_token_expiration
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.http import construct_url, base_headers, iterate_over_pageable_resource, DEFAULT_CHARSET
from ansible.module_utils.misc import dict_subset, construct_module_result, copy_identity_properties
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible.module_utils.urls import open_url


class ScheduleTroubleshootResource(object):
    
    @staticmethod
    @retry_on_token_expiration
    def addScheduleTroubleshoot(params):
        body_params = dict_subset(params, ['forceOperation', 'id', 'ipAddress', 'jobHistoryUuid', 'jobName', 'scheduleType', 'type', 'user', 'version'])

        url = construct_url(params['hostname'], '/action/troubleshoot')
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='POST',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params)
        content = response.read().decode(response.headers.get_content_charset(DEFAULT_CHARSET))
        return json.loads(content) if content else content

    @staticmethod
    @retry_on_token_expiration
    def deleteScheduleTroubleshoot(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/action/troubleshoot/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='DELETE',
        )

        response = open_url(url, **request_params)
        content = response.read().decode(response.headers.get_content_charset(DEFAULT_CHARSET))
        return json.loads(content) if content else content

    @staticmethod
    @retry_on_token_expiration
    def editScheduleTroubleshoot(params):
        path_params = dict_subset(params, ['objId'])
        body_params = dict_subset(params, ['forceOperation', 'id', 'ipAddress', 'jobHistoryUuid', 'jobName', 'scheduleType', 'type', 'user', 'version'])

        url = construct_url(params['hostname'], '/action/troubleshoot/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='PUT',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params)
        content = response.read().decode(response.headers.get_content_charset(DEFAULT_CHARSET))
        return json.loads(content) if content else content

    @staticmethod
    @retry_on_token_expiration
    def getScheduleTroubleshoot(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/action/troubleshoot/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='GET',
        )

        response = open_url(url, **request_params)
        content = response.read().decode(response.headers.get_content_charset(DEFAULT_CHARSET))
        return json.loads(content) if content else content

    @staticmethod
    @retry_on_token_expiration
    def getScheduleTroubleshootList(params):
        query_params = dict_subset(params, ['filter', 'limit', 'offset', 'sort'])

        url = construct_url(params['hostname'], '/action/troubleshoot', query_params=query_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='GET',
        )

        response = open_url(url, **request_params)
        content = response.read().decode(response.headers.get_content_charset(DEFAULT_CHARSET))
        return json.loads(content) if content else content

    @staticmethod
    @retry_on_token_expiration
    def getScheduleTroubleshootByName(params):
        search_params = params.copy()
        search_params['filter'] = 'name:%s' % params['name']
        item_generator = iterate_over_pageable_resource(ScheduleTroubleshootResource.getScheduleTroubleshootList, search_params)
        return next(item for item in item_generator if item['name'] == params['name'])

    @staticmethod
    @retry_on_token_expiration
    def upsertScheduleTroubleshoot(params):
        def is_duplicate_name_error(err):
            err_msg = err.read().decode(err.headers.get_content_charset(DEFAULT_CHARSET))
            return err.code == 422 and "Validation failed due to a duplicate name" in err_msg

        try:
            return ScheduleTroubleshootResource.addScheduleTroubleshoot(params)
        except HTTPError as e:
            if is_duplicate_name_error(e):
                existing_object = ScheduleTroubleshootResource.getScheduleTroubleshootByName(params)
                params = copy_identity_properties(existing_object, params)
                return ScheduleTroubleshootResource.editScheduleTroubleshoot(params)
            else:
                raise e

    @staticmethod
    @retry_on_token_expiration
    def editScheduleTroubleshootByName(params):
        existing_object = ScheduleTroubleshootResource.getScheduleTroubleshootByName(params)
        params = copy_identity_properties(existing_object, params)
        return ScheduleTroubleshootResource.editScheduleTroubleshoot(params)

    @staticmethod
    @retry_on_token_expiration
    def deleteScheduleTroubleshootByName(params):
        existing_object = ScheduleTroubleshootResource.getScheduleTroubleshootByName(params)
        params = copy_identity_properties(existing_object, params)
        return ScheduleTroubleshootResource.deleteScheduleTroubleshoot(params)


def main():
    fields = dict(
        hostname=dict(type='str', required=True),
        access_token=dict(type='str', required=True),
        refresh_token=dict(type='str', required=True),

        operation=dict(type='str', default='upsertScheduleTroubleshoot', choices=['addScheduleTroubleshoot', 'deleteScheduleTroubleshoot', 'editScheduleTroubleshoot', 'getScheduleTroubleshoot', 'getScheduleTroubleshootList', 'getScheduleTroubleshootByName', 'upsertScheduleTroubleshoot', 'editScheduleTroubleshootByName', 'deleteScheduleTroubleshootByName']),
        register_as=dict(type='str'),

        filter=dict(type='str'),
        forceOperation=dict(type='bool'),
        id=dict(type='str'),
        ipAddress=dict(type='str'),
        jobHistoryUuid=dict(type='str'),
        jobName=dict(type='str'),
        limit=dict(type='int'),
        objId=dict(type='str'),
        offset=dict(type='int'),
        scheduleType=dict(type='str'),
        sort=dict(type='str'),
        type=dict(type='str'),
        user=dict(type='str'),
        version=dict(type='str'),
    )

    module = AnsibleModule(argument_spec=fields)
    params = module.params

    try:
        method_to_call = getattr(ScheduleTroubleshootResource, params['operation'])
        response = method_to_call(params)
        result = construct_module_result(response, params)
        module.exit_json(**result)
    except HTTPError as e:
        err_msg = e.read().decode(e.headers.get_content_charset(DEFAULT_CHARSET))
        module.fail_json(changed=False, msg=json.loads(err_msg) if err_msg else {}, error_code=e.code)
    except Exception as e:
        module.fail_json(changed=False, msg=str(e))


if __name__ == '__main__':
    main()
