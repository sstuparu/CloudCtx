from components.json_keys import JsonKeys


class HealthInst(JsonKeys):
    def __init__(self, json_data, mo_order_number):
        cloud_ctx_health_inst = \
            json_data[self.imdata][mo_order_number][self.hcloud_ctx][self.children][0][self.health_inst][self.attributes]

        self.current_health = cloud_ctx_health_inst['cur']
        self.max_sev = cloud_ctx_health_inst['maxSev']

    @property
    def displayed_health(self):
        # print('Healthy' if int(self.current_health) == 100 else 'Unhealthy')
        return 'Healthy' if int(self.current_health) == 100 else 'Unhealthy'
