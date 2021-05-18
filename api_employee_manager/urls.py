from django.contrib import admin
from django.urls import path, include
from core.views import EmployeeViewSet, salary_report, age_report
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('reports/employees/salary', salary_report),
    path('reports/employees/age', age_report)
]
