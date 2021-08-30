from pprint import pprint

from classes import Node, Edge, Graph, GCP
json = [{
   "name":"//cloudbilling.googleapis.com/billingAccounts/01B2E0-10D255-037E4D",
   "asset_type":"cloudbilling.googleapis.com/BillingAccount",
   "iam_policy":{
      "etag":"BwWbYe3dxQk=",
      "bindings":[
         {
            "role":"roles/billing.admin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/folders/188906894377",
   "asset_type":"cloudresourcemanager.googleapis.com/Folder",
   "iam_policy":{
      "etag":"BwWbYXSvzgs=",
      "bindings":[
         {
            "role":"roles/owner",
            "members":[
               "serviceAccount:dev-manager@striking-arbor-264209.iam.gserviceaccount.com",
               "serviceAccount:devops-dude-1@striking-arbor-264209.iam.gserviceaccount.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderAdmin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderEditor",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "folders/188906894377",
      "folders/767216091627",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/folders/36290848176",
   "asset_type":"cloudresourcemanager.googleapis.com/Folder",
   "iam_policy":{
      "etag":"BwWbYPZvrKE=",
      "bindings":[
         {
            "role":"roles/resourcemanager.folderAdmin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderEditor",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "folders/36290848176",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/folders/495694787245",
   "asset_type":"cloudresourcemanager.googleapis.com/Folder",
   "iam_policy":{
      "etag":"BwWbYSFk8bU=",
      "bindings":[
         {
            "role":"roles/resourcemanager.folderAdmin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderEditor",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "folders/495694787245",
      "folders/36290848176",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/folders/635215680011",
   "asset_type":"cloudresourcemanager.googleapis.com/Folder",
   "iam_policy":{
      "etag":"BwWbYW+eUFc=",
      "bindings":[
         {
            "role":"roles/owner",
            "members":[
               "serviceAccount:dev-manager@striking-arbor-264209.iam.gserviceaccount.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderAdmin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderEditor",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "folders/635215680011",
      "folders/767216091627",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/folders/518729943705",
   "asset_type":"cloudresourcemanager.googleapis.com/Folder",
   "iam_policy":{
      "etag":"BwWbYTmoy5Y=",
      "bindings":[
         {
            "role":"roles/resourcemanager.folderAdmin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderEditor",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "folders/518729943705",
      "folders/635215680011",
      "folders/767216091627",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/folders/767216091627",
   "asset_type":"cloudresourcemanager.googleapis.com/Folder",
   "iam_policy":{
      "etag":"BwWbYW62eXU=",
      "bindings":[
         {
            "role":"roles/resourcemanager.folderAdmin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderEditor",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/viewer",
            "members":[
               "serviceAccount:dev-manager@striking-arbor-264209.iam.gserviceaccount.com"
            ]
         }
      ]
   },
   "ancestors":[
      "folders/767216091627",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/folders/93198982071",
   "asset_type":"cloudresourcemanager.googleapis.com/Folder",
   "iam_policy":{
      "etag":"BwWbYTV1QFI=",
      "bindings":[
         {
            "role":"roles/resourcemanager.folderAdmin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderEditor",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "folders/93198982071",
      "folders/96505015065",
      "folders/767216091627",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/folders/361332156337",
   "asset_type":"cloudresourcemanager.googleapis.com/Folder",
   "iam_policy":{
      "etag":"BwWbYY2YQKY=",
      "bindings":[
         {
            "role":"roles/resourcemanager.folderAdmin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderEditor",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "folders/361332156337",
      "folders/96505015065",
      "folders/767216091627",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/folders/837642324986",
   "asset_type":"cloudresourcemanager.googleapis.com/Folder",
   "iam_policy":{
      "etag":"BwWbYWkcDWk=",
      "bindings":[
         {
            "role":"roles/resourcemanager.folderAdmin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderEditor",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "folders/837642324986",
      "folders/635215680011",
      "folders/767216091627",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/folders/96505015065",
   "asset_type":"cloudresourcemanager.googleapis.com/Folder",
   "iam_policy":{
      "etag":"BwWbYY+VoIY=",
      "bindings":[
         {
            "role":"roles/resourcemanager.folderAdmin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderEditor",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/viewer",
            "members":[
               "group:reviewers@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "folders/96505015065",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/organizations/1066060271767",
   "asset_type":"cloudresourcemanager.googleapis.com/Organization",
   "iam_policy":{
      "etag":"BwWbYb7pDdw=",
      "bindings":[
         {
            "role":"roles/billing.creator",
            "members":[
               "domain:test.authomize.com"
            ]
         },
         {
            "role":"roles/browser",
            "members":[
               "serviceAccount:exercise-fetcher@striking-arbor-264209.iam.gserviceaccount.com"
            ]
         },
         {
            "role":"roles/cloudasset.owner",
            "members":[
               "serviceAccount:exercise-fetcher@striking-arbor-264209.iam.gserviceaccount.com"
            ]
         },
         {
            "role":"roles/iam.securityReviewer",
            "members":[
               "serviceAccount:exercise-fetcher@striking-arbor-264209.iam.gserviceaccount.com"
            ]
         },
         {
            "role":"roles/owner",
            "members":[
               "serviceAccount:exercise-fetcher@striking-arbor-264209.iam.gserviceaccount.com",
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderAdmin",
            "members":[
               "user:ron@test.authomize.com"
            ]
         },
         {
            "role":"roles/resourcemanager.folderViewer",
            "members":[
               "serviceAccount:exercise-fetcher@striking-arbor-264209.iam.gserviceaccount.com"
            ]
         },
         {
            "role":"roles/resourcemanager.organizationViewer",
            "members":[
               "serviceAccount:exercise-fetcher@striking-arbor-264209.iam.gserviceaccount.com"
            ]
         },
         {
            "role":"roles/resourcemanager.projectCreator",
            "members":[
               "domain:test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/projects/185023072868",
   "asset_type":"cloudresourcemanager.googleapis.com/Project",
   "iam_policy":{
      "etag":"BwWbY3slQM4=",
      "bindings":[
         {
            "role":"roles/editor",
            "members":[
               "serviceAccount:service-377145543109@gcp-sa-cloudasset.iam.gserviceaccount.com"
            ]
         },
         {
            "role":"roles/owner",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "projects/185023072868",
      "organizations/1066060271767"
   ]
},{
   "name":"//storage.googleapis.com/authomize-exercise-data",
   "asset_type":"storage.googleapis.com/Bucket",
   "iam_policy":{
      "etag":"BwWbY3LgarI=",
      "bindings":[
         {
            "role":"roles/storage.legacyBucketOwner",
            "members":[
               "projectEditor:intrepid-fiber-264210",
               "projectOwner:intrepid-fiber-264210"
            ]
         },
         {
            "role":"roles/storage.legacyBucketReader",
            "members":[
               "projectViewer:intrepid-fiber-264210"
            ]
         }
      ]
   },
   "ancestors":[
      "projects/185023072868",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/projects/20671306372",
   "asset_type":"cloudresourcemanager.googleapis.com/Project",
   "iam_policy":{
      "etag":"BwWbYPhg0Ms=",
      "bindings":[
         {
            "role":"roles/owner",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "projects/20671306372",
      "folders/36290848176",
      "organizations/1066060271767"
   ]
},{
   "name":"//cloudresourcemanager.googleapis.com/projects/377145543109",
   "asset_type":"cloudresourcemanager.googleapis.com/Project",
   "iam_policy":{
      "etag":"BwWbYb/moyI=",
      "bindings":[
         {
            "role":"roles/cloudasset.serviceAgent",
            "members":[
               "serviceAccount:service-377145543109@gcp-sa-cloudasset.iam.gserviceaccount.com"
            ]
         },
         {
            "role":"roles/owner",
            "members":[
               "user:ron@test.authomize.com"
            ]
         }
      ]
   },
   "ancestors":[
      "projects/377145543109",
      "organizations/1066060271767"
   ]
}]
nodes = []
edges = []


def role_splitter(a):
    role = a.split('/')[-1]
    return role


def member_splitter(a):
    for i in a:
        member = i.split(':')[-1]
        return member


def user_premission(user_input):
    user_roles = []
    user_ancestors = []
    for i in json:
        gcp = GCP(i)
        edge = Edge(gcp.ancestors(), gcp.bindings(), gcp.from_node(), gcp.to_node_id())
        for user in edge.bindings['bindings']:
            if user_input in member_splitter(user['members']):
                if user['role'] not in user_roles:
                    user_roles.append(role_splitter(user['role']))
                for anc in gcp.to_node_id()['to_node_id']:
                    if anc not in user_ancestors:
                        user_ancestors.append(anc)


        # for node_id in edge.to_node_id['to_node_id']:
        #     if node_id not in user_ancestors:
        #         user_ancestors.append(node_id)

    print(f'User have premissions:')
    for i in user_roles:
        print(i)
    print('In this ancestors:')
    for i in user_ancestors:
        print(i)



def second_task(user_input):
    for i in json:
        gcp = GCP(i)
        edge = Edge(gcp.ancestors(), gcp.bindings(), gcp.from_node(), gcp.to_node_id())
        node = Node(gcp.asset_type(), gcp.id_resource())
        if node.id_resource == user_input:
            print(edge.ancestors)


def third_task(user_input):
    for i in json:
        gcp = GCP(i)
        edge = Edge(gcp.ancestors(), gcp.bindings(), gcp.from_node(), gcp.to_node_id())
        node = Node(gcp.asset_type(), gcp.id_resource())
        listt = []
        for user in edge.bindings['bindings']:
            if user_input == member_splitter(user['members']):
                listt.append([node.id_resource, node.asset_type, role_splitter(user['role'])])
        if not listt:
            continue
        else:
            print(listt)


def fourth_task(user_input):
    for i in json:
        gcp = GCP(i)
        edge = Edge(gcp.ancestors(), gcp.bindings(), gcp.from_node(), gcp.to_node_id())
        node = Node(gcp.asset_type(), gcp.id_resource())
        listt = []
        if node.id_resource == user_input:
            for user in edge.bindings['bindings']:
                listt.append([member_splitter(user['members']), role_splitter(user['role'])])
        if not listt:
            continue
        else:
            print(listt)


def main():

    for i in json:
        gcp = GCP(i)
        graph = Graph(gcp.get_nodes(), gcp.get_edges())
    user_input = input('user:')
    user_premission(user_input)

    user_input_second = input('unique:')
    second_task(user_input_second)

    user_input_third = input('user:')
    third_task(user_input_third)

    user_input_fourth = input('id:')
    fourth_task(user_input_fourth)


if __name__ == '__main__':
    main()
