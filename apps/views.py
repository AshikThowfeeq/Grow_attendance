from django.shortcuts import render, redirect
from .models import AttendanceTest
from collections import defaultdict
from datetime import date
import datetime

# def attendance_list(request):
#     all_attendance_records = AttendanceTest.objects.all()
#     context = {
#         'attendance_records': all_attendance_records
#     }
#     return render(request, 'attendance_list.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        if (username == 'Grow' and password == '1234') or \
                (username == 'Lead@Control' and password == '1234') or \
                (username == 'Grow@Dev' and password == '1234'):
            request.session['username'] = username
            return redirect('index/')
        else:
            error_message = "Invalid Login"
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def index(request):
    return render(request,'index.html')

def atts(request):
    # Fetch all attendance records
    all_attendances = AttendanceTest.objects.all().order_by('ctime')

    # Get unique dates and names for table headers
    unique_dates = sorted({
        attendance.ctime.date() if isinstance(attendance.ctime, datetime.datetime) else attendance.ctime
        for attendance in all_attendances
    })
    unique_names = sorted({attendance.name for attendance in all_attendances})

    # Create a data structure to keep track of presence
    presence_data = defaultdict(lambda: defaultdict(lambda: "Absent"))

    for attendance in all_attendances:
        d = attendance.ctime.date() if isinstance(attendance.ctime, datetime.datetime) else attendance.ctime
        n = attendance.name
        presence_data[d][n] = "Present"

    return render(request,'table.html', {
        'unique_dates': unique_dates,
        'unique_names': unique_names,
        'presence_data': presence_data
    })

# def filter_by_name(request):
#     # Fetch all attendance records
#     all_attendances = AttendanceTest.objects.all().order_by('ctime')
#
#     # Get unique dates and names for table headers
#     unique_dates = sorted({
#         attendance.ctime.date() if isinstance(attendance.ctime, datetime.datetime) else attendance.ctime
#         for attendance in all_attendances
#     })
#     unique_names = sorted({attendance.name for attendance in all_attendances})
#
#     # Create a data structure to keep track of presence
#     presence_data = defaultdict(lambda: defaultdict(lambda: "Absent"))
#
#     for attendance in all_attendances:
#         d = attendance.ctime.date() if isinstance(attendance.ctime, datetime.datetime) else attendance.ctime
#         n = attendance.name
#         presence_data[d][n] = "Present"
#
#     return render(request, 'filtered_template.html', {
#         'unique_dates': unique_dates,
#         'unique_names': unique_names,
#         'presence_data': presence_data
#     })

