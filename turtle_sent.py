import string


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
    read : bool
        If the message already read or not.
    boxes : dict
        Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.read = False
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
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': self.read
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

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

        len_message = len(self.boxes[user])
        # Take only message that not read.
        message_read = [message for message in self.boxes[user] if message['read'] is False]
        # Take only message the user ask.
        message_read = message_read[0:number_of_message] if number_of_message > 0 else message_read

        for message in message_read:
            for i in range(len_message):
                if self.boxes[user][i]['id'] == message['id']:
                    self.boxes[user][i]['read'] = True

        return message_read

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
        return [message for message in self.boxes[user] if str(message['body']).__contains__(part_message)]


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