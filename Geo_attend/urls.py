
from django.urls import path
from employees import views
urlpatterns = [
    path("register-company/", views.register_company, name="register_company"),
    path("create-employee/", views.create_employee, name="create_employee"),
    path("employee/", views.get_employee, name="get_employee"),
    path("employee/update/", views.update_employee_info, name="update_employee"),
    path("employee/delete/", views.delete_current_employee, name="delete_employee"),
    path("mark-attendance/", views.mark_attendance, name="mark_attendance"),
    path("attendance-records/", views.get_all_attendance_records, name="get_attendance_records"),
    path("login/",views.login_user,name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("get_login/",views.get_logged_in_employee, name="get_logged_in_employee"),
    path("admin_login/", views.cmp_admin, name="admin_login"),
    path("leave-apply/",views.apply_leave,name="leave-emp"),
    path("leave-approve/",views.approve_leave,name="leave-approve"),
    path("update-leave/",views.update_leave_status),
    path("export-attendance/", views.export_attendance_to_csv, name="export_attendance"),
]