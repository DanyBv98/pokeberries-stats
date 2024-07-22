from collections import OrderedDict

from flask import Flask
from matplotlib.figure import Figure

from api.berries import get_berries
from processing import compute_values_info
from utils.response import figure_response, ordered_dict_response


app = Flask(__name__)

@app.route('/allBerryStats')
async def all_berry_stats():
    berries = await get_berries()

    berries_names = [b.name for b in berries]
    berries_growth_time = [b.growth_time for b in berries]

    computed_data = compute_values_info(berries_growth_time)

    return ordered_dict_response(OrderedDict([
        ('berries_names', berries_names),
        ('min_growth_time', computed_data.min),
        ('median_growth_time', computed_data.median),
        ('max_growth_time', computed_data.max),
        ('variance_growth_time', computed_data.variance),
        ('mean_growth_time', computed_data.mean),
        ('frequency_growth_time', computed_data.frequency)
    ]))

@app.route('/growthTimeHistogram')
async def growth_time_histogram():
    berries = await get_berries()
    berries_growth_time = [b.growth_time for b in berries]

    figure = Figure()

    ax = figure.subplots()
    ax.hist(berries_growth_time, ec='white')
    ax.set_xlabel('Growth time')
    ax.set_ylabel('Berries count')

    return figure_response(figure)
