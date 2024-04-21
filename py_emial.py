name: Send Email

on:
  workflow_dispatch:  # This event allows you to manually trigger the workflow

jobs:
  send_email:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'  # Choose the Python version you want to use

      - name: Send email
        run: python send_email.py  # Replace with the path to your Python script
        env:
          SMTP_SERVER: smtp.example.com
          SMTP_PORT: 587
          SMTP_USERNAME: ${{ secrets.SMTP_USERNAME }}  # Store sensitive information like this as secrets in your repository settings
          SMTP_PASSWORD: ${{ secrets.SMTP_PASSWORD }}
          FROM_EMAIL: from@example.com
          TO_EMAIL: to@example.com
