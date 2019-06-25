require 'awspec'
Awsecrets.load

def get_output(stack, key_name)
    for output in stack['outputs'] do 
        if output['output_key'] == key_name then
            return(output['output_value'])
        end
    end
end
