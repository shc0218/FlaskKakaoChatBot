from flask import Flask
from get_meal import *
from tool.config import *
import datetime
app = Flask(__name__)

config = ConfigTool()
meal = Meal()
config.setup_config()
date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

@app.route("/meal", methods=["GET", "POST"])
def index():
    meal_data = meal.get_meal(
        config.get_config("neis_api_key"),
        config.get_config("neis_api_city_code"),
        config.get_config("neis_api_school_code"),
        date.strftime("%Y%m%d")
    )
    return {
        "meal_menu": ", ".join(meal_data["meal_menu"]),
        "meal_allergy": ", ".join(meal_data["meal_allergy"])
    }

if __name__ == "__main__":
    app.run(debug=True)