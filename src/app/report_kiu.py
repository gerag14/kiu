from datetime import datetime

from .trip_manager import TripManager


class ReportKiu:
    def __init__(self, session):
        self.session = session

    def daily_report(self, date):
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()

        total_packages, total_amount = TripManager(
            session=self.session
        ).get_total_per_day(date_obj)

        data = {
            "date": date,
            "packages": total_packages or 0,
            "total_amount": total_amount or 0,
        }

        return self.print_report(data)

    def print_report(self, data, report_type="daily"):
        if data and report_type == "daily":
            msg = f"Daily report: \n     Trip date: {data['date']}\n     Total Packages: {data['packages']},\n     Total Raised: {data['total_amount']}"  # noqa
        else:
            msg = "Invalid report type"

        print("*" * 20)
        print(msg)
        print("*" * 20)
        return msg
