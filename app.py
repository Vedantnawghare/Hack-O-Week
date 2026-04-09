from flask import Flask, render_template, request, jsonify
from datetime import datetime
import difflib

app = Flask(__name__)

def is_similar(word, keyword):
    return difflib.SequenceMatcher(None, word, keyword).ratio() > 0.7


def chatbot_response(user_input):
    user_input = user_input.lower()
    words = user_input.split()

    # GREETING
    for w in words:
        if is_similar(w, "hi") or is_similar(w, "hello") or is_similar(w, "hey"):
            return {"type": "text", "message": "Hi 👋 How can I help you today?"}

    # ADMISSIONS
    for w in words:
        if is_similar(w, "admission") or is_similar(w, "apply"):
            return {"type": "text", "message": (
                "Admissions are based on eligibility criteria and merit.\n"
                "👉 You can find the complete admission procedure here:\n"
                "https://sitnagpur.edu.in/first-year-admission-procedure"
            )}


    # FEES
    for w in words:
        if is_similar(w, "fee") or is_similar(w, "fees"):
            return {"type": "text", "message": (
                "The fee structure varies depending on the course.\n"
                "👉 View detailed fee information here:\n"
                "https://sitnagpur.edu.in/fees-structure"
            )}

    # TIMINGS
    for w in words:
        if is_similar(w, "time") or is_similar(w, "timing"):
            return {"type": "text", "message": "College operates from  9:00 AM – 5:00 PM (Mon–Fri)."}

    # COURSES
    for w in words:
        if is_similar(w, "course"):
            return {"type": "text", "message": (
                "👉 Explore all available courses here:\n"
                "https://sitnagpur.edu.in/courses"
            )}

    # PLACEMENTS
    for w in words:
        if is_similar(w, "placement") or is_similar(w, "job"):
            return {"type": "text", "message": (
                "The institute provides placement support through reputed companies.\n"
                "👉 Check placement records and details here:\n"
                "https://sitnagpur.edu.in/placement-record"
            )}


    # HOSTEL
    for w in words:
        if is_similar(w, "hostel"):
            return {"type": "text", "message": (
                "Separate hostel facilities are available for students.\n"
                "👉 Learn more about hostel amenities here:\n"
                "https://sitnagpur.edu.in/hostel-facilities"
            )}


    # LIBRARY
    for w in words:
        if is_similar(w, "library"):
            return {"type": "text", "message": (
                "The college library is well-equipped with books and digital resources.\n"
                "⏰ Timings: 8:00 AM – 8:00 PM (Working days)"
            )}


    # SCHOLARSHIPS
    for w in words:
        if is_similar(w, "scholarship"):
            return {"type": "text", "message": (
                "Scholarships are available for eligible and meritorious students.\n"
                "👉 View scholarship schemes and eligibility here:\n"
                "https://sitnagpur.edu.in/scholarships"
            )}


    # CONTACT
    for w in words:
        if is_similar(w, "contact") or is_similar(w, "call"):
            return {"type": "text", "message": (
                "You can reach the institute for any queries using the details below:\n"
                "👉 https://sitnagpur.edu.in/contactus"
            )}


    # LOCATION
    for w in words:
        if is_similar(w, "location") or is_similar(w, "address"):
            return {"type": "text", "message": (
                "SIT Nagpur is located in Wathoda Layout, Nagpur.\n"
                "👉 View the location on Google Maps:\n"
                "https://goo.gl/maps/example"
            )}

    # FALLBACK
    with open("unanswered.txt", "a") as f:
        f.write(f"{datetime.now()} - {user_input}\n")

    return {
        "type": "buttons",
        "message": "I might not have understood that 🤔\n\nYou can ask me about:",
        "buttons": [
            "Admissions",
            "Fees",
            "College Timings",
            "Courses Offered",
            "Placements",
            "Hostel Facilities",
            "Library",
            "Scholarships",
            "Contact Details",
            "Location / Address"
        ]
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_bot_response():
    response = chatbot_response(request.form["msg"])
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
