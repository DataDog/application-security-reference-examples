# ASM Reference Examples
The projects in this repo are meant to be easily run to see how Datadog signals different attacks. We aim to continue adding to this repository and the list below are the attacks that can be run today. 

- [Credential Stuffing](credential_stuffing/README.md)

## Disclaimers
This repository contains deliberately insecure web application. Do not deploy it in any production environment.


### How To Run

1. Install the datadog agent on your machine.
Reference: https://docs.datadoghq.com/getting_started/agent/#installation
```
DD_API_KEY=<DATADOG_API_KEY> DD_SITE="datadoghq.com" bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"
```
2. export your Datadog API key 
```
export DD_API_KEY="<api-key>"
```
4. Clone this repo
```
git clone https://github.com//DataDog/application-security-reference-examples
```
4. Run an attack.
   
Credential Stuffer:
```
docker compose --file docker-compose.credential-stuffer.yaml up --build
```

5. Head to datadog, watch results populate in the Application Security tab. This may take a few minutes as things populate. More information on what to look for will be included in the README in the attack folder.



## Datadog Resources
- https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/python/
