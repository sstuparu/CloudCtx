from components.health_inst import HealthInst
from components.json_keys import JsonKeys
import datetime


class CloudCtx(JsonKeys):
    # Keep track of the number of CloudCtx objects instantiated (Ex 12)
    number_of_instantiated_objects = 0

    def __init__(self, json_data, mo_order_number):
        CloudCtx.number_of_instantiated_objects += 1

        self.health_inst_object = HealthInst(json_data=json_data, mo_order_number=mo_order_number)

        cloud_ctx_attributes = json_data[self.imdata][mo_order_number][self.hcloud_ctx][self.attributes]

        self.name = cloud_ctx_attributes['name']
        self.tenant_name = cloud_ctx_attributes['tenantName']
        self.description = cloud_ctx_attributes['description']
        self.name_alias = cloud_ctx_attributes['nameAlias']
        self.ctx_profile_name = cloud_ctx_attributes['ctxProfileName']

        self.last_modified = cloud_ctx_attributes['modTs']
        # self.last_modified = datetime.datetime.strptime(self.last_modified, "%Y-%m-%dT%H:%M:%S.%f%z")
        self.last_modified_datetime_obj = datetime.datetime.fromisoformat(self.last_modified)
        self.last_modified = datetime.datetime.strftime(self.last_modified_datetime_obj, "%d-%m-%Y %I:%M:%S %p")

    def display_cloud_ctx_info(self):
        print(f"Name: {self.name or '-'}")
        print(f"Tenant name: {self.tenant_name or '-'}")
        print(f"Description: {self.description or '-'}")
        print(f"Name alias: {self.name_alias or '-'}")
        print(f"Ctx profile name: {self.ctx_profile_name or '-'}")
        print(f"Current health: {self.health_inst_object.current_health or '-'}")
        print(f"Last modified: {self.last_modified or '-'}")
        print("\n")

    @staticmethod
    def sort_by_health(mo_object_list):
        return sorted(mo_object_list, key=lambda element: int(element.health_inst_object.current_health))

    @staticmethod
    def sort_by_last_modified(mo_object_list):
        return sorted(mo_object_list, key=lambda element: element.last_modified_datetime_obj)





