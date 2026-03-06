from django.shortcuts import render
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("AIzaSyAR9wLsB_KFR96MidEVjSx-YAYm35ZVeSg"))


def home(request):

    answer = ""

    if request.method == "POST":
        question = request.POST.get("question")

        response = client.models.generate_content(
            model="Gemini 2.5 Flash-ite",
            contents=question
        )

        answer = response.text

    return render(request, "index.html", {"answer": answer})