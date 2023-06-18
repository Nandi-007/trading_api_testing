FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "API_test/", "-v", "--html=reports/report.html"]

VOLUME /app/reports