# Server Side Request Forgery (SSRF)
This application contians a blog page that is vulnerable to a SSRF attack. It will inject a payload into the add-blog site 

## Disclaimers
The credentials used to log in are fake credentials and should not be used outside of this.

## How To Run
1. Follow the ASM Referernce Examples README to ensure datadog is connected and the app is running.

2. Run the Attack
   
Ensure you are in the root of the project directory. 
```
docker compose --file docker-compose.ssrf.yaml up --build
```
When done testing, don't forget to stop the container. 

## Interpreting Results

### Inspect the traces: 
- https://app.datadoghq.com/security/appsec/traces
You should be able to see POST request to the test_picture_url endpoint that has a 'ssrf' warning. You are able to click on the trace to invistigate further.

## Next Steps
- https://app.datadoghq.com/security/appsec/protection
Now that you have seen a successfull attack, you can test different ways to block the attacks within Datadog. If you implement blocking, run the ssrf attack again and you should see that the attack was blocked. 



