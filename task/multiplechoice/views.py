import time
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
    start_time = time.time()
    fibonacci_number = fibonacci(n)
    end_time = time.time()
    excution_time = end_time-start_time
    data = {'fibonacci_number':fibonacci_number, 'excution_time': excution_time}
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


# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#         return "Incorrect input"
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#         return b


def fibonacci_helper(n, r):
    """Return the nth Fibonacci number and store the ith Fibonacci number in
    r[i] for 0 <= i <= n."""
    if r[n] >= 0:
        return r[n]

    if (n == 0 or n == 1):
        q = n
    else:
        q = fibonacci_helper(n - 1, r) + fibonacci_helper(n - 2, r)
    r[n] = q

    return q


def fibonacci(n):
    """Return the nth Fibonacci number."""
    # r[i] will contain the ith Fibonacci number
    r = [-1]*(n + 1)
    return fibonacci_helper(n, r)


