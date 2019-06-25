require 'spec_helper'
require 'yaml'

# load config
config = YAML.load_file('config/dev/vpc.yaml')
params = config['parameters']

cfn_cli = Aws::CloudFormation::Client.new()

# get vpc id
stack = cfn_cli.describe_stacks({stack_name: config['stack_name']})['stacks'][0]
vpc_id = get_output(stack, 'vpcid')

# tests from here!
describe vpc(vpc_id) do
  it { should exist }
  its(:cidr_block) { should eq params['CidrBlock'] }
end

