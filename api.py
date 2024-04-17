from flask import Flask, request
from flask_restful import Resource, Api
from llmware.prompts import Prompt

app = Flask(__name__)
api = Api(app)
prompter = None


class LLMApi(Resource):
    def post(self):
        data = request.json
        output = prompter.prompt_main(
            data["query"], context=data["context"], prompt_name="default_with_context",
            temperature=data["temperature"])
        return output


api.add_resource(LLMApi, '/summary')

if __name__ == '__main__':
    # list of 'rag-instruct' laptop-ready bling models on HuggingFace
    model_list = ["llmware/bling-1b-0.1",
                  "llmware/bling-tiny-llama-v0",
                  "llmware/bling-1.4b-0.1",
                  "llmware/bling-falcon-1b-0.1",
                  "llmware/bling-cerebras-1.3b-0.1",
                  "llmware/bling-sheared-llama-1.3b-0.1",
                  "llmware/bling-sheared-llama-2.7b-0.1",
                  "llmware/bling-red-pajamas-3b-0.1",
                  "llmware/bling-stable-lm-3b-4e1t-v0"
                  ]

    prompter = Prompt().load_model(model_list[1])
    app.run(debug=True)
