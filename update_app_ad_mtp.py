"""One-off script to update Mobile To PC app ad assets via create-and-replace."""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from auth import GoogleAdsAuthManager
from tools_ads import AdTools

CUSTOMER_ID = "8185974927"
AD_GROUP_ID = "108855420620"
AD_ID = "460588688827"
HEADLINES = [
    "Transfer Files Phone to PC",
    "No USB Cable Needed",
    "Faster Transfers v11.7",
    "Wi-Fi & Hotspot Transfer",
    "Android 16 Ready",
]
DESCRIPTIONS = [
    "Transfer photos & files wirelessly. No USB—works on Wi-Fi, hotspot, or mobile data.",
    "v11.7: faster transfers, Android 16 ready, dark mode. Needs FTP Manager on PC.",
    "Move files between Android and Windows PC in seconds. Password-protected profiles.",
    "Create, move & delete files from your PC. Multiple profiles for home, work & travel.",
    "Free from Deskshare. Setup takes minutes—watch the tutorial at deskshare.com.",
]


async def main() -> None:
    auth = GoogleAdsAuthManager()
    tools = AdTools(auth, error_handler=None)
    result = await tools.update_ad(
        CUSTOMER_ID,
        AD_GROUP_ID,
        AD_ID,
        headlines=HEADLINES,
        descriptions=DESCRIPTIONS,
    )
    print("SUCCESS:", result)


if __name__ == "__main__":
    asyncio.run(main())
