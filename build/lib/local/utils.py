import yaml

def read_yml_file(file_name: str):
    with open(file_name, "r") as stream:
        try:
            parameters = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise exc
    # assert parameters['username'] is not None
    # assert parameters['password'] is not None
    # assert len(parameters['positions']) > 0
    # assert len(parameters['locations']) > 0

    return parameters