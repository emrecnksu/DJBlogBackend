# blog/rules/validation_rules.py

POST_VALIDATION_RULES = {
    "required_fields": ["title", "content"],
    "min_lengths": {
        "title": 8,
        "content": 100,
    }
}

COMMENT_VALIDATION_RULES = {
    "required_fields": ["content"],
    "min_lengths": {
        "content": 5,
    }
}

AUTH_VALIDATION_RULES = {
    "register_required_fields": ["username", "email", "password", "first_name", "last_name"],
    "login_required_fields": ["username", "password"],
    "min_lengths": {
        "password": 6,
    },
    "unique_fields": ["username", "email"]
}


