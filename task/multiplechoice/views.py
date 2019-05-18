from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def add_track_question(request):
    print(settings.STATIC_ROOT)
    return render(request, 'add-track-question-choices/add-track-question-choices.html', {})


@api_view(["POST"])
def fibonacci_series(request):
    n = int(request.data["number"])
    fibonacci_number = fibonacci(n)
    data = {'fibonacci_number':fibonacci_number}
    return Response(data, status=status.HTTP_200_OK)


# def fibonacci(n):
#     FibArray = [0, 1]
#     if n < 0:
#         print("Incorrect input")
#     elif n <= len(FibArray):
#         return FibArray[n - 1]
#     else:
#         temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
#         FibArray.append(temp_fib)
#         return temp_fib


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
        return "Incorrect input"
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b