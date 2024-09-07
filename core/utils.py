def fetch_course_allocation(lecturer_name):
    try:
        course_allocation = CourseAllocation.objects.get(lecturer=lecturer_name)
        return course_allocation.course_code
    except CourseAllocation.DoesNotExist:
        return None