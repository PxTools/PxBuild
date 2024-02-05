import yaml

def process_properties(properties, required_fields=[], depth=0):
    """Recursively process properties to generate Markdown content."""
    md_content = ""
    indent = "    " * depth  # Indentation for nested properties

    for property_name, property_details in properties.items():

        # Append an asterisk if the field is required
        property_name_display = property_name + "*" if property_name in required_fields else property_name
        property_type = property_details.get('type', 'N/A')
        description = property_details.get('description', 'No description available.')

        md_content += f"{indent}- **{property_name_display}**: {property_type},  Description: {description}\n"
        if 'additionalProperties' in property_details:
            # Handle dictionary-like structure for additionalProperties
            additional_props = property_details['additionalProperties']
            value_type = additional_props.get('type', 'any')
            maxLength = additional_props.get('maxLength', 'N/A')
            md_content += f"{indent}  - This is a dictionary with keys of type string and values of type {value_type}.\n"
            if maxLength != 'N/A':
                md_content += f"{indent}    - Value max length: {maxLength}\n"
        elif property_type == 'object':
            # Recursively process nested object properties
            nested_properties = property_details.get('properties', {})
            nested_required = property_details.get('required', [])
            md_content += process_properties(nested_properties, nested_required, depth + 1)
        else:
            
            description = property_details.get('description', 'No description available.')
            md_content += f"{indent}  - Description: {description}\n"

    return md_content

def process_properties2(node_name:str, node_values:dict, required:bool, depth=0) -> str:
    my_out:str=""

    indent = "    " * (depth -1) if depth > 0 else "" 
    my_desc = f" Description: {node_values['description']}" if 'description' in node_values else ""
    my_default = f" default: {node_values['default']}" if 'default' in node_values else ""
    my_type = f" type: {node_values['type']}" if 'type' in node_values and not node_values['type'] == 'object' else " ND"
    my_max_length = f" ,max length: {node_values['maxLength']}" if 'maxLength' in node_values else ""

    if "$ref" in node_values:
        my_type = f" type:  ["+node_values["$ref"].split("/")[-1]+ "](#"+ node_values["$ref"].split("/")[-1].lower()+")"

    node_name_display = node_name + "(*)" if required else node_name
    if depth == 0:
        my_out += f"# {node_name_display}\n\n"
        my_out += f"{my_desc}\n\n"
    else:
        my_out += f"{indent} - {node_name_display}{my_type}{my_default}{my_max_length}\n\n"
        if my_desc:
            my_out += f"{indent}   {my_desc}\n\n"

    if "$ref" in node_values:
        pass#my_out += f"{indent}    is a ["+node_values["$ref"].split("/")[-1]+ "](#"+ node_values["$ref"].split("/")[-1].lower()+")\n"
    elif node_values["type"] == "object":
        if "properties" in node_values:
           for key, value in node_values["properties"].items():
               my_req = False
               if "required"in node_values and key in node_values["required"]:
                   my_req = True
               my_out += process_properties2(key,value, my_req , depth +1 )

        # Needed:? if 'additionalProperties' in property_details:
               
    elif node_values["type"] == "array":
        temp = node_values["items"]
        my_out += process_properties2("items", temp, False , depth +1 )
    
    
    
        

        
            
    return my_out


def yaml_to_markdown(yaml_file, output_dir):
    with open(yaml_file, 'r', encoding="utf-8") as file:
        data = yaml.safe_load(file)

    components = data["components"]
    schema = components["schemas"]
    is_first:bool = True
    md_content=""
    filename=""
    for key, value in schema.items():
        if is_first:
            filename= f"{output_dir}/{key}.md"
            is_first = False

        md_content += process_properties2(key, value, False)


    with open( filename, 'w') as md_file:
        md_file.write(md_content)

    print("Wrote to file: " + filename)





yaml_to_markdown('jsonformats/openapiyaml/pxbuildconfig.yaml', './docs/input')
yaml_to_markdown('jsonformats/openapiyaml/pxcodes.yaml', './docs/input')
yaml_to_markdown('jsonformats/openapiyaml/pxmetadata.yaml', './docs/input')
yaml_to_markdown('jsonformats/openapiyaml/pxstatistics.yaml', './docs/input')