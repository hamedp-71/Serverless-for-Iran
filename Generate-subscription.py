import json
import os
from jsmin import jsmin

all_configs = ["Serverless.jsonc", "Serverless-local.jsonc", "Serverless-dynx.jsonc"]
output_path = os.path.join('Subscription', 'Serverless-for-Iran.json')

all_c = []
for config in all_configs:
    with open(config) as js_file:
        minified = jsmin(js_file.read())
    all_c.append(json.loads(minified))
json.dump(all_c, open(output_path, "w"), indent=4)
print("done")
