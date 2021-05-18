import logging
from nomnomdata.engine import Engine, Parameter, ParameterGroup
from nomnomdata.engine.parameters import Int, String

logger = logging.getLogger("engine.hello_world")
engine = Engine(
    uuid="ALEXANDERCASIAS",
    alias="Hello World Sample",
    description="Demonstrates basic app structure and functionality.",
    categories=["general"],
)
@engine.action(
    display_name="Send by API",
    description="Prints a greeting multiple times in the Task execution log.",            
)
@engine.parameter_group(
    name="general_parameters",
    display_name="General Parameters",
    description="Parameters for Hello World",
    parameter_group=ParameterGroup(
        Parameter(
            type=Int(),
            name="repeat",
            display_name="Repeat",
            description="Specify how many times to print.",
            default=1,
            required=True,
        ),
        Parameter(
            type=String(),
            name="User",
            display_name="User",
            description="Specify a name to print instead of World.",
            required=False,
        ),
        Parameter(
            type=String(),
            name="Password",
            display_name="Password",
            description="Specify a name to print instead of World.",
            required=False,
        ),
        Parameter(
            type=String(),
            name="Url_Api",
            display_name="Url Api",
            description="Specify a name to print instead of World.",
            required=False,
        ),
    ),
)
def hello_world(parameters):
    i = 0
    x = f"Hello {parameters.get('name') or 'World'}"
    while i < parameters["repeat"]:
        logger.info(x)
        i += 1
    return i, x

@engine.action(
    display_name="Send by IMAP",
    description="Prints a greeting multiple times in the Task execution log.",        
)
@engine.parameter_group(
    name="general_parameters_IMAP",
    display_name="General Parameters IMAP",
    description="Parameters for IMAP",
    parameter_group=ParameterGroup(
        Parameter(
            type=Int(),
            name="repeat",
            display_name="Repeat",
            description="Specify how many times to print.",
            default=1,
            required=True,
        ),
        Parameter(
            type=String(),
            name="User",
            display_name="User",
            description="Specify a name to print instead of World.",
            required=False,
        ),
        Parameter(
            type=String(),
            name="Password",
            display_name="Password",
            description="Specify a name to print instead of World.",
            required=False,
        ),
        Parameter(
            type=String(),
            name="Url",
            display_name="Url",
            description="Specify a name to print instead of World.",
            required=False,
        ),
    ),
)
def hello_world2(parameters):
    i = 0
    x = f"Hello {parameters.get('name') or 'World'}"
    while i < parameters["repeat"]:
        logger.info(x)
        i += 1
    return i, x

@engine.action(
    display_name="Send by POP3",
    description="Prints a greeting multiple times in the Task execution log.",        
)
@engine.parameter_group(
    name="general_parameters_POP3",
    display_name="General Parameters POP3",
    description="Parameters for POP3",
    parameter_group=ParameterGroup(
        Parameter(
            type=Int(),
            name="repeat",
            display_name="Repeat",
            description="Specify how many times to print.",
            default=1,
            required=True,
        ),
        Parameter(
            type=String(),
            name="User",
            display_name="User",
            description="Specify a name to print instead of World.",
            required=False,
        ),
        Parameter(
            type=String(),
            name="Password",
            display_name="Password",
            description="Specify a name to print instead of World.",
            required=False,
        ),
        Parameter(
            type=String(),
            name="Url",
            display_name="Url",
            description="Specify a name to print instead of World.",
            required=False,
        ),
    ),
)
def hello_world3(parameters):
    i = 0
    x = f"Hello {parameters.get('name') or 'World'}"
    while i < parameters["repeat"]:
        logger.info(x)
        i += 1
    return i, x