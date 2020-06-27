# web_app/routes/weather_routes.py

from flask import Blueprint, render_template, request

from app.schedule import schedule_filter

schedule_routes = Blueprint("schedule_routes", __name__)

@schedule_routes.route("/stern_user_input")
def user_input_form():
    print("VISITED THE STERN USER INPUT FORM...")
    return render_template("stern_user_input.html")

@schedule_routes.route("/stern_user_output", methods=["GET", "POST"])
def user_output_results():
    
    #print("GENERATING COURSE RESULTS...")

    if request.method == "POST":
        #print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        SEMESTER = str(request.form["semester"])
        ACADEMIC_YEAR = str(request.form["academic_year"])
        USER_CATEGORY = str(request.form["user_category"])
        USER_SPECIALIZATION = str(request.form["specialization"])
        NUM_CREDITS = str(request.form["credits"])
        USER_DAYS = str(request.form["days"])

        filtered_df = schedule_filter(SEMESTER, ACADEMIC_YEAR, USER_CATEGORY, USER_SPECIALIZATION, NUM_CREDITS, USER_DAYS)
        #print(filtered_df)

        RESULTS_COUNT = len(filtered_df)

        html = filtered_df.to_html(index=False) # to create HTML table on output page

    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        USER_CATEGORY = request.args["user_category"] #> {'zip_code': '20057'}

    return render_template("stern_user_output.html", semester=SEMESTER, academic_year=ACADEMIC_YEAR, user_category=USER_CATEGORY, specialization=USER_SPECIALIZATION, credits=NUM_CREDITS, days=USER_DAYS, results_count = RESULTS_COUNT, data=html)