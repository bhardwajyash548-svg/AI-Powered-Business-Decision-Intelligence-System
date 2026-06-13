import google.generativeai as genai

API_KEY = "AQ.Ab8RN6JWItlvU4rSNnwIz7P09WDbZLyHp6dASp98SOTiwmS6hA"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_insights(sales, profit):

    prompt = f"""
    Total Sales = {sales}
    Total Profit = {profit}

    Give:
    1. Key Insights
    2. Risks
    3. Opportunities
    4. Recommendations
    """

    response = model.generate_content(prompt)

    return response.text