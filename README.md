# ASM Reference Examples
The projects in this repo are meant to be easily run to see how Datadog signals different attacks. We aim to continue adding to this repository and the list below are the attacks that can be run today. 

- [Credential Stuffing](credential_stuffing/README.md)
- [SSRF](ssrf/README.md)

## Disclaimers
This repository contains deliberately insecure web application. Do not deploy it in any production environment.

## Before Getting Started
You will need a Datadog API key in order to run any of the scripts. If you do not have an account, head to [Datadog](https://www.datadoghq.com/) and click "Get Started Free" or "Free Trial." Create a new API key [here](https://app.datadoghq.com/organization-settings/api-keys).

### How To Run
1. export your Datadog API key 
```
export DD_API_KEY="<api-key>"
```

2. (optional) If your Datadog site is not app.datadoghq.com (US1), export your correct site. If you are not sure what site you are on, check out the list [here](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site). The following example is for US5.

```
export DD_SITE="us5.datadoghq.com" 
```

3. Clone this repo
```
git clone https://github.com//DataDog/application-security-reference-examples
```
4. Run an attack.
   
```
docker compose --file docker-compose.[attack].yaml up --build
```
When done testing, don't forget to stop the container. 

| Attack | README | Command to run|
| ------ | ------ | ------ |
|Credential Stuffing | [README](credential_stuffing/README.md)| docker compose --file docker-compose.credential-stuffing.yaml up --build |
|SSRF | [README](ssrf/README.md)| docker compose --file docker-compose.ssrf.yaml up --build |


5. Head to datadog, watch results populate in the Application Security tab. This may take around 15 minutes as the website is spun up and results populate. More information on what to look for will be included in the README in the attack folder.



## Datadog Resources
- https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/python/