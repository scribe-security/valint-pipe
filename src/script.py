#!/usr/bin/python3
import os
from bitbucket_pipes_toolkit import Pipe
import yaml


pipe = Pipe(pipe_metadata_file="./config.yaml")

command_name = pipe.get_variable("command_name")

with open(os.path.join("./","plugins", command_name + ".yaml"), "r") as stream:
    try:
        command_schema = yaml.safe_load(stream)
        command = command_schema["command_prefix"]
        for var in pipe.variables:
            if var == "command_name":
                continue
            if var in command_schema["variable_mapping"]:
                value = pipe.get_variable(var)
                command = command + " " + command_schema["variable_mapping"][var] + "=" + "\"" + str(pipe.get_variable(var)) + "\""
        print("Executing:", command)
        exit_code = os.system(command)
        if exit_code:
            pipe.fail("command exited unsuccessfully", True)
        pipe.success("Succesfully executed")
    except yaml.YAMLError as exc:
        print(exc)
