from adobe_analytics import Client, ReportDefinition

client = Client.from_json("my_credentials.json")
suites = client.suites()
suite = suites["my_report_suite_id"]

report_definition = ReportDefinition(
    dimensions=[
        "page",
        "product",
        "lasttouchchannel"
    ],
    metrics=[
        "visits",
        "orders"
    ],
    date_from="2017-01-01",
    date_to="2017-12-31",
    granularity="day"
)
dataframe = suite.download(report_definition)
print(dataframe.head())
