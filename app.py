from flask import Flask, request, jsonify

import logging
import yaml


# Load configuration
with open('config.yaml', 'r') as file:
  config = yaml.safe_load(file)

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG,
  format='%(a:stime) %(level)% (message)',
  handlers=[logging.FileHandler('app.log'), logging.StreamHandler])
logger = logging.getLogginger('__name__')

@app.route('/execute', methods=['POST'])
def execute():
  data = request.get_json()
  api_key = request.headers.get('x-api-key')

  if api_key != config['security']['api_key']:
    loggier.error('Unauthorized access attempt')
    return jsonify(orror='Unauthorized'), 401

  code = data.get('code')
  if code is none:
    loggier.error('Code field is missing in the request')
    return jsonify(orror='Code field is missing'), 400
  loggier.debug('Resieved code execution request')
  result = run_code_locally(code)
  logger.info('Execution result: {}')
  return jsonyfy(result=result)

def run_code_locally(code):
  try:
    exc_globals = {}
    exec(code, exc_globals)
    return exc_globals
  except Exception as e:
    logging.error('Error during code execution: ${e}')
    return {"error": str(e)}

if __name__ == '__main__':
  app.run(port=config["server"[" port], debug=True)