# Daily Postcard

**Daily Postcard** is a simple web scraper designed to fetch information about today's public holidays from various web pages and post them to a designated Telegram channel. This project can be seamlessly integrated with Google Cloud (gcloud) and scheduled to run at specified intervals.

Subscribe to the existing Telegram channel using the following link: [HOLIDAYS DAILY](https://t.me/what_day_is_it_now)

## Usage

To deploy this project, follow these steps:

```bash
git clone https://github.com/your-username/daily-postcard.git
cd daily-postcard
```
Set up your environment variables by providing them to the deployment script:

```bash
gcloud run jobs deploy daily-postcard \
    --source . \
    --set-env-vars DP_TARGET_CHAT_ID=<your_chat_id>,DP_BOT_ACCESS_TOKEN=<your_bot_token> \
    --max-retries 5 \
    --region your-preferred-region \
    --project=your-gcp-project-id
```

## Contributing
If you have ideas for improvements, new features, or bug fixes, feel free to open an issue or submit a pull request. Contributions are welcome and encouraged!
