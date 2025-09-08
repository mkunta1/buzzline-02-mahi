"""
basic_generator_mahi.py

Generate streaming patient check-in messages.
"""
print("Kafka producer starting...")

import os
import random
import time

from dotenv import load_dotenv
from utils.utils_logger import logger

load_dotenv()

def get_message_interval() -> int:
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval

PATIENT_NAMES = [
    "Aman Ruth",
    "John Doe",
    "Jane Smith",
    "Alex Kim",
    "Mary Johnson",
    "David Lee",
    "Samantha Brown"
]

PATIENT_GENDERS = {
    "Aman Ruth": "male",
    "John Doe": "male",
    "Jane Smith": "female",
    "Alex Kim": "other",
    "Mary Johnson": "female",
    "David Lee": "male",
    "Samantha Brown": "female"
}

CHECKIN_STATUSES = [
    "has checked in at the hospital.",
    "just arrived at the reception desk.",
    "is here for their appointment.",
    "completed the registration process.",
    "is waiting in the lobby."
    "is with the provider."
]

def generate_patient_checkin_messages():
    while True:
        patient = random.choice(PATIENT_NAMES)
        gender = PATIENT_GENDERS.get(patient, "other")
        
        pronoun = "they"
        if gender.lower() == "male":
            pronoun = "he"
        elif gender.lower() == "female":
            pronoun = "she"
        
        status = random.choice(CHECKIN_STATUSES)
        message = f"Patient {patient} is here at the hospital; {pronoun} {status}"
        yield message

def main() -> None:
    logger.info("START patient check-in producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    interval_secs: int = get_message_interval()

    for message in generate_patient_checkin_messages():
        logger.info(message)
        time.sleep(interval_secs)

    logger.info("END patient check-in producer.")

if __name__ == "__main__":
    main()