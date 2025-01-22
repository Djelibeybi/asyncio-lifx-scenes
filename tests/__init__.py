"""Test configuration."""

LIFX_SCENES = [
    {
        "uuid": "11111111-2222-3333-4444-555555555555",
        "name": "TestScene1",
        "account": {"uuid": "55555555-4444-3333-2222-111111111111"},
        "states": [
            {
                "selector": "id:d073d5123456",
                "power": "on",
                "color": {"hue": 0, "saturation": 0, "brightness": 0.9, "kelvin": 2700},
            }
        ],
        "created_at": 1737541235,
        "updated_at": 1737541235,
    },
    {
        "uuid": "11111111-2222-3333-4444-555555555555",
        "name": "TestScene2",
        "account": {"uuid": "55555555-4444-3333-2222-111111111111"},
        "states": [
            {
                "selector": "id:d073d5112233",
                "power": "on",
                "color": {"hue": 0, "saturation": 0, "brightness": 0.9, "kelvin": 3500},
            }
        ],
        "created_at": 1737541235,
        "updated_at": 1737541235,
    },
]
