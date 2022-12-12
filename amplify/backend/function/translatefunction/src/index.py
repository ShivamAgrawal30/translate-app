# import json

# # def handler(event, context):
# #   print('received event:')
# #   print(event)
  
# #   body = {
# #     "message": "Hello from your new Amplify Python lambda!"
# #   }
# #   return {
# #       'statusCode': 200,
# #       'headers': {
# #           'Access-Control-Allow-Headers': '*',
# #           'Access-Control-Allow-Origin': '*',
# #           'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
# #       },
# #       #'body': json.dumps("message": 'Hello from your new Amplify Python lambda!'),
# #       'body': json.dumps(body)
# #   }

# #handle a POST request
# # from flask import Flask, render_template, request, url_for, jsonify
# # app = Flask(__name__)
# import requests
# # from flask_cors import CORS
# # import base64
# #from time import sleep 

# #CORS(app)

# @app.route('/translate', methods=['GET', 'POST'])
# def handler(event, context):
#     if request.method == 'GET':
#         message = {'greeting':'Hello from Flask!'}
#         return jsonify(message)

#         # return render_template('index.html')
    
#     if request.method == 'POST':
#         # input_json = request.get_json(force=True) 
#         # force=True, above, is necessary if another developer 
#         # forgot to set the MIME type to 'application/json'
#         #print 'data from client:', input_json
#         #ictToReturn = {'answer':42}
#         #return jsonify(dictToReturn)
#         src_lang = request.json['srcLanguage']
#         print(src_lang)
#         dest_lang = request.json['destLanguage']
#         content = request.json['inputString']

#         # content=base64.b64decode(content).decode('utf_8_sig')



#         API_URL = f"https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-{src_lang}-{dest_lang}"
#         API_TOKEN='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'
#         headers = {"Authorization": f"Bearer {API_TOKEN}", "Access-Control-Allow-Origin": "*", 
#                         "Access-Control-Allow-Methods": "*",
#                         "Access-Control-Allow-Headers": "*",}

#         def query(payload):
#             response = requests.post(API_URL, headers=headers, json=payload)
#             #sleep(20)   
#             return response.json()
            
#         output = query({
#             # "inputs": "Hello, My name is Shivam. What is yours? I live in Frankfurt. I am pursuing my masters in Data Science",
#             "inputs": f"{content}"
#         })
#     print(output[0])
#     # return ''.join(output)
#     return output[0]

#     # return {
#     #     "statusCode": 200,
#     #     'headers': { "Access-Control-Allow-Origin": "*", 
#     #                  "Access-Control-Allow-Methods": "*",
#     #                  "Access-Control-Allow-Headers": "*", },
#     #     "body": output
#     # }

# # if __name__ == '__main__':
# #     app.run(debug=True)


from flask import Flask, render_template, request, url_for, jsonify
app = Flask(__name__)
import requests
from flask_cors import CORS
#import base64
import awsgi

#BASE_ROUTE="/translate"
CORS(app)

@app.route('/translate', methods=['GET', 'POST'])
def my_test_endpoint():
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)

        # return render_template('index.html')
    
    if request.method == 'POST':
        # input_json = request.get_json(force=True) 
        # force=True, above, is necessary if another developer 
        # forgot to set the MIME type to 'application/json'
        #print 'data from client:', input_json
        #ictToReturn = {'answer':42}
        #return jsonify(dictToReturn)
        src_lang = request.json['srcLanguage']
        print(src_lang)
        dest_lang = request.json['destLanguage']
        content = request.json['inputString']

        # content=base64.b64decode(content).decode('utf_8_sig')



        API_URL = f"https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-{src_lang}-{dest_lang}"
        API_TOKEN='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'
        headers = {"Authorization": f"Bearer {API_TOKEN}", "Access-Control-Allow-Origin": "*", 
                        "Access-Control-Allow-Methods": "*",
                        "Access-Control-Allow-Headers": "*",}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            #sleep(20)   
            return response.json()
            
        output = query({
            # "inputs": "Hello, My name is Shivam. What is yours? I live in Frankfurt. I am pursuing my masters in Data Science",
            "inputs": f"{content}"
        })
    print(output[0])
    # return ''.join(output)
    return output[0]

def handler(event, context):
  print('received event:')
  print(event)

  return awsgi.response(app, event, context)