import json
import os
import json5
from jsmin import jsmin

all_configs = ["Serverless.jsonc", "Serverless-local.jsonc", "Serverless-dynx.jsonc"]
output_path = os.path.join('Subscription', 'Serverless-for-Iran.json')

all_json5 = []
all_jsmin = []
for config in all_configs:
    with open(config) as config_file:
        all_json5.append(json5.load(config_file))
        config_file.seek(0)
        all_jsmin.append(json.loads(jsmin(config_file.read())))

if all_json5 != all_jsmin:
    print("error")

else:
    json.dump(all_json5, open(output_path, "w"), indent=4)
    print("done")
