#!/usr/bin/python3
import os
from bitbucket_pipes_toolkit import Pipe, get_logger
import yaml

logger = get_logger()
pipe = Pipe(pipe_metadata_file="/src/config.yaml")

command_name = pipe.get_variable("COMMAND_NAME")
target = pipe.get_variable("TARGET")

print("########### 1", command_name)
print("########### 2", target)
if command_name == "version":
    command_schema = yaml.safe_load(stream)
    command = command_schema["command_prefix"]
    print("########### 3", command)
    exit_code = os.system(command + "--version")
    if exit_code:
        pipe.fail("command exited unsuccessfully", True)
    pipe.success("Succesfully executed")

with open(os.path.join("/src/","plugins", command_name + ".yaml"), "r") as stream:
    try:
        command_schema = yaml.safe_load(stream)
        command = command_schema["command_prefix"]
        print("########### 4", command, command_schema)
        if  target is not None and target != "":
            command = command + " " + target
            print("########### 5", command)

        for var in pipe.variables:
            if var == "COMMAND_NAME" or var == "TARGET":
                continue
            if var in command_schema["variable_mapping"]:
                value = pipe.get_variable(var)
                command = command + " " + command_schema["variable_mapping"][var] + "=" + "\"" + str(pipe.get_variable(var)) + "\""
                print("########### 6", command)
           

        logger.info("> echo $(cd " + os.getenv('BITBUCKET_WORKSPACE') + " && " + command + " )")
        if os.getenv('BITBUCKET_WORKSPACE') != None:
            exit_code = os.system("echo $(cd " + os.getenv('BITBUCKET_WORKSPACE') + "/.. && " + command + " )")
        else:
            exit_code = os.system("echo $(" + command + ")")
        
        if exit_code:
            pipe.fail("command exited unsuccessfully", True)
        pipe.success("Succesfully executed")
    except yaml.YAMLError as exc:
        print(exc)
