from pprint import pprint

from classes import Node, Edge, Graph
json = {
        "name": "//cloudresourcemanager.googleapis.com/folders/188906894377",
        "asset_type": "cloudresourcemanager.googleapis.com/Folder",
        "iam_policy": {
            "etag": "BwWbYXSvzgs=",
            "bindings": [
                {
                    "role": "roles/owner",
                    "members": [
                        "serviceAccount:dev-manager@striking-arbor-264209.iam.gserviceaccount.com",
                        "serviceAccount:devops-dude-1@striking-arbor-264209.iam.gserviceaccount.com"
                    ]
                },
                {
                    "role": "roles/resourcemanager.folderAdmin",
                    "members": [
                        "user:ron@test.authomize.com"
                    ]
                },
                {
                    "role": "roles/resourcemanager.folderEditor",
                    "members": [
                        "user:ron@test.authomize.com"
                    ]
                }
            ]
        },
        "ancestors": [
            "folders/188906894377",
            "folders/767216091627",
            "organizations/1066060271767"
        ]
    }
nodes = []
edges = []
node = Node(json)
edge = Edge(json)


def role_splitter(a):
    role = a.split('/')[-1]
    return role


def member_splitter(a):
    for i in a:
        member = i.split(':')[-1]
        return member


def user_premission():
    user_input = input('user:')
    user_roles = []
    user_ancestors = ''
    for user in edge.bindings()['bindings']:
        if user_input in member_splitter(user['members']):
            user_roles.append(role_splitter(user['role']))
            user_ancestors = edge.to_node_id()['to_node_id']

    print(f'User have premissions:')
    for i in user_roles:
        print(i)
    print('In this ancestors:')
    for i in user_ancestors:
        print(i)



def second_task():
    user_input = input('unique:')
    if node.id_resource() == user_input:
        print(edge.ancestors())


def third_task():
    user_input = input('user:')
    listt = []
    for user in edge.bindings()['bindings']:
        if user_input == member_splitter(user['members']):
            listt.append([node.id_resource(), node.asset_type(), role_splitter(user['role'])])
    print(listt)


def fourth_task():
    user_input = input('id:')
    listt = []
    if node.id_resource() == user_input:
        for user in edge.bindings()['bindings']:
            listt.append([member_splitter(user['members']), role_splitter(user['role'])])
    print(listt)


def main():

    nodes.append({'type': node.asset_type(), 'id': node.id_resource()})

    edges.append(edge.ancestors())
    edges.append(edge.bindings())
    graph = Graph(nodes, edges)
    user_premission()
    second_task()
    third_task()
    fourth_task()

if __name__ == '__main__':
    main()