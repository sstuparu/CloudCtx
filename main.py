import unittest
import json
from cloud_ctx import CloudCtx
from health_inst import HealthInst


class JsonTests(unittest.TestCase):
    with open('CloudCtx.json', 'r') as json_to_read:
        cloud_ctx_dict = json.load(json_to_read)

    total_hcloud_ctx_no = int(cloud_ctx_dict['totalCount'])

    def test_create_and_display_objects(self):
        # Ex 1 2 3 4
        hcloud_ctx_objects_list = list()

        for no in range(self.total_hcloud_ctx_no):
            hcloud_ctx_objects_list.append(CloudCtx(self.cloud_ctx_dict, no))

        for no, hcloud_ctx_object in enumerate(hcloud_ctx_objects_list, start=1):
            print(f"Object no {no}:\n{50*'='}")
            hcloud_ctx_object.display_cloud_ctx_info()

    def test_health_inst(self):
        # Ex 5 6 7
        health_inst_objects_list = list()

        for no in range(self.total_hcloud_ctx_no):
            health_inst_objects_list.append(HealthInst(self.cloud_ctx_dict, no))

        for no, obj in enumerate(health_inst_objects_list, start=1):
            obj.displayed_health()

    def test_cloudctx_and_healthinst(self):
        # Ex 8 9
        objects = list()

        for no in range(self.total_hcloud_ctx_no):
            objects.append(CloudCtx(self.cloud_ctx_dict, no))

        for i, obj in enumerate(objects):
            print(obj.name)
            print(obj.tenant_name)
            obj.health_inst_object.displayed_health()
            print('\n')


