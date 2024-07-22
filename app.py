import json

from collections import OrderedDict
from flask import Flask, Response

from api.berries import get_berries
from processing import compute_values_info


app = Flask(__name__)

@app.route('/allBerryStats')
async def all_berry_stats():
    berries = await get_berries()

    berries_names = [b.name for b in berries]
    berries_growth_time = [b.growth_time for b in berries]

    computed_data = compute_values_info(berries_growth_time)

    # we manually serialize to json, because by letting flask
    # do the serialization using its functions, the order of the
    # keys in the dictionary won't be preserved

    serialized_data = json.dumps(OrderedDict([
        ('berries_names', berries_names),
        ('min_growth_time', computed_data.min),
        ('median_growth_time', computed_data.median),
        ('max_growth_time', computed_data.max),
        ('variance_growth_time', computed_data.variance),
        ('mean_growth_time', computed_data.mean),
        ('frequency_growth_time', computed_data.frequency)
    ]))

    # also, because now to flask it seems that we're responding with
    # a string, we need to manually add the content type
    return Response(serialized_data, headers={'Content-Type': 'application/json'})
