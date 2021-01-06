adict = {'name':'zs'}

import json

ajson = json.dumps(adict)
print(ajson,type(ajson))

bdict = json.loads(ajson)
print(bdict,type(bdict))