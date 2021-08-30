from pprint import pprint
from dataclasses import dataclass
from typing import List


class Node:
    def __init__(self, json):
        self.json = json

    def asset_type(self):
        asset_type = self.json['asset_type'].split('/')[-1]
        return asset_type

    def id_resource(self):
        id_resource = self.json['name'].split('/')[-1]
        return id_resource


class Edge:
    def role_splitter(self, a):
        role = a.split('/')[-1]
        return role

    def __init__(self, json):
        self.json = json

    def ancestors(self):
        ancestors_dict = {'ancestors': []}
        ancestors = self.json['ancestors']
        ancestors_dict['ancestors'] = ancestors
        return ancestors_dict

    def bindings(self):
        bindings_dict = {'bindings': []}
        role_and_member = self.json["iam_policy"]["bindings"]
        for i in role_and_member:
            role = Edge.role_splitter(self, i['role'])
            members = []
            for j in i['members']:
                members.append(j)
            bindings_dict['bindings'].append({'role': role, 'members': members})
        return bindings_dict


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges



