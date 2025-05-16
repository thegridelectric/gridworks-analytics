import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Float, JSON, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker
import pendulum

load_dotenv()
backoffice_db_url = os.getenv("GBO_DB_URL")
engine = create_engine(backoffice_db_url)
Base = declarative_base()

class HourlyDataChannel(Base):
    __tablename__ = 'hourly_data_channels'
    name = Column(String, nullable=False)
    time_created_s = Column(Integer, nullable=False)
    version = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint('name', 'version', name='unique_version'),
    )

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

'''
Computed as the sum of the HP's indoor and outdoor unit power (hp-idu-pwr and hp-odu-pwr)
'''
hp_kwh_el = HourlyDataChannel(
    name="hp-kwh-el",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

'''
Computed as the integral of the heat pump's mass flow rate (primary-flow) 
and temperature lift (hp-lwt - hp-ewt) over time, using synchrounous data 
with a 1-second time resolution.
When primary-flow data is missing and primary-pump-pwr data is available, 
the primary-flow is given a fixed value when the primary-pump-pwr is above a given threshold.
'''
hp_kwh_th = HourlyDataChannel(
    name="hp-kwh-th",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

'''
Computed as the integral of the mass flow rate and the temperature difference over time, 
using synchrounous data with a 1-second time resolution.
'''
dist_kwh = HourlyDataChannel(
    name="dist-kwh",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

store_change_kwh = HourlyDataChannel(
    name="store-change-kwh",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

hp_avg_lwt = HourlyDataChannel(
    name="hp-avg-lwt",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

hp_avg_ewt = HourlyDataChannel(
    name="hp-avg-ewt",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

dist_avg_swt = HourlyDataChannel(
    name="dist-avg-swt",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

dist_avg_rwt = HourlyDataChannel(
    name="dist-avg-rwt",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

buffer_depth1_start = HourlyDataChannel(
    name="buffer-depth1-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

buffer_depth2_start = HourlyDataChannel(
    name="buffer-depth2-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

buffer_depth3_start = HourlyDataChannel(
    name="buffer-depth3-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

buffer_depth4_start = HourlyDataChannel(
    name="buffer-depth4-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank1_depth1_start = HourlyDataChannel(
    name="tank1-depth1-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank1_depth2_start = HourlyDataChannel(
    name="tank1-depth2-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank1_depth3_start = HourlyDataChannel(
    name="tank1-depth3-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank1_depth4_start = HourlyDataChannel(
    name="tank1-depth4-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank2_depth1_start = HourlyDataChannel(
    name="tank2-depth1-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank2_depth2_start = HourlyDataChannel(
    name="tank2-depth2-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank2_depth3_start = HourlyDataChannel(
    name="tank2-depth3-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank2_depth4_start = HourlyDataChannel(
    name="tank2-depth4-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank3_depth1_start = HourlyDataChannel(
    name="tank3-depth1-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank3_depth2_start = HourlyDataChannel(
    name="tank3-depth2-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank3_depth3_start = HourlyDataChannel(
    name="tank3-depth3-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

tank3_depth4_start = HourlyDataChannel(
    name="tank3-depth4-start",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

relay_3_pulled_fraction = HourlyDataChannel(
    name="relay-3-pulled-fraction",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

relay_5_pulled_fraction = HourlyDataChannel(
    name="relay-5-pulled-fraction",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

relay_6_pulled_fraction = HourlyDataChannel(
    name="relay-6-pulled-fraction",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

relay_9_pulled_fraction = HourlyDataChannel(
    name="relay-9-pulled-fraction",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

zone1_heatcall_fraction = HourlyDataChannel(
    name="zone1-heatcall-fraction",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

zone2_heatcall_fraction = HourlyDataChannel(
    name="zone2-heatcall-fraction",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

zone3_heatcall_fraction = HourlyDataChannel(
    name="zone3-heatcall-fraction",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

zone4_heatcall_fraction = HourlyDataChannel(
    name="zone4-heatcall-fraction",
    time_created_s=int(pendulum.datetime(2025,5,1).timestamp()),
    version="1.0.0"
)

session.add_all([
    hp_kwh_el, 
    hp_kwh_th, 
    dist_kwh, 
    store_change_kwh, 
    hp_avg_lwt, 
    hp_avg_ewt, 
    dist_avg_swt, 
    dist_avg_rwt, 
    
    buffer_depth1_start, 
    buffer_depth2_start, 
    buffer_depth3_start, 
    buffer_depth4_start, 

    tank1_depth1_start, 
    tank1_depth2_start, 
    tank1_depth3_start, 
    tank1_depth4_start, 

    tank2_depth1_start, 
    tank2_depth2_start, 
    tank2_depth3_start, 
    tank2_depth4_start, 

    tank3_depth1_start,
    tank3_depth2_start, 
    tank3_depth3_start, 
    tank3_depth4_start, 
    
    relay_3_pulled_fraction, 
    relay_5_pulled_fraction, 
    relay_6_pulled_fraction, 
    relay_9_pulled_fraction, 
    
    zone1_heatcall_fraction, 
    zone2_heatcall_fraction, 
    zone3_heatcall_fraction, 
    zone4_heatcall_fraction
])
session.commit()