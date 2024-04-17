Example request:

```
$ pip install -r requirements.txt
$ python api.py
$ curl -H "Content-Type: application/json" http://127.0.0.1:5000/summary --data '
{
    "query": "Summarize a vehicle insurance chat with a user who has reconnected so chatgpt can use it to continue the conversation. The chat should be concise, containing all essential information and not exceeding more than 30 percent or the original characters, this is key to make this a cost viable solution. Key details include the user’s name, phone number, vehicle type (motorcycle or car), vehicle brand and model (if available), and the vehicle’s year. Also, remember any objections or questions raised by the user, as well as an assessment of their interest in purchasing insurance. The prompt should be structured as a list of key points, with a narrative summary at the end to capture additional unforeseen information. Additional Guidelines: The user’s interest can be gauged by the number of questions they ask about the product, their stated need for insurance now or in the near future, or their expressed opinions about insurance. Lack of interest may be indicated by statements such as already having insurance, not caring about insurance, or negative views on insurance. Recall previous information given about the user’s needs or interest in the product, as well as personal information the agent has requested to craft a sales pitch. The final narrative should look for facts the user has given about themselves or their property,  and try to extract what aspects of the insurance are motivating them to move forward and what objections need to be addressed before they are ready to buy. Use as few unnecessary characters as possible.",
    "context": "Hola buenos dias. Si, me parece bien. Me llamo Ariel. tengo una moto yamaha del 2011. Es para moverme por el barrio. no sé cuál más cuál es el más importante. Contra todos los riesgos es importante. que adquirir. ¿Qué pasó? si me interesa No, muchas gracias.",
    "temperature": 0.3
}' -v

Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000
> POST /summary HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.4.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 1879
>


< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.12.3
< Date: Wed, 17 Apr 2024 20:57:19 GMT
< Content-Type: application/json
< Content-Length: 2831
< Connection: close
<
{
    "llm_response": "\u2022Name: Ariel\r\n\u2022Phone number: 212-555-1234\r\n\u2022Vehicle type: Motorcycle\r\n\u2022Vehicle brand: Yamaha\r\n\u2022Year: 2011\r\n\u2022Motorcycle model: 2011 Yamaha\r\n\u2022Interest: I have a motorcycle and am looking for insurance.",
    "prompt": "Summarize a vehicle insurance chat with a user who has reconnected so chatgpt can use it to continue the conversation. The chat should be concise, containing all essential information and not exceeding more than 30 percent or the original characters, this is key to make this a cost viable solution. Key details include the user\u2019s name, phone number, vehicle type (motorcycle or car), vehicle brand and model (if available), and the vehicle\u2019s year. Also, remember any objections or questions raised by the user, as well as an assessment of their interest in purchasing insurance. The prompt should be structured as a list of key points, with a narrative summary at the end to capture additional unforeseen information. Additional Guidelines: The user\u2019s interest can be gauged by the number of questions they ask about the product, their stated need for insurance now or in the near future, or their expressed opinions about insurance. Lack of interest may be indicated by statements such as already having insurance, not caring about insurance, or negative views on insurance. Recall previous information given about the user\u2019s needs or interest in the product, as well as personal information the agent has requested to craft a sales pitch. The final narrative should look for facts the user has given about themselves or their property,  and try to extract what aspects of the insurance are motivating them to move forward and what objections need to be addressed before they are ready to buy. Use as few unnecessary characters as possible.",
    "evidence": "Hola buenos dias. Si, me parece bien. Me llamo Ariel. tengo una moto yamaha del 2011. Es para moverme por el barrio. no s\u00e9 cu\u00e1l m\u00e1s cu\u00e1l es el m\u00e1s importante. Contra todos los riesgos es importante. que adquirir. \u00bfQu\u00e9 pas\u00f3? si me interesa No, muchas gracias.",
    "instruction": "default_with_context",
    "model": "llmware/bling-tiny-llama-v0",
    "usage": {
        "input": 428,
        "output": 89,
        "total": 517,
        "metric": "tokens",
        "processing_time": 38.392902851104736
    },
    "time_stamp": "Wed Apr 17 17:57:19 2024",
    "calling_app_ID": "",
    "rating": "",
    "account_name": "llmware",
    "prompt_id": 0,
    "batch_id": 0,
    "evidence_metadata": [
        {
            "evidence_start_char": 0,
            "evidence_stop_char": 258,
            "page_num": "NA",
            "source_name": "NA",
            "doc_id": "NA",
            "block_id": "NA"
        }
    ]
}
```
