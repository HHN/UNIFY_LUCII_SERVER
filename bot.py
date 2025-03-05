#!/usr/bin/env python3

from nio import AsyncClient, RoomMessageText, LoginResponse
from flask import Flask, request, jsonify
import asyncio
import time

app = Flask(__name__)

client = AsyncClient("https://matrix.com", "@bot_user:matrix.com")

# Replace with your list of user IDs
all_user_ids = ["@userA:matrix.com", "@userB:matrix.com"]

# This will store the matched pairs for anonymous chatting
matched_pairs = {}

async def ensure_logged_in():
    if not client.logged_in:
        await client.login("password")

@app.route('/create_event', methods=['POST'])
async def create_event():
    await ensure_logged_in()
    event_data = request.json
    event_id = generate_event_id()
    event_data['id'] = event_id

    # Store the event creator info to manage anonymous chats later
    matched_pairs[event_id] = {"creator": event_data['creator'], "is_group": event_data['is_group']}
    
    await broadcast_event(event_data)
    return jsonify({"status": "Event created and broadcasted", "event_id": event_id}), 201

def generate_event_id():
    # Generate a unique event ID
    return f"event_{int(time.time())}"

async def broadcast_event(event_data):
    content = {
        "msgtype": "m.text",
        "body": f"Event Name: {event_data['name']}\nEvent Details: {event_data['details']}\nKeywords: {event_data['keywords']}\nEvent ID: {event_data['id']}"
    }
    for user_id in all_user_ids:
        await client.room_send(
            room_id=user_id,
            message_type="m.room.message",
            content=content
        )

async def message_callback(room, event):
    try:
        sender = event.sender
        message = event.body['body']  # Correct way to access the message body
        print(f"Received message from {sender}: {message}")

        if message.startswith("reply:"):
            event_id = message.split(":")[1].strip()
            if event_id in matched_pairs:
                creator = matched_pairs[event_id]["creator"]
                recipient = matched_pairs[event_id].get("recipient")
                if not recipient:
                    matched_pairs[event_id]["recipient"] = sender
                    recipient = sender
                
                if matched_pairs[event_id]["is_group"]:
                    # Handle group event replies
                    # You can add logic to manage group chats if needed
                    pass
                else:
                    content = {
                        "msgtype": "m.text",
                        "body": message.split(":", 2)[2].strip()
                    }
                    await client.room_send(
                        room_id=creator if sender != creator else recipient,
                        message_type="m.room.message",
                        content=content
                    )
    except Exception as e:
        print(f"Failed to forward message: {e}")

client.add_event_callback(message_callback, RoomMessageText)

async def sync_loop(client):
    while True:
        await client.sync(timeout=30000)  # Sync every 30 seconds

async def main():
    try:
        login_response = await client.login("password")
        if isinstance(login_response, LoginResponse) and login_response.user_id:
            print(f"Logged in as {login_response.user_id}")
        else:
            print("Failed to log in, missing user_id in response")
            return
    except Exception as e:
        print(f"Failed to log in: {e}")
        return

    asyncio.create_task(sync_loop(client))
    await asyncio.Event().wait()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    app.run(host='0.0.0.0', port=5000)
