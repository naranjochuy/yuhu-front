from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from utils.yuhu import Yuhu
from .forms import InputForm


def list(request):
    query_params = request.GET.dict()
    page = int(query_params.get("page", "1"))
    yuhu = Yuhu()
    response = yuhu.get_tasks(page)
    status_code = response.get("status_code")
    if status_code == 200:
        data = response.get("data")
        count = data.get("count")
        pages = data.get("total_pages") + 1
        total_pages = [i for i in range(1, pages)]
        msg = f"Showing {page * 2 - 1 } to {page * 2 } of {count} result."
        data.update({"total_pages": total_pages})
        return render(request, "list.html", {"data": data, "msg": msg})
    else:
        error_msg = response.get("error_msg")
        return render(request, "list.html", {"error_msg": error_msg})


def create(request):
    if request.method == "GET":
        return render(
            request,
            "form.html",
            {"form": InputForm(), "action": "Create"}
        )
    elif request.method == "POST":
        yuhu = Yuhu()
        data = request.POST.dict()
        form = InputForm(data)
        if form.is_valid():
            response = yuhu.create_task(data)
            return HttpResponseRedirect(reverse("list"))
        else:
            return render(
                request,
                "form.html",
                {"form": form, "action": "Create"}
            )


def update(request, id):
    yuhu = Yuhu()
    if request.method == "GET":
        response = yuhu.get_task(id)
        status_code = response.get("status_code")
        if status_code == 200:
            task = response.get("data")
            return render(
                request,
                "form.html",
                {"form": InputForm(task), "action": "Update"}
            )
        else:
            error_msg = response.get("error_msg")
            return render(request, "form.html", {"error_msg": error_msg})
    elif request.method == "POST":
        data = request.POST.dict()
        form = InputForm(data)
        if form.is_valid():
            yuhu.update_task(data, id)
            return HttpResponseRedirect(reverse("list"))
        else:
            return render(
                request,
                "form.html",
                {"form": form, "action": "Update"}
            )


def delete(request, id):
    if request.method == "GET":
        context = {}
        yuhu = Yuhu()
        response = yuhu.get_task(id)
        status_code = response.get("status_code")
        if status_code == 200:
            context.update({"task": response.get("data")})
        else:
            context.update({"error_msg": response.get("error_msg")})
        return render(request, "item.html", context)
    elif request.method == "POST":
        yuhu = Yuhu()
        response = yuhu.delete_task(id)
        print("delete response:", response)
        return HttpResponseRedirect(reverse("list"))
