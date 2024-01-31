import logging

from sqlalchemy import func

from models import Trip, TripDetail
from schemas import TripDetailSchema, TripSchema


class TripManager:
    def __init__(self, session):
        self.session = session

    def create_new_trip(self, new_trip: TripSchema):
        try:
            self.session.begin()
            trip = Trip(
                plane_id=new_trip.plane_id,
                airport_from_id=new_trip.airport_from_id,
                airport_to_id=new_trip.airport_to_id,
                departure_date=new_trip.departure_date,
                arrive_date=new_trip.arrive_date,
            )

            self.session.add(trip)
            for trip_d in trip.trip_detail:
                self.create_trip_detail(trip_d)

            self.session.commit()
            self.session.refresh(trip)
            return trip
        except Exception as e:
            self.session.rollback()
            logging.exception(f"Error to add new trip: {e}")
        finally:
            # Cerrar la sesión
            self.session.close()

    def create_trip_detail(self, new_trip_detail: TripDetailSchema):
        new_trip_d = Trip(
            client_id=new_trip_detail.client_id,
            package_quantity=new_trip_detail.package_quantity,
            package_price=new_trip_detail.package_price,
        )

        self.session.add(new_trip_d)
        return new_trip_d

    def get_total_per_day(self, date_str):
        totals_query = (
            self.session.query(
                func.sum(TripDetail.package_quantity).label("total_packages"),
                func.sum(TripDetail.package_quantity * TripDetail.package_price).label(
                    "total_amount"
                ),
            )
            .select_from(TripDetail)
            .join(Trip)
            .filter(func.date(Trip.departure_date) == date_str)
        )

        total_packages, total_amount = totals_query.one()

        return total_packages, total_amount
