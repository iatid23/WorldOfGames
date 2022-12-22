import json

class Info:
    quote: float
    timestamp: float

class Query:
    amount: int
    fromm: str
    to: str


class Convert:
    info: Info
    query: Query
    result: float
    success: bool

