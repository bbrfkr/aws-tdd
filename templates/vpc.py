#!/usr/bin/python
# -*- coding: utf-8 -*-

from troposphere import Output
from troposphere import Parameter, Ref, Tags, Template
from troposphere.ec2 import VPC

t = Template()

t.set_version('2010-09-09')

ref_stack_id = Ref('AWS::StackId')

cidr_block = t.add_parameter(Parameter(
    "CidrBlock",
    Type="String"
))

vpc = t.add_resource(
    VPC(
        'Vpc',
        CidrBlock=Ref(cidr_block),
        Tags=Tags(
            Application=ref_stack_id)))

t.add_output(
    [
        Output('vpcid', Description='Newly created vpc id', Value=Ref(vpc))
    ]
)

template_str = t.to_json()
print(template_str)

def sceptre_handler(sceptre_user_data):
    return template_str
