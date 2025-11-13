example_nested_json = """{
  "id": "root-0001",
  "name": "Example Nested Document",
  "version": 1,
  "active": true,
  "count": 42,
  "null_field": null,
  "profile": {
    "username": "name",
    "email": "name@example.com",
    "created_at": "2023-05-18T12:34:56Z",
    "roles": [
      "admin",
      "editor",
      "user"
    ],
    "addresses": [
      {
        "type": "home",
        "line1": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "postal": "62701",
        "coordinates": {
          "lat": 39.7817,
          "lng": -89.6501
        }
      },
      {
        "type": "work",
        "line1": "456 Commerce Ave",
        "line2": "Suite 800",
        "city": "Metropolis",
        "state": "NY",
        "postal": "10001",
        "coordinates": {
          "lat": 40.7128,
          "lng": -74.0060
        }
      }
    ],
    "preferences": {
      "language": "en-US",
      "timezone": "America/Chicago",
      "notifications": {
        "email": true,
        "sms": false,
        "push": {
          "enabled": true,
          "sound": "chime",
          "vibrate": false
        }
      },
      "theme": {
        "name": "dark",
        "primary_color": "#0b3d91",
        "accent_color": "#ffcc00"
      }
    }
  },
  "groups": [
    {
      "group_id": "g-001",
      "name": "Engineering",
      "metadata": {
        "created": "2022-01-10",
        "owner": "team-lead",
        "tags": ["backend", "api", "services"]
      },
      "members": [
        {
          "id": "u-101",
          "name": "Alice",
          "permissions": ["read", "write"],
          "profile": {
            "email": "alice@example.com",
            "preferences": {
              "language": "en-GB"
            }
          }
        },
        {
          "id": "u-102",
          "name": "Bob",
          "permissions": ["read"],
          "profile": {
            "email": "bob@example.com",
            "preferences": {
              "language": "en-US"
            }
          }
        }
      ]
    },
    {
      "group_id": "g-002",
      "name": "Design",
      "metadata": {
        "created": "2021-08-05",
        "owner": "design-lead",
        "tags": ["ux", "ui", "branding"]
      },
      "members": [
        {
          "id": "u-201",
          "name": "Carol",
          "permissions": ["read", "design"],
          "profile": {
            "email": "carol@example.com"
          }
        }
      ]
    }
  ],
  "events": [
    {
      "id": "e-1001",
      "type": "login",
      "timestamp": "2025-01-10T09:12:34Z",
      "details": {
        "ip": "192.0.2.10",
        "device": {
          "type": "laptop",
          "os": "Windows",
          "browser": "Edge"
        }
      }
    },
    {
      "id": "e-1002",
      "type": "update",
      "timestamp": "2025-02-14T15:00:00Z",
      "details": {
        "changed": ["profile.preferences.theme", "profile.email"],
        "summary": "Updated theme and email address"
      }
    }
  ],
  "matrix": [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[10,11],[12,13],[14,15]]
  ],
  "items": [
    {
      "sku": "A100",
      "quantity": 3,
      "meta": {
        "dimensions": {"w": 10, "h": 5, "d": 2},
        "tags": ["sale", "clearance"]
      }
    },
    {
      "sku": "B200",
      "quantity": 0,
      "meta": {
        "dimensions": {"w": 20, "h": 10, "d": 4},
        "tags": []
      }
    },
    "a simple string item",
    12345,
    false,
    null
  ],
  "deep": {
    "level1": {
      "level2": {
        "level3": {
          "level4": {
            "level5": {
              "level6": {
                "level7": {
                  "level8": {
                    "final": {
                      "message": "This is deeply nested",
                      "values": [1, {"x":2, "y":[3,4,{"z":"end"}]}]
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "logs": [
    {"t":"2025-03-01T00:00:00Z","msg":"system start","severity":"info"},
    {"t":"2025-03-01T01:23:45Z","msg":"user login","user":"u-101","severity":"info"},
    {"t":"2025-03-01T02:34:56Z","msg":"error processing request","severity":"error","ctx":{"code":500,"path":"/api/data"}}
  ],
  "config": {
    "features": {
      "beta": ["feature_x","feature_y"],
      "stable": {"a":true,"b":false}
    },
    "limits": {
      "requests_per_minute": 1200,
      "concurrent_sessions": 50
    },
    "nested_arrays": [
      [{"a":1},{"b":2}],
      [{"c":[{"d":[{"e":"value"}]}]}]
    ]
  }
}"""