# ASM Reference Examples

## Disclaimers
This repository contains deliberately insecure web application. Do not deploy it in any production environment.


## Credential Stuffing

This application contians a login site that is vulnerable to credential stuffing. It will set up users, start logging in authorized users to establish a baseline of requests, and then launch a credential stuffing attack.

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

3. Build and run the necessary containers

```
docker compose up 
```

4. run the credential stuffing tool 
```

```

5. Head to datadog, watch results populate in the Application Security tab. This may take a few minutes as things populate.

6. Optional: Configure the In-App WAF to block credential stuffing attepts by using an existing policy or creating a custom rule.


## Datadog Resources Referenced
1. https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=loginfailure&code-lang=python#adding-authenticated-user-information-to-traces-and-enabling-user-blocking-capability

2. https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/python/

3. https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/
