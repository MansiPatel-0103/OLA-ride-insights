# Data Dictionary – OLA Ride Insights

## 1. Dataset overview

| Item | Detail |
|---|---|
| File | `data/raw/OLA_DataSet.xlsx` (sheet **July**) |
| Rows | 103,024 (1 row = 1 booking) |
| Columns | 20 |
| Period | 1–31 July 2024 |
| City | Bangalore (50 areas) |
| Unique customers | 94,544 |
| Other sheets | `Sheet1` (rough working notes) and `Sheet2` (vehicle icon links) – not used |

**Key idea:** each row is a **booking** (a ride request), not a completed ride. Only 62.1% of bookings became successful rides.

## 2. The journey of a booking

1. **Customer books** → Date, Time, Booking_ID, Customer_ID, Vehicle_Type, Pickup_Location, Drop_Location, Booking_Value
2. **Booking ends in one of 4 ways** → Booking_Status
   - Driver Not Found → story ends
   - Canceled by Driver → reason in Canceled_Rides_by_Driver
   - Canceled by Customer → reason in Canceled_Rides_by_Customer
   - Success → continues below
3. **Vehicle arrives** → V_TAT
4. **Customer gets in** → C_TAT
5. **Ride happens** → Ride_Distance, Incomplete_Rides, Incomplete_Rides_Reason
6. **Customer pays** → Payment_Method
7. **Both give ratings** → Driver_Ratings, Customer_Rating

## 3. Column descriptions

| Column | Description | Type | Values / range | Filled for |
|---|---|---|---|---|
| Date | Date and time of booking | Date-time | 2024-07-01 to 2024-07-31 | All |
| Time | Time of booking (repeats the time inside Date) | Time | 00:00 to 23:59 | All |
| Booking_ID | Unique booking number | Text | "CNR" + 10 digits, all unique | All |
| Customer_ID | Customer number | Text | "CID" + 6 digits, 94,544 unique | All |
| Booking_Status | Outcome of the booking | Text | Success, Canceled by Driver, Canceled by Customer, Driver Not Found | All |
| Vehicle_Type | Vehicle chosen | Text | Bike, eBike, Auto, Mini, Prime Sedan, Prime Plus, Prime SUV | All |
| Pickup_Location | Start area | Text | 50 Bangalore areas | All |
| Drop_Location | End area | Text | 50 Bangalore areas | All |
| V_TAT | Vehicle turnaround time – time for the vehicle to reach the customer | Number | 35–308 (avg 171) | Success only |
| C_TAT | Customer turnaround time – time for the customer to get in | Number | 25–145 (avg 85) | Success only |
| Canceled_Rides_by_Customer | Reason the customer cancelled | Text | 5 reasons | Canceled by Customer only |
| Canceled_Rides_by_Driver | Reason the driver cancelled | Text | 4 reasons | Canceled by Driver only |
| Incomplete_Rides | Did the ride stop halfway? | Text | Yes / No | Success only |
| Incomplete_Rides_Reason | Why the ride stopped | Text | Customer Demand, Vehicle Breakdown, Other Issue | Incomplete = Yes only |
| Booking_Value | Fare of the booking (₹) | Number | ₹100–₹2,999 (avg ₹549) | All (see note below) |
| Payment_Method | How the customer paid | Text | Cash, UPI, Credit Card, Debit Card | Success only |
| Ride_Distance | Distance travelled (km) | Number | 1–49 km for Success; 0 for all others | All |
| Driver_Ratings | Rating given **to the driver** by the customer | Number | 3.0–5.0 | Success only |
| Customer_Rating | Rating given **to the customer** by the driver | Number | 3.0–5.0 | Success only |
| Vehicle Images | Link to a vehicle icon | Text | 7 links (one per vehicle) | All – not used |

## 4. Booking status breakdown

| Booking_Status | Bookings | Share |
|---|---|---|
| Success | 63,967 | 62.1% |
| Canceled by Driver | 18,434 | 17.9% |
| Canceled by Customer | 10,499 | 10.2% |
| Driver Not Found | 10,124 | 9.8% |
| **Total** | **103,024** | **100%** |

## 5. Key observations from data exploration

1. **Missing values are expected, not errors.** 39,057 bookings (all non-successful) have no payment, ratings or turnaround times, because the ride never happened.
2. **Revenue trap.** Booking_Value is filled even for cancelled bookings (the fare shown, not money earned). Revenue must use **Success rides only**: ₹3,50,80,467 (≈ ₹3.51 crore), not ₹5.65 crore.
3. **Distance trap.** Ride_Distance is 0 for all non-successful bookings, so averages must use Success rides only, or they look too small.
4. **Incomplete rides sit inside "Success".** 3,926 successful bookings stopped halfway.
5. **Hidden driver problem.** 56% of customer cancellations (5,845 of 10,499) are driver-related ("Driver is not moving towards pickup location", "Driver asked to cancel").
6. **Possible anomaly.** 2,121 bookings have the same pickup and drop location.
7. **No low ratings.** All ratings are between 3.0 and 5.0.
8. **Few repeat customers.** Most customers booked once; the highest is 5 bookings, with ties at 4 – relevant for "top customers" questions.
9. **Evenly spread data.** Bookings are very even across days, hours and vehicles, suggesting practice data; time-based differences will be small.
10. **No duplicates.** 0 repeated rows and 0 repeated Booking_IDs.

## 6. Assumptions

- V_TAT and C_TAT are assumed to be in **seconds** (units are not stated in the data).
- Booking_Value for non-successful bookings is treated as a **quoted fare**, not revenue.