import json
import os
import json5

all_configs = ["Serverless.jsonc", "Serverless-dynx.jsonc", "Serverless-shatel.jsonc", "Serverless-vanilla.jsonc", "Serverless-zeus.jsonc"]
output_path = os.path.join('Subscription', 'Serverless-for-Iran.json')

all_j = []
for config in all_configs:
    with open(config) as config_file:
        all_j.append(json5.load(config_file))

json.dump(all_j, open(output_path, "w"), indent=4)
print("done")
