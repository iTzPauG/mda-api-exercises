import unittest

from flask import json

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.note_create import NoteCreate  # noqa: E501
from openapi_server.models.note_list_response import NoteListResponse  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNotesController(BaseTestCase):
    """NotesController integration test stubs"""

    def test_notes_get(self):
        """Test case for notes_get

        List notes (paginated)
        """
        query_string = [('page', 1),
                        ('per_page', 10),
                        ('q', 'q_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/notes',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notes_id_get(self):
        """Test case for notes_id_get

        Get note by id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/notes/{id}'.format(id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notes_post(self):
        """Test case for notes_post

        Create a note
        """
        note_create = {"title":"title","content":"content"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/notes',
            method='POST',
            headers=headers,
            data=json.dumps(note_create),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
