import nostr

def main():
    # Create a NOSTR client
    client = nostr.Client()

    # Get the bot's username
    username = "my_bot_username"

    # Set up a message handler
    def handle_message(message):
        if message.username == username:
            message.reply("Hello, there!")

    # Start listening for messages
    client.on_message(handle_message)

    # Run the bot
    client.run()

if __name__ == "__main__":
    main()
      