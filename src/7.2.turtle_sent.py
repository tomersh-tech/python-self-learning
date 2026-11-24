"""Exercise 7.2 - Turtle sent.

A post office that lets users send, read and search messages.

Changes to the original PostOffice class from the notebook:
    * Messages now have a title, because search_inbox has to search in
      titles. It is the last parameter of send_message and defaults to
      an empty string, so existing calls keep working.
    * Messages now have an "is_read" flag, so read_inbox can skip
      messages that were already read.
    * Added type hints, and replaced the "+ 1" assignment with "+=".
"""
from typing import Any, Iterable, Optional

Message = dict[str, Any]

ID_KEY = "id"
TITLE_KEY = "title"
BODY_KEY = "body"
SENDER_KEY = "sender"
IS_READ_KEY = "is_read"


class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames: Users for which we should create PO Boxes.

    Attributes:
        message_id: Incremental id of the last message sent.
        boxes: Users' inboxes, from username to a list of messages.
    """

    def __init__(self, usernames: Iterable[str]) -> None:
        self.message_id = 0
        self.boxes: dict[str, list[Message]] = {
            user: [] for user in usernames
        }

    def send_message(
        self,
        sender: str,
        recipient: str,
        message_body: str,
        urgent: bool = False,
        title: str = "",
    ) -> int:
        """Send a message to a recipient.

        Args:
            sender: The message sender's username.
            recipient: The message recipient's username.
            message_body: The body of the message.
            urgent: Urgent messages appear first in the inbox.
            title: The title of the message.

        Returns:
            The message ID, an auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            ID_KEY: self.message_id,
            TITLE_KEY: title,
            BODY_KEY: message_body,
            SENDER_KEY: sender,
            IS_READ_KEY: False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(
        self, username: str, count: Optional[int] = None
    ) -> list[Message]:
        """Return the first unread messages of a user and mark them as read.

        Messages that were already read are not returned again.

        Args:
            username: The user whose inbox to read.
            count: How many messages to read. If not given, all the unread
                messages are returned.

        Returns:
            The messages that were read, in inbox order.

        Raises:
            KeyError: If the user does not exist.
            ValueError: If count is negative.
        """
        if count is not None and count < 0:
            raise ValueError("count can't be negative.")

        unread_messages = [
            message for message in self.boxes[username]
            if not message[IS_READ_KEY]
        ]
        messages_to_read = unread_messages[:count]
        for message in messages_to_read:
            message[IS_READ_KEY] = True
        return messages_to_read

    def search_inbox(self, username: str, text: str) -> list[Message]:
        """Return all of a user's messages that contain a string.

        Both read and unread messages are searched, in the title and
        in the body. The search is case sensitive.

        Args:
            username: The user whose inbox to search.
            text: The string to look for.

        Returns:
            The matching messages, in inbox order.

        Raises:
            KeyError: If the user does not exist.
        """
        return [
            message for message in self.boxes[username]
            if text in message[TITLE_KEY] or text in message[BODY_KEY]
        ]


def turtle_sent() -> None:
    """Show an example of sending, reading and searching messages."""
    post_office = PostOffice(["Newman", "Mr. Peanutbutter"])
    post_office.send_message(
        "Mr. Peanutbutter", "Newman", "Hello, Newman.", title="Hi"
    )
    post_office.send_message(
        "Mr. Peanutbutter", "Newman", "Lunch at noon?", title="Lunch"
    )
    print(post_office.search_inbox("Newman", "Lunch"))
    print(post_office.read_inbox("Newman", 1))
    print(post_office.read_inbox("Newman"))
    print(post_office.read_inbox("Newman"))


if __name__ == "__main__":
    turtle_sent()
