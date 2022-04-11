import string


class Message:
    """
    A Message class. Allows to store messages in an orderly fashion.

    Parameters
    ----------
    m_id : int
        Incremental id of the message sent.
    _body : str
        String of a body text of message.
    sender : str
        Name of a sender.

    Attributes
    ----------
    message_id : int
        Incremental id of the message sent.
    message_body : str
        String of a body text of message.
    message_sender : str
        Name of a sender.
    message_read : bool
        If the message already read or not.
    """
    def __init__(self, m_id, body, sender):
        self.message_id = m_id
        self.message_body = body
        self.message_sender = sender
        self.message_read = False

    def get_details(self):
        """
        The function return details of message.

        Returns
        -------
        str
            String with message's details.

        """
        return {"Id: " + str(self.message_id) + ", Body: " + self.message_body + ", Sender: " + self.message_sender +\
                 ", Read: " + str(self.message_read)}

    def set_read(self, status_read):
        """
        The function that change status of message. Read or not read.

        Parameters
        -------
        status_read : bool
            New status of read.

        """
        self.message_read = status_read


class PostOffice:
    """
    A Post Office class. Allows users to message each other.

    Parameters
    ----------
    usernames : list
        Users for which we should create PO Boxes.

    Attributes
    ----------
    message_id : int
        Incremental id of the last message sent.
    boxes : dict
        Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """
        Send a message to a recipient.

        Parameters
        ----------
        sender : str
            The message sender's username.
        recipient : str
            The message recipient's username.
        message_body : str
            The body of the message.
        urgent : bool, optional
            The urgency of the message.
            Urgent messages appear first.

        Returns
        -------
        int
            The message ID, auto incremented number.

        Raises
        ------
        KeyError
            If the recipient does not exist.

        Examples
        --------
        After creating a PO box and sending a letter,
        the recipient should have 1 messege in the
        inbox.

        >>> po_box = PostOffice(['a', 'b'])
        >>> message_id = po_box.send_message('a', 'b', 'Hello!')
        >>> len(po_box.boxes['b'])
        1
        >>> message_id
        1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = Message(self.message_id, message_body, sender)
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return message_details.message_id

    def read_inbox(self, user, number_of_message=0):
        """
        Return the messages of a user.

        Parameters
        ----------
        user : str
            The user's name.
        number_of_message : str
            How mach message to return.
            If the user don't move any number, return all the message.

        Returns
        -------
        list
            The message in g-mail of user.

        Raises
        ------
        KeyError
            If the user does not exist.
        """
        # Take only message that not read.
        message_read = [message for message in self.boxes[user] if message.message_read is False]
        # Take only message the user ask.
        message_read = message_read[0:number_of_message] if number_of_message > 0 else message_read

        for message in message_read:
            message.set_read(True)

        return [message.get_details() for message in message_read]

    def search_inbox(self, user, part_message):
        """
        The function find messages (of the user) that containing the part message.

        Parameters
        ----------
        user : str
            The user's name.
        part_message : str
            Sub message.

        Returns
        -------
        list
            The messages that containing the part message.

        Raises
        ------
        KeyError
            If the user does not exist.
        """
        return [message.get_details() for message in self.boxes[user]
                if str(message.message_body).__contains__(part_message)]


def show_example():
    """Show example of using the PostOffice class."""
    users = ('Newman', 'Mr. Peanutbutter')
    post_office = PostOffice(users)

    # function send_message():
    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    print(f"Successfuly sent message number {message_id}.")

    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello world, Newman.',
    )
    print(f"Successfuly sent message number {message_id}.")

    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Good bye, Newman.',
    )
    print(f"Successfuly sent message number {message_id}.")

    # function read_inbox():
    print(f'\nread_inbox with number 1: {post_office.read_inbox("Newman", 1)}')
    print(f'read_inbox with number 1: {post_office.read_inbox("Newman", 1)}')

    # function search_inbox():
    print(f'\nsearch_inbox - "Good": {post_office.search_inbox("Newman", "Good")}')
    print(f'search_inbox - "llo": {post_office.search_inbox("Newman", "llo")}')
    print(f'search_inbox - "hi": {post_office.search_inbox("Newman", "hi")}')


def main():
    show_example()


if __name__ == '__main__':
    main()
    