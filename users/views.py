from django.http import HttpResponse


def user_list(request):
    return HttpResponse("User list")


def user_detail(request, pk):
    return HttpResponse(f"User detail {pk}")


def user_create(request):
    return HttpResponse("User create")


def user_update(request, pk):
    return HttpResponse(f"User update {pk}")


def user_delete(request, pk):
    return HttpResponse(f"User delete {pk}")
