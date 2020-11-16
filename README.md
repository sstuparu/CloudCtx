# json tutorial

1. Create a class CloudCtx that would hold the information for a hcloudCtx MO.
2. From the json dict retrieve the following information and save it as object attributes:
    - name
    - tenant_name
    - description
    - name_alias
    - ctx_profile_name
3. Write a method that can displays the CloudCtx object information (name, tenant_name, description, name_alias, ctx_profile_name)
4. For each attribute, if value from backend is "" display the property as "-"

5. Create a class HealthInst that would hold the information for a healthInst MO
6. From the json dict retrieve the following information and save it as object attributes:
    - current_health ("cur" key in json)
    - max_sev
    
7. Add a property to the MO called displayed_health that would display "Healthy" if current_health is 100 and "Unhealthy" if current_health is lower than 100

8. Add an attribute to CloudCtx that holds a reference to the corresponding HealthInst instance

9. Parse the below example JSON and create 3 CloudCtx that each has a HealthInst and display the following information: CloudCtx - name and tenant_name with corresponding health (displayed_health)

10. Update method at point 4 to include the correspoding health information from HealthInst

11. Display the ojects in order of the current health (cur attribute of healthInst) - lowest to highest

12. Keep track of the number of CloudCtx objects instantiated (at any point you can display how many CloudCtx objects were created)

13. Take into consideration that hcloudCtx MO may not have a healthInst. In this case you can make the assumption that the hcloudCtx MO has 0 health (most 'unhealthy') and add a new dictionary in the json example for this case (children will be empty list). Repeat tests at point 9/10/11

14. Add an attribute to the CloudCtx object that displays when it was last modified ("modTs" key in json). The format should be the following: <day-month-year hour:minute:second Am/PM>. Add this information to the method created at point 3

15. Display the ojects from the one modified most recently to the oldest one modified 


``` json
{
   "totalCount":"3",
   "imdata":[
      {
         "hcloudCtx":{
            "attributes":{
               "awsVPC":"",
               "azResourceGroup":"",
               "azVirtualNetwork":"",
               "childAction":"",
               "ctxProfileName":"ct_ctxprofile_us-west-1",
               "delegateDn":"uni/tn-infra/ctxprofile-ct_ctxprofile_us-west-1",
               "description":"",
               "dn":"acct-[infra]/region-[us-west-1]/context-[overlay-1]-addr-[10.10.0.0/25]",
               "encap":"16777199",
               "encapType":"vxlan",
               "fvCtxDn":"uni/tn-infra/ctx-overlay-1",
               "interSitePeeringEnabled":"yes",
               "lcOwn":"local",
               "modTs":"2020-10-22T16:27:14.966+00:00",
               "name":"overlay-1",
               "nameAlias":"",
               "primaryCidr":"10.10.0.0/25",
               "resolvedObjDn":"ctxdefcont/ctxProfileVrfDef-[uni/tn-infra/ctxprofile-ct_ctxprofile_us-west-1]-ctxDef-[uni/tn-infra/ctx-overlay-1]",
               "status":"",
               "tenantName":"infra",
               "type":"regular"
            },
            "children":[
               {
                  "healthInst":{
                     "attributes":{
                        "childAction":"",
                        "chng":"0",
                        "cur":"100",
                        "maxSev":"cleared",
                        "prev":"100",
                        "rn":"health",
                        "status":"",
                        "twScore":"100",
                        "updTs":"2020-10-27T12:46:50.008+00:00"
                     }
                  }
               }
            ]
         }
      },
      {
         "hcloudCtx":{
            "attributes":{
               "awsVPC":"",
               "azResourceGroup":"",
               "azVirtualNetwork":"",
               "childAction":"",
               "ctxProfileName":"CLD_CTX_PROF_FOR_SG",
               "delegateDn":"uni/tn-Tenant_sg/ctxprofile-CLD_CTX_PROF_FOR_SG",
               "description":"",
               "dn":"acct-[Tenant_sg]/region-[us-west-1]/context-[Vrf_sg]-addr-[20.20.0.0/16]",
               "encap":"2719747",
               "encapType":"vxlan",
               "fvCtxDn":"uni/tn-Tenant_sg/ctx-Vrf_sg",
               "interSitePeeringEnabled":"no",
               "lcOwn":"local",
               "modTs":"2020-10-26T13:31:18.280+00:00",
               "name":"Vrf_sg",
               "nameAlias":"",
               "primaryCidr":"20.20.0.0/16",
               "resolvedObjDn":"ctxdefcont/ctxProfileVrfDef-[uni/tn-Tenant_sg/ctxprofile-CLD_CTX_PROF_FOR_SG]-ctxDef-[uni/tn-Tenant_sg/ctx-Vrf_sg]",
               "status":"",
               "tenantName":"Tenant_sg",
               "type":"regular"
            },
            "children":[
               {
                  "healthInst":{
                     "attributes":{
                        "childAction":"",
                        "chng":"0",
                        "cur":"100",
                        "maxSev":"cleared",
                        "prev":"100",
                        "rn":"health",
                        "status":"",
                        "twScore":"100",
                        "updTs":"2020-10-27T12:46:50.008+00:00"
                     }
                  }
               }
            ]
         }
      },
      {
         "hcloudCtx":{
            "attributes":{
               "awsVPC":"",
               "azResourceGroup":"",
               "azVirtualNetwork":"",
               "childAction":"",
               "ctxProfileName":"ct_ctxprofile_us-west-2",
               "delegateDn":"uni/tn-infra/ctxprofile-ct_ctxprofile_us-west-2",
               "description":"",
               "dn":"acct-[infra]/region-[us-west-2]/context-[overlay-1]-addr-[11.11.11.0/25]",
               "encap":"16777199",
               "encapType":"vxlan",
               "fvCtxDn":"uni/tn-infra/ctx-overlay-1",
               "interSitePeeringEnabled":"yes",
               "lcOwn":"local",
               "modTs":"2020-10-27T09:45:41.089+00:00",
               "name":"overlay-1",
               "nameAlias":"",
               "primaryCidr":"11.11.11.0/25",
               "resolvedObjDn":"ctxdefcont/ctxProfileVrfDef-[uni/tn-infra/ctxprofile-ct_ctxprofile_us-west-2]-ctxDef-[uni/tn-infra/ctx-overlay-1]",
               "status":"",
               "tenantName":"infra",
               "type":"regular"
            },
            "children":[
               {
                  "healthInst":{
                     "attributes":{
                        "childAction":"",
                        "chng":"0",
                        "cur":"100",
                        "maxSev":"cleared",
                        "prev":"100",
                        "rn":"health",
                        "status":"",
                        "twScore":"100",
                        "updTs":"2020-10-27T12:46:50.008+00:00"
                     }
                  }
               }
            ]
         }
      }
   ]
}
```
