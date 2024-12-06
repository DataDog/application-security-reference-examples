# ASM Reference Examples
The projects in this repo are meant to be easily run to see how Datadog signals different attacks. We aim to continue adding to this repository and the list below are the attacks that can be run today. 

- [Credential Stuffing](credential_stuffing/README.md)
- [SSRF](ssrf/README.md)

## Disclaimers
This repository contains deliberately insecure web application. Do not deploy it in any production environment.


### How To Run
1. export your Datadog API key 
```
export DD_API_KEY="<api-key>"
```
2. Clone this repo
```
git clone https://github.com//DataDog/application-security-reference-examples
```
3. Run an attack.
   
Credential Stuffer:
```
docker compose --file docker-compose.credential-stuffer.yaml up --build
```
SSRF Attack:
```
docker compose --file docker-compose.ssrf.yaml up --build
```
4. Head to datadog, watch results populate in the Application Security tab. This may take a few minutes as things populate. More information on what to look for will be included in the README in the attack folder.



## Datadog Resources
- https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/python/
