# web_app/routes/weather_routes.py

from flask import Blueprint, render_template, request

from app.weather_service import get_hourly_forecasts

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/form")
def weather_form():
    print("VISITED THE WEATHER FORM...")
    return render_template("weather_form.html")

@weather_routes.route("/weather/forecast", methods=["GET", "POST"])
def weather_forecast():
    print("GENERATING A WEATHER FORECAST...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        zip_code = request.form["zip_code"]
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        zip_code = request.args["zip_code"] #> {'zip_code': '20057'}

    results = get_hourly_forecasts(zip_code)
    print(results.keys())
    return render_template("weather_forecast.html", zip_code=zip_code, results=results)

@weather_routes.route("/stern_user_input")
def user_input_form():
    print("VISITED THE STERN USER INPUT FORM...")
    return render_template("stern_user_input.html")

@weather_routes.route("/stern_user_output", methods=["GET", "POST"])
def user_output_results():
    
    print("GENERATING COURSE RESULTS...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        semester = request.form["semester"]
        academic_year = request.form["academic_year"]
        user_category = request.form["user_category"]
        specialization = request.form["specialization"]
        credits = request.form["credits"]
        days = request.form["days"]
        print(user_category)
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        user_category = request.args["user_category"] #> {'zip_code': '20057'}
    return render_template("stern_user_output.html", semester=semester, academic_year=academic_year,user_category=user_category, specialization=specialization, credits=credits, days=days)