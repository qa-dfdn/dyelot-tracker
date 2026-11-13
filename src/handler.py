"""Request handler for dyelot-tracker."""

def handle(event: dict) -> dict:
    kind = event.get("kind", "scan")
    return {"ok": True, "kind": kind, "service": "dyelot-tracker"}
