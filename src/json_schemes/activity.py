ACTIVITY_SCHEME = {
    "type": "object",
    "properties": {
        "activity": {"type": "string"},
        "type": {"type": "string", "enum": ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]},
        "participants": {"type": "number"},
        "price": {"type": "number"},
        "link": {"type": "string"},
        "key": {"type": "string"}
    },
    "required": ["key"]
}
