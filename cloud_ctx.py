from health_inst import HealthInst
from json_keys import JsonKeys


class CloudCtx(JsonKeys):

    def __init__(self, json_data, person_number):
        self.health_inst_object = HealthInst(json_data=json_data, person_number=person_number)

        cloud_ctx_attributes = json_data[self.imdata][person_number][self.hcloud_ctx][self.attributes]

        self.name = cloud_ctx_attributes['name']
        self.tenant_name = cloud_ctx_attributes['tenantName']
        self.description = cloud_ctx_attributes['description']
        self.name_alias = cloud_ctx_attributes['nameAlias']
        self.ctx_profile_name = cloud_ctx_attributes['ctxProfileName']

    def display_cloud_ctx_info(self):
        print(f"Name: {self.name}" if self.name else 'Name: -')
        print(f"Tenant name: {self.tenant_name}" if self.tenant_name else 'Tenant name: -')
        print(f"Description: {self.description}" if self.description else 'Description: -')
        print(f"Name alias: {self.name_alias}" if self.name_alias else 'Name alias: -')
        print(f"Ctx profile name: {self.ctx_profile_name}" if self.ctx_profile_name else 'Ctx profile name: -')
        print("\n")





