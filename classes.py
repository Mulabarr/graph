from pprint import pprint
from dataclasses import dataclass
from typing import List


class Node:
    def __init__(self, asset_type, id_resource):
        self.asset_type = asset_type
        self.id_resource = id_resource


class Edge:
    def __init__(self, ancestors, bindings, from_node, to_node_id):
        self.ancestors = ancestors
        self.bindings = bindings
        self.from_node = from_node
        self.to_node_id = to_node_id


class GCP:
    def role_splitter(self, a):
        role = a.split('/')[-1]
        return role

    def __init__(self, json):
        self.json = json

    def asset_type(self):
        asset_type = self.json['asset_type'].split('/')[-1]
        return asset_type

    def id_resource(self):
        id_resource = self.json['name'].split('/')[-1]
        return id_resource

    def ancestors(self):
        ancestors_dict = {'ancestors': []}
        ancestors = self.json['ancestors']
        ancestors_dict['ancestors'] = ancestors
        return ancestors_dict

    def bindings(self):
        bindings_dict = {'bindings': []}
        role_and_member = self.json["iam_policy"]["bindings"]
        for i in role_and_member:
            role = GCP.role_splitter(self, i['role'])
            members = []
            for j in i['members']:
                members.append(j)
            bindings_dict['bindings'].append({'role': role, 'members': members})
        return bindings_dict

    def from_node(self):
        node = GCP(self.json)
        node_id = node.id_resource()
        from_node_dict = {'from_node_id': node_id}
        return from_node_dict

    def to_node_id(self):
        ancestors_dict = {'to_node_id': []}
        ancestors = self.json['ancestors']
        ancestors_dict['to_node_id'] = ancestors
        return ancestors_dict

    def get_edges(self):
        edges = []
        edges.append(GCP.ancestors(self))
        edges.append(GCP.bindings(self))
        edges.append(GCP.from_node(self))
        edges.append(GCP.to_node_id(self))
        return edges

    def get_nodes(self):
        nodes = []
        nodes.append(GCP.asset_type(self))
        nodes.append(GCP.id_resource(self))
        return nodes

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges



