from datetime import datetime

from models import Airport, Client, Plane
from schemas import TripDetailSchema, TripSchema

from .report_kiu import ReportKiu
from .trip_manager import TripManager


class KiuChallenge:
    def __init__(self, session):
        self.session = session
        self.trip_manager = TripManager(session)
        self.report = ReportKiu(session)

    def run(self):
        to_exit = True
        while to_exit:
            option = self.console_menu()
            if option == "6":
                to_exit = False
        exit()

    def console_menu(self):
        print("Welcome to KIU Challenge")
        print("1. Add new trip")
        print("2. Daily report")
        print("3. Add client")
        print("4. Add plane")
        print("5. Add airport")
        print("6. Exit")

        option = input("Select an option: ")

        if option == "1":
            self.add_new_trip()
        elif option == "2":
            self.daily_report()
        elif option == "3":
            self.add_client()
        elif option == "4":
            self.add_plane()
        elif option == "5":
            self.add_airport()
        elif option == "6":
            print("Thanks for using KIU Challenge")

        else:
            print("Invalid option")
            exit()

        return option

    def daily_report(self):
        date = input("Date (yyyy-mm-dd): ")
        self.report.daily_report(date)

    def add_new_trip(self):
        print("Add new trip")
        new_trip = TripSchema(
            plane_id=input("Plane id: "),
            airport_from_id=input("Airport from id: "),
            airport_to_id=input("Airport to id: "),
            departure_date=datetime.strptime(
                input("Departure date (yyyy-mm-dd): "), "%Y-%m-%d"
            ),
            arrive_date=datetime.strptime(
                input("Arrive date (yyyy-mm-dd): "), "%Y-%m-%d"
            ),
            trip_detail=[],
        )
        add_detail = True
        while add_detail:
            new_detail = TripDetailSchema(
                client_id=input("Client id: "),
                package_quantity=input("Package quantity: "),
            )
            new_trip.trip_detail.append(new_detail)
            add_detail = input("Do you want to add another detail? (y/n): ") == "y"

        self.trip_manager.create_new_trip(new_trip)
        print("Trip added successfully")

    def add_client(self):
        print("Add client")
        username = input("Client username: ")
        self.session.add(Client(username=username))
        self.session.commit()

    def add_plane(self):
        print("Add plane")
        code = input("Plane code: ")
        self.session.add(Plane(code=code))
        self.session.commit()

    def add_airport(self):
        print("Add plane")
        name = input("Airport name: ")
        self.session.add(Airport(name=name))
        self.session.commit()
