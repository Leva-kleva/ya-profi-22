post = {
    "type": "object",
    "properties": {
        "login": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["login", "password"]
}

put = {
    "type": "object",
    "properties": {
        "password": {"type": "string"}
    },
    "required": ["password"]
}
