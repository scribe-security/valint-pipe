#!/usr/bin/python3
import os
from bitbucket_pipes_toolkit import Pipe, get_logger
import yaml

logger = get_logger()
pipe = Pipe(pipe_metadata_file="./config.yaml")

command_name = pipe.get_variable("COMMAND_NAME")

with open(os.path.join("./","plugins", command_name + ".yaml"), "r") as stream:
    try:
        command_schema = yaml.safe_load(stream)
        command = command_schema["command_prefix"]
        for var in pipe.variables:
            if var == "COMMAND_NAME":
                continue
            if var in command_schema["variable_mapping"]:
                value = pipe.get_variable(var)
                command = command + " " + command_schema["variable_mapping"][var] + "=" + "\"" + str(pipe.get_variable(var)) + "\""
        logger.info("> echo $(cd " + os.getenv('BITBUCKET_WORKSPACE') + " && " + command + " )")
        exit_code = os.system("echo $(cd " + os.getenv('BITBUCKET_WORKSPACE') + "/.. && " + command + " )")
        if exit_code:
            pipe.fail("command exited unsuccessfully", True)
        pipe.success("Succesfully executed")
    except yaml.YAMLError as exc:
        print(exc)
