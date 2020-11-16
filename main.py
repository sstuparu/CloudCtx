import unittest
import json
from components.cloud_ctx import CloudCtx
from components.health_inst import HealthInst


class JsonTests(unittest.TestCase):
    with open('json_files/demo_response_capic.json', 'r') as json_to_read:
        cloud_ctx_dict = json.load(json_to_read)

    total_hcloud_ctx_no = int(cloud_ctx_dict['totalCount'])

    def test_create_and_display_objects(self):
        # Ex 1 2 3 4 10 11 12 15
        hcloud_ctx_objects_list = list()

        # Create CloudCtx objects for each hcloud ctx mo in the json dictionary
        for no in range(self.total_hcloud_ctx_no):
            hcloud_ctx_objects_list.append(CloudCtx(self.cloud_ctx_dict, no))
        
        # Sort objects by health (Ex 11)
        # hcloud_ctx_objects_list = sorted(hcloud_ctx_objects_list,
        #                                  key=lambda element: int(element.health_inst_object.current_health))

        hcloud_ctx_objects_list = CloudCtx.sort_by_health(mo_object_list=hcloud_ctx_objects_list)

        for no, hcloud_ctx_object in enumerate(hcloud_ctx_objects_list, start=1):
            print(f"Object no {no}:\n{50*'='}")
            hcloud_ctx_object.display_cloud_ctx_info()

        hcloud_ctx_objects_list = CloudCtx.sort_by_last_modified(mo_object_list=hcloud_ctx_objects_list)

        for no, hcloud_ctx_object in enumerate(hcloud_ctx_objects_list, start=1):
            print(f"Object no {no}:\n{50 * '='}")
            hcloud_ctx_object.display_cloud_ctx_info()

        # Ex 12 demo
        print(f"Number of CloudCtx objects instantiated: {CloudCtx.number_of_instantiated_objects}")

    def test_health_inst(self):
        # Ex 5 6 7
        health_inst_objects_list = list()

        # Crate HealthInst objects for each mo present in json dictionary
        for no in range(self.total_hcloud_ctx_no):
            health_inst_objects_list.append(HealthInst(self.cloud_ctx_dict, no))

        for no, obj in enumerate(health_inst_objects_list, start=1):
            print(obj.displayed_health)

    def test_cloudctx_and_healthinst(self):
        # Ex 8 9
        objects = list()

        # Create CloudCtx objects for each hcloud ctx mo in the json dictionary
        for no in range(self.total_hcloud_ctx_no):
            objects.append(CloudCtx(self.cloud_ctx_dict, no))

        for i, obj in enumerate(objects):
            print(obj.name)
            print(obj.tenant_name)
            print(obj.health_inst_object.displayed_health)
            print('\n')


