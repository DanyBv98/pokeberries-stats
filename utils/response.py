from collections import OrderedDict
from io import BytesIO
import json

from flask import Response
from matplotlib.figure import Figure


def ordered_dict_response(data: OrderedDict) -> Response:
    # we manually serialize to json, because by letting flask
    # do the serialization using its functions, the order of the
    # keys in the dictionary won't be preserved
    serialized_data = json.dumps(data)

    # also, because now to flask it seems that we're responding with
    # a string, we need to manually add the content type
    return Response(serialized_data, mimetype='application/json')

def figure_response(figure: Figure) -> Response:
    buf = BytesIO()
    figure.savefig(buf, format='png')
    return Response(bytes(buf.getbuffer()), mimetype='image/png')
