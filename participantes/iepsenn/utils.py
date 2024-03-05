from datetime import datetime, timezone


def format_date_to_utc(date: datetime):
    return (
        date.astimezone(timezone.utc)
        .isoformat("T", "milliseconds")
        .replace("+00:00", "Z")
    )
