from components.json_keys import JsonKeys


class HealthInst(JsonKeys):
    def __init__(self, json_data, mo_order_number):

        # Treating the case where there is no health inst. (Ex 13)
        if len(json_data[self.imdata][mo_order_number][self.hcloud_ctx][self.children]) == 0:
            self.current_health = 0
        else:
            cloud_ctx_health_inst = \
                json_data[self.imdata][mo_order_number][self.hcloud_ctx][self.children][0][self.health_inst][
                    self.attributes]

            self.current_health = cloud_ctx_health_inst.get('cur', 0)
            self.max_sev = cloud_ctx_health_inst['maxSev']

    @property
    def displayed_health(self):
        # print('Healthy' if int(self.current_health) == 100 else 'Unhealthy')
        return 'Healthy' if int(self.current_health) == 100 else 'Unhealthy'
