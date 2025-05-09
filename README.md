# Calendario Protocol v0.1

**Make Human Time Resolvable**  
Calendario is an open protocol to declare and discover human availability across the internet — built to power calendar-aware agents, apps, and people.

## 🔗 What Is Calendario?
Calendario is a decentralized, federated standard that allows individuals and organizations to publish availability, preferences, booking endpoints, and verification proofs using a standardized `.well-known` JSON file.

Think of it as **DNS for Time** — resolvable, declarative, and agent-friendly.

## 📄 Protocol Summary
A Calendario profile is hosted at:
```
/.well-known/calendario/{username}
```
It includes:
- Availability rules and time windows
- Optional pricing and payment enforcement
- Identity and delegation proofs
- Human and programmatic notification channels

## 🌍 Why It Matters
- **Federated:** Anyone can host their profile
- **Resolvable:** One GET request to load data
- **Declarative:** Express intent, not state
- **Composable:** Works across bots, UIs, and agents
- **AI-Ready:** Machine-readable, human-meaningful

## 📦 Sample JSON Profile
```json
{
  "version": "0.1",
  "username": "jane",
  "display_name": "Jane Doe",
  "timezone": "America/New_York",
  "min_notice_hours": 72,
  "max_bookings_per_day": 3,
  "blackouts": [
    "2025-12-01",
    { "start": "2025-12-24", "end": "2025-12-31" }
  ],
  "scheduling": [
    {
      "type": "weekly",
      "days": ["monday", "wednesday", "friday"],
      "hours": ["09:00-11:00", "16:00-18:00"],
      "expires": "2025-06-30"
    }
  ],
  "visibility": "public",
  "allow_anonymous_booking": false,
  "pricing": {
    "hour": 75,
    "half_hour": 45,
    "currency": "USD"
  },
  "payment_required": true,
  "payment_url": "https://yourdomain.com/pay/jane",
  "response_channel": {
    "human_ack_required": true,
    "notify": [
      { "type": "email", "value": "jane@example.com" },
      { "type": "sms", "value": "+14155551234" }
    ],
    "confirm": {
      "meeting_response_url": "https://yourdomain.com/api/bookings/jane",
      "free_busy_url": "https://yourdomain.com/api/freebusy/jane"
    }
  }
}
```

## ✅ Booking Confirmation Format
```json
{
  "status": "confirmed",
  "meeting_url": "https://meet.google.com/xyz-1234",
  "start_time": "2025-06-03T14:00:00Z",
  "duration_minutes": 30,
  "confirmation_message": "Looking forward to speaking with you!"
}
```

## 🔐 Security Guidelines
- Sign identity proofs using [DID Signature 2021](https://w3c-ccg.github.io/ld-proofs/)
- Use HTTPS for all endpoints
- Avoid exposing sensitive webhook/meeting URLs publicly

## 🧠 Concurrency & Conflict Prevention
- Calendario is **declarative**, not stateful
- Always verify current availability with `free_busy_url` before POSTing

## 🧪 Schema Validation
Validate your profile against the [calendario-schema-v0.1.json](./calendario-schema-v0.1.json):
```bash
python validator.py yourfile.json
```

## 🔎 Discovery
Add this TXT record to your DNS:
```
calendario=/.well-known/calendario
```

## 📝 License
Calendario Protocol is open source under the MIT License. Contributions welcome.

## 📚 Resources
- [Spec (HTML)](./spec-v0.1.html)
- [Example JSON Profile](./sample.html)
- [Schema Definition](./schema-v0.1.json)
- [Validator Script](./validator.py)
- [Live Hosted Demo](https://calendario.dev/demo)

---
Made with ❤️ by [RCloud Labs](https://rcloudlabs.com) and the open protocol community.
