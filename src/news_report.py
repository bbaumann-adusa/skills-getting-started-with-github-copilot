"""
Daily Last Mile E-Commerce News Report

Provides curated highlights of US e-commerce competitors focused exclusively
on Last Mile delivery operations, innovations, and competitive developments.
"""

from datetime import date

# US e-commerce competitor profiles with Last Mile highlights
COMPETITORS = {
    "Amazon": {
        "description": "World's largest e-commerce platform with its own end-to-end logistics network.",
        "last_mile_highlights": [
            "Expanding Amazon Delivery Service Partner (DSP) network to over 3,000 small businesses.",
            "Deploying electric delivery vans (Rivian EDV) — targeting 100,000 units by 2030.",
            "Amazon Key In-Garage and In-Car delivery reducing failed delivery attempts.",
            "Same-day delivery now available in 90+ US metro areas via Amazon Logistics.",
        ],
        "focus_areas": ["Same-day delivery", "Electric vehicles", "DSP network", "Autonomous delivery"],
    },
    "Walmart": {
        "description": "Brick-and-mortar retail giant leveraging its 4,700+ US stores as micro-fulfillment hubs.",
        "last_mile_highlights": [
            "Walmart GoLocal white-label delivery service opened to third-party retailers.",
            "Store-fulfilled delivery now covers 93% of US households within 10 miles.",
            "Spark Driver crowd-sourced delivery network surpassed 50,000 active drivers.",
            "Piloting autonomous delivery with Cruise and Gatik in select markets.",
        ],
        "focus_areas": ["Store-as-hub", "Crowd-sourced delivery", "Autonomous vehicles", "GoLocal"],
    },
    "Target": {
        "description": "Omnichannel retailer using Shipt and in-store fulfillment for last mile execution.",
        "last_mile_highlights": [
            "Shipt same-day delivery expanded to over 200 retail partners beyond Target.",
            "Drive Up with Returns reducing package return friction at curbside.",
            "Sortation centers in 15+ markets cutting same-day delivery costs by 40%.",
            "Target Circle 360 offering unlimited same-day delivery for members.",
        ],
        "focus_areas": ["Shipt network", "Drive Up", "Sortation centers", "Membership delivery"],
    },
    "FedEx": {
        "description": "Global carrier investing heavily in residential last mile and smart locker networks.",
        "last_mile_highlights": [
            "FedEx OnSite network of 12,000+ retail drop-off/pick-up locations across the US.",
            "FedEx Surround predictive analytics reducing missed deliveries by 20%.",
            "Rolling out FedEx Autonomous Delivery Robots on college campuses and suburbs.",
            "FedEx Returns Technology enabling boxless, label-free returns at Walgreens and Dollar General.",
        ],
        "focus_areas": ["OnSite network", "Predictive analytics", "Autonomous robots", "Returns"],
    },
    "UPS": {
        "description": "Carrier focused on density-based efficiency and healthcare last mile delivery.",
        "last_mile_highlights": [
            "UPS Access Point network exceeds 22,000 locations for flexible pickup and drop-off.",
            "UPS My Choice for Business giving SMBs real-time last mile visibility.",
            "Drone delivery (UPS Flight Forward) expanding healthcare specimen and prescription routes.",
            "UPS Carbon Neutral program offering offset options on all residential deliveries.",
        ],
        "focus_areas": ["Access Point network", "Drone delivery", "Healthcare logistics", "Sustainability"],
    },
    "USPS": {
        "description": "National postal carrier providing universal last mile coverage including rural and remote areas.",
        "last_mile_highlights": [
            "USPS Delivering for America plan: replacing 66,000 delivery vehicles with electric models.",
            "Informed Delivery interactive notifications sent to 60M+ enrolled households.",
            "Package Plus service offering integrated last mile for e-commerce sellers.",
            "Parcel Select partnership remains key last mile injection point for FedEx SmartPost and UPS SurePost.",
        ],
        "focus_areas": ["Electric fleet", "Informed Delivery", "Rural coverage", "Carrier injection"],
    },
    "Instacart": {
        "description": "Grocery-focused platform specializing in ultra-fast last mile delivery from local stores.",
        "last_mile_highlights": [
            "Instacart+ membership driving 15-minute delivery pilots in dense urban markets.",
            "Caper Cart smart shopping cart enabling seamless checkout-to-delivery flow.",
            "Carrot Ads platform monetizing last mile data for CPG brands.",
            "Instacart Business expanding last mile B2B grocery delivery for offices and events.",
        ],
        "focus_areas": ["Ultra-fast delivery", "Smart carts", "B2B delivery", "Data monetization"],
    },
    "DoorDash": {
        "description": "On-demand marketplace extending last mile beyond restaurants into convenience and grocery.",
        "last_mile_highlights": [
            "DoorDash Drive white-label last mile API used by 100,000+ business locations.",
            "DashMart dark-store network in 30+ US cities for 15–30 minute delivery.",
            "Package delivery partnerships with FedEx and Ulta Beauty for same-hour drop-offs.",
            "Wolt partnership accelerating international last mile expansion model back to US playbook.",
        ],
        "focus_areas": ["Drive API", "Dark stores", "Package delivery", "On-demand logistics"],
    },
    "Shopify": {
        "description": "E-commerce platform building distributed last mile fulfillment for independent merchants.",
        "last_mile_highlights": [
            "Shopify Fulfillment Network (SFN) routing orders to nearest fulfillment center for 2-day delivery.",
            "Shop Promise badge signaling reliable 2-day delivery directly on merchant storefronts.",
            "Shopify Shipping integrations with USPS, UPS, DHL reducing label costs up to 88%.",
            "Deliverr acquisition strengthening last mile capacity for 10,000+ Shopify sellers.",
        ],
        "focus_areas": ["Fulfillment network", "Shop Promise", "Carrier integrations", "SMB enablement"],
    },
}


def get_daily_report() -> dict:
    """
    Generate the daily Last Mile e-commerce news report.

    Returns a structured report containing today's date, a summary, and
    per-competitor Last Mile highlights for all tracked US e-commerce players.
    """
    today = date.today().isoformat()

    report = {
        "report_date": today,
        "title": "Daily US E-Commerce Last Mile Report",
        "summary": (
            "Curated daily highlights covering Last Mile delivery strategies, "
            "innovations, and competitive moves from leading US e-commerce operators. "
            "Focus areas include same-day delivery, autonomous vehicles, carrier networks, "
            "sustainability, and technology-enabled fulfillment."
        ),
        "competitors": [],
    }

    for name, data in COMPETITORS.items():
        report["competitors"].append(
            {
                "name": name,
                "description": data["description"],
                "last_mile_highlights": data["last_mile_highlights"],
                "focus_areas": data["focus_areas"],
            }
        )

    return report
