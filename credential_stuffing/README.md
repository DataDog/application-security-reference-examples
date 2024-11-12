# Credential Stuffing

This application contians a login site that is vulnerable to credential stuffing. It will set up users, start logging in authorized users to establish a baseline of requests, and then launch a credential stuffing attack.

For this attack, https://github.com/vanhauser-thc/thc-hydra is used.

## Disclaimers
The credentials used in credentials.txt are either common username/password combos or completely made up. None of these credentials are from dataleaks.

## How To Run
1. Follow the ASM Referernce Examples README to ensure datadog is connected and the app is running.

2. Run the Attack
   
Ensure you are in the root of the project directory. 
```
docker compose --file docker-compose.credential-stuffer.yaml up --build
```
When done testing, don't forget to stop the container. 

## Interpreting Results

### Inspect the traces: 
- https://app.datadoghq.com/security/appsec/traces
These traces are what the signal uses to find trends and alert on behaviors. It can be interesting to look at the top users and the top security activities in the graphs at the top. This will only be showing traces related to security activity to help narrow focus. 

### Look at the signals:
After reviewing the traces above, click on "Signals" in the top tab. Signals are created when Datadog detects a threat based on a detection rule. These may take a short time to populate, but will usually alert within 5 - 10 minutes on the traces occuring. By running the credential stuffing attack above, you should see a critical severity signal titled "Account compromised by credential stuffing attack." Click on it and start exploring the information provided, including compromised users, attacking ips, and targeted users. From there you are able to explore different next steps to respond or protect by blocking certain behaviors or ips. 

## Next Steps
- https://app.datadoghq.com/security/appsec/protection
Now that you have seen a successfull attack, you can test different ways to block the attacks within Datadog. If you implement a blocking method, run the credential stuffing attack again and you should see that the attack was blocked. 

### Use the Denylist
- https://app.datadoghq.com/security/appsec/denylist
When looking at the signal from the previous step, there are options to block compromised users or attacking ips. Here is where you can find more information on those attackers and block additional attackers.

## Datadog Resources
- https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=loginfailure&code-lang=python#adding-authenticated-user-information-to-traces-and-enabling-user-blocking-capability

