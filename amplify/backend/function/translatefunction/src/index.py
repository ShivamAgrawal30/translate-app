from flask import Flask, render_template, request, url_for, jsonify
app = Flask(__name__)
import requests
from flask_cors import CORS
import awsgi

CORS(app)

@app.route('/translate', methods=['GET', 'POST'])
def my_test_endpoint():
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)

    
    if request.method == 'POST':
        src_lang = request.json['srcLanguage']
        print(src_lang)
        dest_lang = request.json['destLanguage']
        content = request.json['inputString']

        # content=base64.b64decode(content).decode('utf_8_sig') #TO-DO



        API_URL = f"https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-{src_lang}-{dest_lang}"
        API_TOKEN='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'
        headers = {"Authorization": f"Bearer {API_TOKEN}", "Access-Control-Allow-Origin": "*", 
                        "Access-Control-Allow-Methods": "*",
                        "Access-Control-Allow-Headers": "*",}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            #sleep(20) # NEED TO DISCUSS
            return response.json()
            
        output = query({
            # "inputs": "Hello, My name is Shivam. What is yours? I live in Frankfurt. I am pursuing my masters in Data Science",
            "inputs": f"{content}"
        })
    print(output[0])
    return output[0]

def handler(event, context):
  print('received event:')
  print(event)

  return awsgi.response(app, event, context)