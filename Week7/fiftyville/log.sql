-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports WHERE street == 'Humphrey Street' AND year == 2024 AND month == 7 AND day == 28; -- id 295 //took place at 10:15am at the Humphrey Stree//bakery

SELECT * FROM interviews  WHERE year == 2024 AND month == 7 AND day == 28 AND transcript LIKE "%bakery%";
-- If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
-- 2024/07/28 before 1015 ATM\\Leggett Street\\withdrawing
-- 2024/07/29 earliest flight out of Fiftyville tomorrow

--CAR
SELECT name FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2024 AND month = 7 AND day = 28 AND hour = 10 AND minute >=15 AND minute < 25 AND activity = 'exit';

--ATM
SELECT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2024 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

--Tel call
SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE year = 2024 AND month = 7 AND day = 28
AND duration < 60;

--Flight
SELECT name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = (SELECT id FROM flights
                  WHERE year = 2024 AND month = 7 AND day = 29
                  ORDER BY hour, minute LIMIT 1);


--THIEF is:
SELECT people.name FROM people
WHERE name IN(SELECT name FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
WHERE year = 2024 AND month = 7 AND day = 28 AND hour = 10 AND minute >=15 AND minute < 25 AND activity = 'exit')
AND name IN (SELECT name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2024 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw')
AND name IN (SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE year = 2024 AND month = 7 AND day = 28
AND duration < 60)
AND name IN (SELECT name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = (SELECT id FROM flights
                  WHERE year = 2024 AND month = 7 AND day = 29
                  ORDER BY hour, minute LIMIT 1));







--CITY
SELECT city FROM airports
WHERE id = (SELECT destination_airport_id FROM flights
            WHERE year = 2024 AND month = 7 AND day = 29
            ORDER BY hour, minute LIMIT 1);

--The ACCOMPLICE is:
SELECT name FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE year = 2024 AND month = 7 AND day = 28
AND duration < 60
AND caller = (SELECT phone_number FROM people WHERE name = 'Bruce');


--airports
--crime_scene_reports
--people
--atm_transactions
--flights
--phone_calls
--bakery_security_logs
--interviews
--bank_accounts
--passengers
