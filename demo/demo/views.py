
from prometheus_client import Counter
from django.http import HttpResponse
from django.template import loader

# Counter metriği oluşturma
index_requests_total = Counter('index_requests_total', 'Total number of index requests')

def index(request):
    # Counter metriğini artırma
    index_requests_total.inc()

    template = loader.get_template('demo/index.html')

    return HttpResponse(template.render())


