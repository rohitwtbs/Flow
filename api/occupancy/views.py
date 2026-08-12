import random
import time
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_fake_occupancy(request):
    """
    Returns fake random occupancy data on query.
    """
    occupancy_values = [0, 1, 2]
    fake_data = random.choice(occupancy_values)
    sensor_id = request.query_params.get('sensor_id', 'sensor_1')
    
    payload = {
        "data": fake_data,
        "timestamp": time.time(),
        "sensor_id": sensor_id
    }
    return Response(payload)
