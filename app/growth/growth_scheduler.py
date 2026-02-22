import time
from threading import Thread

from .growth_engine import (
    detect_growth_signals,
    generate_growth_actions,
    execute_approved_actions
)


def growth_loop(get_usage_callback, interval=300):
    while True:
        try:
            usage_data = get_usage_callback()

            detect_growth_signals(usage_data)
            generate_growth_actions()
            execute_approved_actions()

        except Exception as e:
            print("Growth Engine Error:", e)

        time.sleep(interval)


def start_growth_engine(get_usage_callback):
    thread = Thread(
        target=growth_loop,
        args=(get_usage_callback,),
        daemon=True
    )
    thread.start()