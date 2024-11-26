from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def calculate_pension_age(birth_year):
    # Define pension age logic (example: age 65 for everyone)
    return 65

def pension_age_calculator(request):
    result = None
    if request.method == "POST":
        birth_year = int(request.POST.get("birth_year"))
        pension_age = calculate_pension_age(birth_year)
        result = {
            "birth_year": birth_year,
            "pension_age": pension_age,
            "retirement_year": birth_year + pension_age,
        }
    return render(request, "calculator/index.html", {"result": result})
