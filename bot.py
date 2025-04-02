
from apify_client import ApifyClient

# Initialize the ApifyClient with your Apify API token
# Replace '<YOUR_API_TOKEN>' with your token.
client = ApifyClient("7551049610:AAG2cCdhEjKU8RSn_qgP87urZr1C4AYEzWk")

# Prepare the Actor input
run_input = { "video_urls": ["https://www.terabox.com/sharing/embed?surl=Aniwje1yO1cWz0uiVHud_A&resolution=720&autoplay=true&mute=false&uk=4400272805412&fid=305068574050618"] }

# Run the Actor and wait for it to finish
run = client.actor("scraper-mind/terabox-downloader").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)

# 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/python/docs/quick-start
