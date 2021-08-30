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

    def bindings(self):
        bindings_dict = []
        role_and_member = self.json["iam_policy"]["bindings"]
        for i in role_and_member:
            role = GCP.role_splitter(self, i['role'])
            members = []
            for j in i['members']:
                members.append(j)
            bindings_dict.append({'role': role, 'members': members})
        return bindings_dict

    def from_node(self):
        node = GCP(self.json)
        node_id = node.id_resource()
        return node_id

    def to_node_id(self):
        ancestors = self.json['ancestors']
        return ancestors

    def get_edges(self):
        edges = {}
        edges['bindings'] = GCP.bindings(self)
        edges['from_node'] = GCP.from_node(self)
        edges['to_node_id'] = GCP.to_node_id(self)
        return edges

    def get_nodes(self):
        nodes = {}
        nodes['type'] = (GCP.asset_type(self))
        nodes['id'] = (GCP.id_resource(self))
        return nodes

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges



