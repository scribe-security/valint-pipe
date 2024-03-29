#!/usr/bin/python3
import os
from bitbucket_pipes_toolkit import Pipe, get_logger
import yaml

logger = get_logger()
pipe = Pipe(pipe_metadata_file="/src/config.yaml")

command_name = pipe.get_variable("COMMAND_NAME")
target = pipe.get_variable("TARGET")

if command_name == "version":
    command_schema = yaml.safe_load(stream)
    command = command_schema["command_prefix"]
    exit_code = os.system(command + "--version")
    if exit_code:
        pipe.fail("command exited unsuccessfully", True)
    pipe.success("Succesfully executed")
    exit(0) 

with open(os.path.join("/src/","plugins", command_name + ".yaml"), "r") as stream:
    try:
        command_schema = yaml.safe_load(stream)
        command = command_schema["command_prefix"]
        if  target is not None and target != "":
            command = command + " " + target
        command = command + " " + "--context-type=bitbucket"
        for var in pipe.variables:
            if var == "COMMAND_NAME" or var == "TARGET":
                continue
            if var in command_schema["variable_mapping"]:
                value = pipe.get_variable(var)
                command = command + " " + command_schema["variable_mapping"][var] + "=" + "\"" + str(pipe.get_variable(var)) + "\""
        if os.getenv('BITBUCKET_WORKSPACE') != None:
           runCommand = "echo $(cd " + os.getenv('BITBUCKET_WORKSPACE') + "/.. && " + command + " )"
        else:
            runCommand = "echo $(" + command + ")"


        logger.info("> " + runCommand)
        exit_code = os.system(runCommand)
        if exit_code:
            pipe.fail("command exited unsuccessfully", True)
        pipe.success("Succesfully executed")
    except yaml.YAMLError as exc:
        print(exc)
