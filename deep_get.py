from functools import reduce


def deep_get(data, keys):
    return reduce(lambda obj, key: obj[key], keys, data)


webhook_data = {
    "event_type": "subscription_created",
    "content": {
        "customer": {
            "created_at": 1575397900,
            "card_status": "card",
            "subscription": {
                "status": "active",
                "created_at": 1575397900,
                "next_billing_at": 1577817100,
            },
        }
    },
}
status_key = ("content", "customer", "subscription", "status")
assert deep_get(webhook_data, status_key) == "active"
