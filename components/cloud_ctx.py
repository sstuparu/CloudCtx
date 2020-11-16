from components.health_inst import HealthInst
from components.json_keys import JsonKeys


class CloudCtx(JsonKeys):

    def __init__(self, json_data, mo_order_number):
        self.health_inst_object = HealthInst(json_data=json_data, mo_order_number=mo_order_number)

        cloud_ctx_attributes = json_data[self.imdata][mo_order_number][self.hcloud_ctx][self.attributes]

        self.name = cloud_ctx_attributes['name']
        self.tenant_name = cloud_ctx_attributes['tenantName']
        self.description = cloud_ctx_attributes['description']
        self.name_alias = cloud_ctx_attributes['nameAlias']
        self.ctx_profile_name = cloud_ctx_attributes['ctxProfileName']

    def display_cloud_ctx_info(self):
        print(f"Name: {self.name or '-'}")
        print(f"Tenant name: {self.tenant_name or '-'}")
        print(f"Description: {self.description or '-'}")
        print(f"Name alias: {self.name_alias or '-'}")
        print(f"Ctx profile name: {self.ctx_profile_name or '-'}")
        print("\n")





