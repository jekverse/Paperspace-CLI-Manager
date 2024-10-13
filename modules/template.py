# TEMPLATE 

def default():
    machine_type = "Free-A4000"
    container = "paperspace/gradient-base:pt211-tf215-cudatk120-py311-20240202"
    name = "default"
    command = "PIP_DISABLE_PIP_VERSION_CHECK=1 jupyter lab --allow-root --ip=0.0.0.0 --no-browser --ServerApp.trust_xheaders=True --ServerApp.disable_check_xsrf=False --ServerApp.allow_remote_access=True --ServerApp.allow_origin='*' --ServerApp.allow_credentials=True"
    return machine_type, container, name, command

def comfyui():
    machine_type = "Free-A4000"
    container = "jekverse/paperspace-based:v1"
    shutdown_timeout="6" 
    name = "comfyui"
    command = "PIP_DISABLE_PIP_VERSION_CHECK=1 jupyter lab --allow-root --ip=0.0.0.0 --no-browser --ServerApp.trust_xheaders=True --ServerApp.disable_check_xsrf=False --ServerApp.allow_remote_access=True --ServerApp.allow_origin='*' --ServerApp.allow_credentials=True"
    return machine_type, container , name, command, shutdown_timeout

def forge():
    machine_type = "Free-A4000"
    container = "paperspace/gradient-base:pt211-tf215-cudatk120-py311-20240202"
    name = "forge"
    command = "PIP_DISABLE_PIP_VERSION_CHECK=1 jupyter lab --allow-root --ip=0.0.0.0 --no-browser --ServerApp.trust_xheaders=True --ServerApp.disable_check_xsrf=False --ServerApp.allow_remote_access=True --ServerApp.allow_origin='*' --ServerApp.allow_credentials=True"
    return machine_type, container, name,command

def fooocus():
    machine_type = "Free-A4000"
    container = "jekverse/fooocus:v4"
    name = "fooocus"
    command = "PIP_DISABLE_PIP_VERSION_CHECK=1 jupyter lab --allow-root --ip=0.0.0.0 --no-browser --ServerApp.trust_xheaders=True --ServerApp.disable_check_xsrf=False --ServerApp.allow_remote_access=True --ServerApp.allow_origin='*' --ServerApp.allow_credentials=True & python /content/Fooocus/entry_with_update.py & cloudflared tunnel run fooocus"
    return machine_type, container, name, command