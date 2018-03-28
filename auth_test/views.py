from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
# Create your views here.


@permission_required('dashdoard.view_server', login_url="/success")
def manager(request):
    return render(request, 'manager.html', {})


def general(request):
    return render(request, 'general.html', {})
